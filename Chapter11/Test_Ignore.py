# encoding = utf-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
from time import sleep

class Test_Disable_Ignore(unittest.TestCase):

    def setUp(self):
        # 创建Chrome的Options对象
        chrome_option = Options()
        # 为chrome_option添加配置
        chrome_option.add_argument("--disable-extensions")
        chrome_option.add_experimental_option("excludeSwitches", ["--ignore-certificate-errors"])
        chrome_option.add_argument("--start-maximized")
        self.chrome_driver = webdriver.Chrome(options=chrome_option)
        self.url = "http://www.baidu.com"

    def test_demo(self):
        self.chrome_driver.get(self.url)
        sleep(5)

    def tearDown(self):
        self.chrome_driver.quit()
