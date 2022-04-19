# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyDangdangItem(scrapy.Item):
    # 图片
    src = scrapy.Field()
    # 名称
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
