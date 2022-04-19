import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始url地址
    start_urls = ['http://www.baidu.com/']

    # 执行start_urls后要执行的方法，相当于urllib.request.urlopen()或requests.get()
    def parse(self, response):
        print("爱爱")
