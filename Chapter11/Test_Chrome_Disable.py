# encoding = utf-8
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.chrome.options import Options


class Test_Disable_IMAGE(unittest.TestCase):

    def setUp(self):
        # 创建chrome的Options对象
        chrome_options = Options()
        # 设置chrome禁用配置
        diable_option = {"profile.managed_default_content_settings.images":2}
        #  添加屏蔽设置
        chrome_options.add_experimental_option("prefs", diable_option)
        # 启动浏览器
        self.chrome_driver = webdriver.Chrome(chrome_options = chrome_options)
        self.url = "http://www.sohu.com"

    def test_diable(self):
        self.chrome_driver.get(self.url)
        sleep(20)

    def tearDown(self):
        self.chrome_driver.quit()