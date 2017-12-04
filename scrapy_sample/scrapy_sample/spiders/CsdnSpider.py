import scrapy
import urllib.parse


class CsdnBlogSpider(scrapy.Spider):
    """我的CSDN所有文章和链接的爬虫"""
    name = 'csdn_blog'
    start_urls = ['http://blog.csdn.net/u011054333/article/list/1']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = 'http://blog.csdn.net'

    def parse(self, response):
        articles = response.css('div#article_list div.article_item')
        for article in articles:
            list1 = article.css('div.article_title a::text').extract()
            list2 = [e.strip() for e in list1 if e.strip()]
            title = list2[0]
            link = self.base_url + article.css('div.article_title a::attr(href)').extract_first().strip()
            yield {'title': title, 'link': link}

        pages = response.css('div#papelist')
        next_page_url = pages.css('a').re_first('<a href=\"(.*)\">下一页')
        if next_page_url is not None:
            yield scrapy.Request(urllib.parse.urljoin(self.base_url, next_page_url))
