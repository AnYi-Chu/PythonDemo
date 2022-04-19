# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request

from itemadapter import ItemAdapter


class ScrapyDangdangPipeline:
    # 执行爬虫文件前
    def open_spider(self, spider):
        self.fp = open('fp/book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # write方法必须写一个字符串，w模式会覆盖
        # with open('fp/book.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item

    # 执行爬虫文件后
    def close_spider(self, spider):
        self.fp.close()


# 定义新管道
class DownloadPipeline:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        filename = 'fp/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
