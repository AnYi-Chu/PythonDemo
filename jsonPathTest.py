# _*_ coding : utf-8 _*_
# @Time : 2022/4/13 5:20
# @Author : gaohao
# @File : jsonpathTest
# @Project : demo
import json
import jsonpath
import urllib.request

# obj = json.load(open('.json', 'r', encoding='utf-8'))
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# author_list = jsonpath.jsonpath(obj, '$..author')
# tag_list = jsonpath.jsonpath(obj, '$.store.*')
# price_list = jsonpath.jsonpath(obj, '$.store..price')
# book = jsonpath.jsonpath(obj, '$..book[2]')
# book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# book = jsonpath.jsonpath(obj, '$..book[0,1]')
# book = jsonpath.jsonpath(obj, '$..book[:2]')
# book_list = jsonpath.jsonpath(obj, '$..book[?@.isbn]')
# book_list = jsonpath.jsonpath(obj, '$..book[?(@price>10)]')

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1649799608729_97&jsoncallback=jsonp98&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1649799608729_97&jsoncallback=jsonp98&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': ' gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 't=54d37d80b9ec8d133cb9fa4fa56b813a; cookie2=13592cd9dfc9c6628aaae70ab9404c23; v=0; _tb_token_=e909ee16b03ee; cna=WN/cGsj2fTQCAXJfIQVqbqKM; xlly_s=1; tfstk=ciHVB7VZNKp4Pow69-ww5EW33bVAZ9omjTrQie0pTTIw64Pci6_Tq4-74lsPSSf..; l=eBLKcJPeLiul97JhBO5anurza77OrIOb4sPzaNbMiInca6IVtFZISNC3Fg3WSdtjgtCjDety52gX3RLHR3AgCc0c0KDtBacSFxvO.; isg=BPLyK4GPxFipT_hkHW2vDLppQzjUg_YdrEP0gLzKX6WQT5JJpBHgLcShP-tzP261',
    'referer': 'https://dianying.taobao.com/index.htm?spm=a1z21.6646273.header.3.613c4890iK1czN&n_s=new',
    'sec-ch-ua': ' "Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]
with open('../../Desktop/demo/fp/test.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
obj = json.load(open('../../Desktop/demo/fp/test.json', 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj, '$..regionName')
print(city_list)
