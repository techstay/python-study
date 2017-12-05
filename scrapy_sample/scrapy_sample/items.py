# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapySampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    referer = scrapy.Field()


class BudejieItem(scrapy.Item):
    username = scrapy.Field()
    content = scrapy.Field()


class CsdnBlogItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
