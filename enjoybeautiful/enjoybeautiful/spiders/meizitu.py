import scrapy


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['https://www.mzitu.com/231755',
                  'https://www.mzitu.com/92910']

    def parse(self, response):
        url = response.xpath('''//div[@class='main-image']//img/@src''').get()
        yield {'url': url}
        total_page = int(response.xpath(
            '''//div[@class='pagenavi']//span/text()''').getall()[-2])
        for i in range(2, total_page+1):
            yield scrapy.Request(response.url+f'/{i}')
