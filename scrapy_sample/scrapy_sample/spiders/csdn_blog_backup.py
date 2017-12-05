# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
from scrapy import Request
from scrapy_sample.items import CsdnBlogItem


class CsdnBlogBackupSpider(scrapy.Spider):
    name = 'csdn_backup'
    start_urls = ['https://passport.csdn.net/account/login']
    base_url = 'http://write.blog.csdn.net/postlist/'
    get_article_url = 'http://write.blog.csdn.net/mdeditor/getArticle?id='

    def __init__(self, name=None, username=None, password=None, **kwargs):
        super(CsdnBlogBackupSpider, self).__init__(name=name, **kwargs)
        if username is None or password is None:
            raise Exception('没有用户名和密码')
        self.username = username
        self.password = password

    def parse(self, response):
        lt = response.css('form#fm1 input[name="lt"]::attr(value)').extract_first()
        execution = response.css('form#fm1 input[name="execution"]::attr(value)').extract_first()
        eventid = response.css('form#fm1 input[name="_eventId"]::attr(value)').extract_first()
        return FormRequest.from_response(
            response,
            formdata={
                'username': self.username,
                'password': self.password,
                'lt': lt,
                'execution': execution,
                '_eventId': eventid
            },
            callback=self.redirect_to_articles
        )

    def redirect_to_articles(self, response):
        return Request(CsdnBlogBackupSpider.base_url, callback=self.get_all_articles)

    def get_all_articles(self, response):
        import re
        text = response.css('div.page_nav span::text').extract_first()
        total_page = int(re.findall(r'共(\d+)页', text)[0])
        for i in range(1, total_page + 1):
            yield Request(CsdnBlogBackupSpider.base_url + f'0/0/enabled/{i}', callback=self.parse_article_links)

    def parse_article_links(self, response):
        article_links = response.xpath('//table[@id="lstBox"]/tr[position()>1]/td[1]/a[1]/@href').extract()
        last_index_of = lambda x: x.rfind('/')
        article_ids = [link[last_index_of(link) + 1:] for link in article_links]
        for id in article_ids:
            yield Request(CsdnBlogBackupSpider.get_article_url + id, callback=self.parse_article_content)

    def parse_article_content(self, response):
        import json
        obj = json.loads(response.body, encoding='UTF8')
        yield CsdnBlogItem(title=obj['data']['title'], content=obj['data']['markdowncontent'])
