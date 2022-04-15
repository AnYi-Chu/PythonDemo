# _*_ coding : utf-8 _*_
# @Time : 2022/4/13 1:32
# @Author : gaohao
# @File : xpathTest
# @Project : demo
from lxml import etree
import urllib.request


# xpath解析本地文件
# tree = etree.parse('fp/test.html')
# li_list = tree.xpath('//body/ul/li')
# li_list = tree.xpath('//li[@id="a1"]/text()')
# li_list = tree.xpath('//li[@id="a1"]/@class')
# li_list=tree.xpath('//li[contains(@id,"1")]/text()')
# li_list = tree.xpath('li[starts-with(@id,"c")]/text()')
# li_list = tree.xpath('li[@id="a1" and @class="c1"]/text()')
# li_list = tree.xpath('//li[@id="a1"or @id="b2"]/text()')
# print(li_list)
# print(len(li_list))

# xpath解析网页
# url = 'https://www.baidu.com/'
# headers = {
#     'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
# }
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# tree = etree.HTML(content)
# result = tree.xpath('//input[@id="su"]/@value')[0]
# print(result)

# 站点爬取图片
# def create_request(page):
#     if (page == 1):
#         url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
#     else:
#         url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'
#     headers = {
#         'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
#     }
#     request = urllib.request.Request(url=url, headers=headers)
#     return request
#
#
# def get_content(request):
#     response = urllib.request.urlopen(request)
#     context = response.read().decode('utf-8')
#     return context
#
#
# def down_load(context):
#     tree = etree.HTML(context)
#     name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
#     src_list = tree.xpath('//div[@id="container"]//a/img/@src2')
#     for i in range(len(name_list)):
#         name = name_list[i]
#         src = src_list[i]
#         url = 'https:' + src
#         urllib.request.urlretrieve(url=url, filename='./img/' + name + '.jpg')
#
#
# start_page = int(input())
# end_page = int(input())
# for page in range(start_page, end_page + 1):
#     request = create_request(page)
#     context = get_content(request)
#     down_load(context)
