# encoding = utf -8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
from time import sleep

class Test_Disable_PDF_FLASH(unittest.TestCase):
    def setUp(self):
        desire_caps = DesiredCapabilities.INTERNETEXPLORER
        #  配置禁用IE保护模式
        desire_caps["ignoreProtectedModeSettings"] = True
        #  启动带有我们设置的浏览器
        self.ie_driver = webdriver.Ie(capabilities=desire_caps)
        self.url = "http://www.sohu.com"

    def test_demo(self):
        self.ie_driver.get(self.url)
        sleep(20)


    def tearDown(self):
        self.ie_driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)