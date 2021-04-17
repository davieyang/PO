# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:23:25 2019

@author: davieyang
"""

from selenium import webdriver  # 引入webdriver
from time import sleep  # 从time模块引入sleep 
from time import ctime  # 从time模块引入ctime
import threading


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
    
    
threading_list = []  #创建一个空列表用于存储线程
# 定义一个执行start_chrome()方法的线程
chrome_thread = threading.Thread(target = start_chrome)  
threading_list.append(chrome_thread)  # 将线程放到列表中

# 定义一个执行start_firefox()方法的线程
firefox_thread = threading.Thread(target = start_firefox)  
threading_list.append(firefox_thread)  # 将线程放到列表中

# 定义一个执行start_chrome()方法的线程
ie_thread = threading.Thread(target = start_ie)  
threading_list.append(ie_thread)  # 将线程放到列表中



if __name__ == '__main__':
    for start_thread in threading_list:
        start_thread.start()
    for start_thread in threading_list:
        start_thread.join()
    print(u"全部结束 %s" %ctime())
            

