# _*_ coding : utf-8 _*_
# @Time : 2022/4/13 20:25
# @Author : gaohao
# @File : beautifulSoupTest
# @Project : demo
from bs4 import BeautifulSoup
import urllib.request

# soup = BeautifulSoup(open('fp/test.html', encoding='utf-8'), 'lxml')
# print(soup.li)
# print(soup.li.attrs)
# print(soup.find('li', title='a1'))
# print(soup.find('li', class_='a1'))
# print(soup.find_all(['li', 'a'], limit=1))
# print(soup.select('a'))
# print(soup.select('.c1'))
# print(soup.select('#a1'))
# print(soup.select('li[id="a1"]'))
# print(soup.select('ul li'))
# print(soup.select('ul > li'))
# print(soup.select('li,a'))
# print(soup.select('#a1')[0].string)
# print(soup.select('#a1')[0].get_text())
# print(soup.select('#a1')[0].name)
# print(soup.select('#a1')[0].attrs())
# print(soup.select('#a1')[0].attrs.get('class'))

# 爬取星巴克
url = 'https://www.starbucks.com.cn/menu/'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content, 'lxml')
name_list = soup.select('ul[class="grid padded-3 product"] strong')
for name in name_list:
    print(name.string)
