# _*_ coding : utf-8 _*_
# @Time : 2022/4/11 19:26
# @Author : gaohao
# @File : urllibTest
# @Project : demo
# 包
import random
import urllib.request

# 类型与方法
url = 'http://www.baidu.com'
# response=urllib.request.urlopen(url)
# content = response.read(3)
# content = response.readline()
# content = response.readlines()
# print(type(response))
# print(response.getcode())
# print(response.geturl())
# print(response.getheaders())


# 下载
urllib.request.urlretrieve(url, "baidu.html")
# urllib.request.urlretrieve(url=url_img,filename="img.jpg")
# urllib.request.urlretrieve(url_video,"video.mp4")


# get请求
# url = 'http://www.baidu.com/s?'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36'
# }
# name = urllib.parse.quote('刘德华')
# request = urllib.request.Request(url=url + 'wd=' + name, headers=headers)
# data = {
#     'wd': '刘德华',
#     'sex': '男',
# }
# par = urllib.parse.urlencode(data)
# request = urllib.request.Request(url=url + par, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode("utf-8")
# print(content)


# post请求
# url = 'https://fanyi.baidu.com/sug'
# url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
# headers = {
#     'Accept': ' */*',
#     #'Accept-Encoding': ' gzip, deflate, br',
#     'Accept-Language': ' zh-CN,zh;q=0.9',
#     'Connection': ' keep-alive',
#     'Content-Length': ' 132',
#     'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
#     'Cookie: BIDUPSID=F117EFEE7FDCD4F8E42D098597C77ECC; PSTM=1649683130; BAIDUID=F117EFEE7FDCD4F88BBA64D0FA81AC95': 'FG=1; H_PS_PSSID=35838_36176_31660_34813_35914_36165_34584_36141_36120_36192_35978_36126_35802_36233_26350_36100_36061; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1649684285; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; BA_HECTOR=0ka4250480ah81alc31h58cu40r; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1649687356; ab_sr=1.0.1_MjUxMGU5MjQ3MjVjMWY0OGI5OWJjOGEwYTI3MjYzN2I0ZTFkZTdmZDg2MDIyYzU5OTNmMjkyYTIxMTdkMDZkNDRhYWM5ZGFkNzczYzdjODVkNjdmOGY5ZWM3MGRlOWFlNGQ2NDZkZTllYzBjY2JmODhiNGE1ZTM1MjA4YzlhYTM4NDlmODMzODJiZmI2YzA0NGM0YTVkMmY1OWE3NjQwZQ==',
#     'Host': ' fanyi.baidu.com',
#     'Origin: https': '//fanyi.baidu.com',
#     'Referer: https': '//fanyi.baidu.com/translate?aldtype=16047&query=%0D%0A&keyfrom=baidu&smartresult=dict&lang=auto2zh',
#     'Sec-Fetch-Dest': ' empty',
#     'Sec-Fetch-Mode': ' cors',
#     'Sec-Fetch-Site': ' same-origin',
#     'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
#     'X-Requested-With': ' XMLHttpRequest',
#     'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
#     'sec-ch-ua-mobile': ' ?0',
#     'sec-ch-ua-platform': ' "Windows"',
# }
# data = {
#     'kw': 'spider'
# }
# data = {
#     'from': ' en',
#     'to': ' zh',
#     'query': ' l',
#     'transtype': ' realtime',
#     'simple_means_flag': ' 3',
#     'sign': ' 501460.214501',
#     'token': ' 5a6f252106ba615984bf1c14ab94589c',
#     'domain': ' common',
# }
# par = urllib.parse.urlencode(data).encode("utf-8")
# request = urllib.request.Request(url=url, data=par, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode("utf-8")
# js = json.loads(content)
# print(js)

# ajax的get
# url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start=0&limit=20'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
# }
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# fp = open('fp/test.json', 'w', encoding='utf-8')
# fp.write(content)
# with open('fp/test.json', 'w', encoding='utf-8') as fp:
#     fp.write(content)
# print(content)

# def create_request(page):
#     base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&'
#     data = {
#         'start': (page - 1) * 20,
#         'limit': 20
#     }
#     data = urllib.parse.urlencode(data)
#     url = base_url + data
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
#     }
#     request = urllib.request.Request(url=url, headers=headers)
#     return request
#
#
# def get_content(request):
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf-8')
#     return content
#
#
# def down_load(page, content):
#     with open('fp/douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
#         fp.write(content)
#
#
# start_page = int(input())
# end_page = int(input())
# for page in range(start_page, end_page + 1):
#     request = create_request(page)
#     content = get_content(request)
#     down_load(page, content)

