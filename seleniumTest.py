# _*_ coding : utf-8 _*_
# @Time : 2022/4/13 23:52
# @Author : gaohao
# @File : seleniumTest
# @Project : demo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# path = 'chromedriver.exe'
# browser = webdriver.Chrome(path)
# url = 'https://www.jd.com'
# browser.get(url)
# content = browser.page_source
# print(content)

# path = 'chromedriver.exe'
# browser = webdriver.Chrome(path)
# url = 'https://www.baidu.com'
# browser.get(url)
# # button = browser.find_element_by_id('su')
# # button = browser.find_element_by_name('wd')
# # button = browser.find_elements_by_xpath('//input[@id="su"]')
# # button = browser.find_elements_by_tag_name('input')
# # button = browser.find_elements_by_css_selector('#su')
# button = browser.find_element_by_link_text('地图')
# print(button)

# path = 'chromedriver.exe'
# browser = webdriver.Chrome(path)
# url = 'http:www.baidu.com'
# browser.get(url)
# input = browser.find_element_by_id('su')
# print(input.get_attribute('class'))
# print(input.tag_name)
# a = browser.find_element_by_link_text('新闻')
# print(a.text)

# path = 'chromedriver.exe'
# browser = webdriver.Chrome(path)
# url = 'https://www.baidu.com'
# browser.get(url)
# time.sleep(2)
# input = browser.find_element_by_id('kw')
# input.send_keys('刘德华')
# time.sleep(2)
# button = browser.find_element_by_id('su')
# button.click()
# time.sleep(2)
# js_bottom = 'document.documentElement.scrollTop=100000'
# browser.execute_script(js_bottom)
# time.sleep(2)
# next = browser.find_element_by_xpath('//a[@class="n"]')
# next.click(2)
# time.sleep(2)
# browser.back()
# time.sleep(2)
# browser.forward()
# time.sleep(3)
# browser.quit()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path
browser = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('fp/baidu.png')
