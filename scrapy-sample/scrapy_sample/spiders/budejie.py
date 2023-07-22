import scrapy
from scrapy_sample.items import BudejieItem


class BudejieSpider(scrapy.Spider):
    """百思不得姐段子的爬虫"""
    name = 'budejie'
    start_urls = ['http://www.budejie.com/text/']
    total_page = 5

    def parse(self, response):
        current_page = int(response.css('a.z-crt::text').extract_first())
        lies = response.css('div.j-r-list >ul >li')
        for li in lies:
            username = li.css('a.u-user-name::text').extract_first()
            content = '\n'.join(li.css('div.j-r-list-c-desc a::text').extract())
            yield BudejieItem(username=username, content=content)
        if current_page < self.total_page:
            yield scrapy.Request(self.start_urls[0] + f'{current_page+1}')
