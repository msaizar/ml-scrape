# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Identity


class MLItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()

    description = scrapy.Field()
    latest_questions = scrapy.Field()


def filter_empty(x):
    return None if not x else x


class MLItemLoader(ItemLoader):

    default_output_processor = TakeFirst()

    title_in = MapCompose(str.strip)
    description_in = MapCompose(str.strip, filter_empty)
    price_in = MapCompose(str.strip)
    currency_in = MapCompose(str.strip)

    latest_questions_out = Identity()
    description_out = Identity()
