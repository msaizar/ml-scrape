import scrapy

from ..items import MLItem, MLItemLoader


class MLSpider(scrapy.Spider):
    name = 'ml'
    start_urls = [
        'https://listado.mercadolibre.com.uy/technics-1200'
    ]

    def parse_item(self, response):
        item = MLItemLoader(item=MLItem(), response=response)
        item.add_value('url', response.url)
        item.add_css('title', '.item-title__primary ::text')

        item.add_xpath(
            'description',
            '//div[contains(@class, "item-description__html-text")]'
            '/descendant-or-self::*/text()'
        )

        item.add_css('image_urls', 'label.gallery__thumbnail img::attr(src)')
        item.add_css('price', '.price-tag-fraction ::text')
        item.add_css('currency', '.price-tag-symbol ::text')

        question_groups = response.css('.questions__group')

        for question_group in question_groups:
            obj = {}
            obj['question'] = question_group.css(
                '.questions__item--question p::text'
            ).extract_first().strip()
            answer = question_group.css(
                '.questions__item--answer p::text'
            ).extract_first()
            if answer:
                obj['answer'] = answer.strip()

            item.add_value('latest_questions', obj)

        yield item.load_item()

    def parse(self, response):
        for href in response.css('.item__info-link'):
            next_page = href.css('::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(
                    next_page,
                    callback=self.parse_item
                )
