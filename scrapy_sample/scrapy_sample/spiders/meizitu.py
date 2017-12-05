# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    start_urls = ['http://www.meizitu.com/a/5501.html',
                  'http://www.meizitu.com/a/5524.html']

    def parse(self, response):
        yield ImageItem(image_urls=response.css('div#picture img::attr(src)').extract())
