import scrapy

from scrapy_movie.scrapy_movie.items import ScrapyMovieItem


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/china/index.html']

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'https://www.dytt8.net' + href
            yield scrapy.Request(url=url, callback=self.pars_second, method={'name': name})

    def pars_second(self, response):
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']
        movie = ScrapyMovieItem(src=src, name=name)
        yield movie
