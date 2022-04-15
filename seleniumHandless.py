# _*_ coding : utf-8 _*_
# @Time : 2022/4/14 2:12
# @Author : gaohao
# @File : seleniumHandless
# @Project : demo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


browser = share_browser()
url = 'https://www.baidu.com'
browser(url)
