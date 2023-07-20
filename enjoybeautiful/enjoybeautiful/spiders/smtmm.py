import scrapy
from .. import items


class SmtmmSpider(scrapy.Spider):
    name = 'smtmm'
    allowed_domains = ['smtmm.win']
    start_urls = ['https://smtmm.win/article/52735/']

    def parse(self, response):
        image_urls = response.css(
            'article.article-content img::attr(data-original)').getall()
        # yield items.MyImageItem(image_urls=map(lambda x: response.urljoin(x), image_urls))
        for i in map(lambda x: response.urljoin(x), image_urls):
            yield {'url': i}
