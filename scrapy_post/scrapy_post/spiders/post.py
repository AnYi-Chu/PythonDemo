import json

import scrapy


class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['fanyi.baidu.com/sug']

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        data = {
            'kw': 'final'
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        obj = json.loads(content, encoding='utf-8')
        print(obj)