# ajax的post
# def create_request(page):
#     base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
#     data = {
#         'cname': '北京',
#         'pid': '',
#         'keyword': '名称或地址',
#         'pageIndex': page,
#         'pageSize': '10'
#     }
#     data = urllib.parse.urlencode(data).encode('utf-8')
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
#     }
#     request = urllib.request.Request(url=base_url, data=data, headers=headers)
#     return request
#
#
# def get_content(request):
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf-8')
#     return content
#
#
# def down_load(page, content):
#     with open('fp/kdj_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
#         fp.write(content)
#
#
# start_page = int(input())
# end_page = int(input())
# for page in range(start_page, end_page):
#     request = create_request(page)
#     content = get_content(request)
#     down_load(page, content)

# 异常
# url = 'https://blog.csdn.net/sulix/article/details/119818949'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
# }
# try:
#     request = urllib.request.Request(url=url, headers=headers)
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf-8')
# except urllib.error.HTTPError:
#     print('x')
# except urllib.error.URLError:
#     print('o')

# cooke使用
# url = 'https://user.qzone.qq.com/963643059'
# headers = {
#     # ':authority': ' user.qzone.qq.com',
#     # ':method': ' GET',
#     # ':path': ' /963643059',
#     # ':scheme': ' https',
#     'accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     # 'accept-encoding': ' gzip, deflate, br',
#     'accept-language': ' zh-CN,zh;q=0.9',
#     'cache-control': ' max-age=0',
#     'cookie': ' _qpsvr_localtk=0.11019781977658138; pgv_pvid=4590406040; pgv_info=ssid=s5466410217; ptui_loginuin=963643059; uin=o0963643059; skey=@Y9LRyMzkS; RK=WK1wrHFgdC; ptcz=e00dd18f92d2d2308569a8ca71015469c8af40e13ec26e13e8fc72c2c3cd19ff; p_uin=o0963643059; pt4_token=BIA4blgA2zBY-4X4dW061ItnqJLIB7vc*L*NFU1u-kc_; p_skey=kuAOoxBsxYB1atJw-X6ZYDRp8SjjQleJY*L1pXRWxoo_; Loading=Yes; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=4',
#     'if-modified-since: Tue, 12 Apr 2022 12:24': '04 GMT',
#     'referer: https': '//qzs.qq.com/',
#     'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
#     'sec-ch-ua-mobile': ' ?0',
#     'sec-ch-ua-platform': ' "Windows"',
#     'sec-fetch-dest': ' document',
#     'sec-fetch-mode': ' navigate',
#     'sec-fetch-site': ' same-site',
#     'sec-fetch-user': ' ?1',
#     'upgrade-insecure-requests': ' 1',
#     'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
# }
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# with open('fp\qq.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)

# handler使用
# url = 'http://www.baidu.com'
# headers = {
#     'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
# }
# request = urllib.request.Request(url=url, headers=headers)
# handler = urllib.request.HTTPHandler()
# opener = urllib.request.build_opener(handler)
# response = opener.open(request)
# content = response.read().decode('utf-8')
# print(content)

# 代理
# url = 'http://www.baidu.com/s?wd=ip'
# headers = {
#     'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
# }
# request = urllib.request.Request(url=url, headers=headers)
# proxies = {
#     'http': '112.250.107.37:53281'
# }
# handler = urllib.request.ProxyHandler(proxies=proxies)
# opener = urllib.request.build_opener(handler)
# response = opener.open(request)
# content = response.read().decode('utf-8')
# with open('fp\daili.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)

# url = 'http://www.baidu.com/s?wd=ip'
# headers = {
#     'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
# }
# request = urllib.request.Request(url=url, headers=headers)
# proxise_pool = [
#     {'http': '112.250.107.37:53281'},
#     {'http': '112.250.107.37:53282'}
# ]
# proxies = random.choice(proxise_pool)
# handler = urllib.request.ProxyHandler(proxies=proxies)
# opener = urllib.request.build_opener(handler)
# response = opener.open(request)
# content = response.read().decode('utf-8')
# with open('fp\daili.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)
