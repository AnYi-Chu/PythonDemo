import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['bj.58.com']
    start_urls = ['http://bj.58.com/']

    def parse(self, response):
        print(response.text)
        print(response.body)
        print(response.xpth('//*[@id="homeNav"]/a'))
