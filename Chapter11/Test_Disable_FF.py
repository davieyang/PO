# encoding = utf-8
from selenium import webdriver
from time import sleep
import unittest


class Test_Disable_IMAGE(unittest.TestCase):

    def setUp(self):
        # 创建Firefox的Options对象
        firefox_profile = webdriver.FirefoxProfile()
        # 禁止加载CSS
        firefox_profile.set_preference("permissions.default.stylesheet", 2)
        # 禁止加载Image
        firefox_profile.set_preference("permissions.default.image", 2)
        # 禁止加载Flash
        firefox_profile.set_preference("dom.ipc.plugins.enables.libflashplayer.so", False)
        # 启动浏览器
        self.firefox_driver = webdriver.Firefox(firefox_profile = firefox_profile)
        self.url = "http://www.sohu.com"

    def test_diable(self):
        self.firefox_driver.get(self.url)
        sleep(20)

    def tearDown(self):
        self.firefox_driver.quit()