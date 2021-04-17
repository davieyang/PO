# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 13:55
# @Author  : davieyang
# @File    : Test_Headless.py
# @Project: LeadsCloudAutoTest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# 创建chrome的Option对象
chrome_options = Options()
# 添加静默参数
chrome_options.add_argument('--headless')
for i in range(100000):
    # 静默模式启动浏览器
    chrome_driver = webdriver.Chrome(options=chrome_options)
    # 打开页面
    chrome_driver.get("http://www.yialife.co.za/contact.html")
    chrome_driver.maximize_window()
    chrome_driver.find_element_by_class_name("xhl-button-text").click()
    # 获取当前时间
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    chrome_driver.find_element_by_id("messageText").send_keys("audio notification testing at " + current_time)
    time.sleep(1)
    chrome_driver.find_element_by_id("sendBtn").click()
    print(current_time)
    time.sleep(5)
    # 删掉所有cookie
    chrome_driver.delete_all_cookies()
    chrome_driver.quit()
