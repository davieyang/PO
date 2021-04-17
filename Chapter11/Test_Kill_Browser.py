# encoding = utf-8
from selenium import webdriver
import unittest
import os
from time import sleep
class Test_Kill_Browser(unittest.TestCase):

    def test_kill_browser_process(self):
        # 启动浏览器
        chrome_driver = webdriver.Chrome()
        sleep(5)
        firefox_driver = webdriver.Firefox()
        sleep(5)
        ie_driver = webdriver.Ie()
        sleep(5)
        # 杀chrome浏览器进程
        code = os.system("taskkill /F /iM chrome.exe")
        if code ==0:
            print(u"Kill Firefox Successfully")
        else:
            print(u"Kill Firefox Failed")
        # 杀firefox浏览器进程
        code = os.system("taskkill /F /iM firefox.exe")
        if code ==0:
            print(u"Kill Firefox Successfully")
        else:
            print(u"Kill Firefox Failed")
        # 杀ie浏览器进程
        code = os.system("taskkill /F /iM ie.exe")
        if code ==0:
            print(u"Kill Firefox Successfully")
        else:
            print(u"Kill Firefox Failed")

if __name__ == '__main__':
    unittest.main(verbosity=2)

