# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Compose, Identity, Join


class MLItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()    
    title = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    
    description = scrapy.Field()
    questions = scrapy.Field()
    answers = scrapy.Field()


def filter_empty(x):
    return None if not x else x


class MLItemLoader(ItemLoader):

    default_output_processor = TakeFirst()

    title_in = MapCompose(str.strip)
    description_in = MapCompose(str.strip, filter_empty)
    price_in = MapCompose(str.strip)
    currency_in = MapCompose(str.strip)
    questions_in = MapCompose(str.strip)
    answers_in = MapCompose(str.strip)
    
    description_out = Identity()
    questions_out = Identity()
    answers_out = Identity()