import scrapy


class BaisibudejieSpider(scrapy.Spider):
    '''百思不得姐首页段子的爬虫'''
    name = 'jokes'
    start_urls = ['http://www.budejie.com/text/']

    def parse(self, response):
        lies = response.css('div.j-r-list >ul >li')
        for li in lies:
            username = li.css('a.u-user-name::text').extract()
            content = li.css('div.j-r-list-c-desc a::text').extract()
            yield {'username': username, 'content': content}
