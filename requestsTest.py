# _*_ coding : utf-8 _*_
# @Time : 2022/4/14 2:20
# @Author : gaohao
# @File : requestsTest
# @Project : demo
from bs4 import BeautifulSoup
import requests
import json

# url = 'http://www.baidu.com'
# response = requests.get(url=url)
# print(type(response))
# response.encoding = 'utf-8'
# print(response.text)
# print(response.url)
# print(response.content)
# print(response.status_code)
# print(response.headers)

# get
# url = 'https://www.baidu.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
# }
# data = {
#     'wd': '北京'
# }
# response = requests.get(url=url, params=data, headers=headers)
# content = response.text
# print(content)

# post
# url = 'https://fanyi.baidu.com/sug'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
# }
# data = {
#     'kw': 'eye'
# }
# response = requests.post(url=url, data=data, headers=headers)
# content = response.text
# obj = json.loads(content)
# print(obj)

# 代理
# url = 'http://www.baidu.com/s?'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
# }
# data = {
#     'wd': 'ip'
# }
# proxy = {
#     'http': '222.66.202.6:80'
# }
# response = requests.get(url=url, params=data, headers=headers, proxies=proxy)
# content = response.text
# with open('fp/daili.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)

# cookie
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
content = response.text
soup = BeautifulSoup(content, 'lxml')
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code
session = requests.session()
response_code = session.get(code_url)
content_code = response_code.content
with open('../../Desktop/demo/fp/code.jpg', 'wb') as fp:
    fp.write(content_code)
code_name = input('输入验证码')
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '963643059@qq.com',
    'pwd': 'aweawea134678',
    'code': code_name,
    'denglu': '登录'
}
response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open('../../Desktop/demo/fp/gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
