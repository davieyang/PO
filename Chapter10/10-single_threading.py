# -*- coding: utf-8 -*-
from selenium import webdriver  # 引入webdriver
from time import sleep  # 从time模块引入sleep 
from time import ctime  # 从time模块引入ctime

def start_chrome():  # 定义启动谷歌浏览器的方法
    print("starting chrome browser now! %s" % ctime())  # 控制台打印当前时间 
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("http://www.baidu.com") #打开百度主页
    sleep(2)
    chrome_driver.quit()

def start_firefox():  # 定义启动火狐浏览器的方法
    print("starting firefox browser now! %s" % ctime())  # 控制台打印当前时间
    fire_driver = webdriver.Firefox()
    fire_driver.get("http://www.baidu.com") #打开百度主页
    sleep(3)
    fire_driver.quit()

def start_ie():  # 定义启动IE浏览器的方法
    print("starting ie browser now! %s" %ctime())  # 控制台打印当前时间
    ie_driver = webdriver.Ie()
    ie_driver.get("http://www.baidu.com")  #打开百度主页
    sleep(5)
    ie_driver.quit()

if __name__ == '__main__':
    start_chrome()
    start_firefox()
    start_ie()
    print(u"全部结束 %s" %ctime())
            

