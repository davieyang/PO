# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from time import ctime
import threading

def start_browser(browser, time):
    if browser == "chrome":
        print("starting chrome browser now! %s" % ctime())  # 控制台打印当前时间 
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("http://www.baidu.com") #打开百度主页
        sleep(time)
        chrome_driver.quit()
    elif browser == "firefox":
        print("starting firefox browser now! %s" % ctime())  # 控制台打印当前时间
        fire_driver = webdriver.Firefox()
        fire_driver.get("http://www.baidu.com") #打开百度主页
        sleep(time)
        fire_driver.quit()
    else: 
        print("starting ie browser now! %s" %ctime())  # 控制台打印当前时间
        ie_driver = webdriver.Ie()
        ie_driver.get("http://www.baidu.com")  #打开百度主页
        sleep(time)
        ie_driver.quit()
browser_dict = {"chrome":3,"firefox":4,"ie":5}
start_browser_threading = []
for browser, time in browser_dict.items():
    threading_browser = threading.Thread(target = start_browser, args = (browser, time))
    start_browser_threading.append(threading_browser)

if __name__ == '__main__':
    for threading_browser in range(len(browser_dict)):
        start_browser_threading[threading_browser].start()
    for threading_browser in range(len(browser_dict)):
        start_browser_threading[threading_browser].join()
    print(u"全部结束 %s" %ctime())
