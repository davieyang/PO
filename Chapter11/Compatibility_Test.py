# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest


class Compatibility_Test(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://admin.leadscloud.com/Front-breeze/#/home"

    def login_leadscloud(self, driver):
        '''
        定义测试方法
        :param driver: 
        :return: 
        '''
        driver.get(self.base_url)
        sleep(5)
        driver.find_element_by_xpath("//*[@id='main']/div/div[1]/div/div[2]/form/div[1]/div/div/input").send_keys('xxxxxx')
        driver.find_element_by_xpath("//*[@id='main']/div/div[1]/div/div[2]/form/div[2]/div/div/input").send_keys('xxxxxx')
        driver.find_element_by_xpath("//*[@id='main']/div/div[1]/div/div[2]/form/div[3]/div/button").click()
        driver.quit()

    def test_chrome(self):
        '''
        启动chrome浏览器执行测试用例
        :return: 
        '''
        chrome_driver = webdriver.Chrome()
        self.login_leadscloud(chrome_driver)

    def test_firefox(self):
        '''
        启动firefox执行测试用例
        :return: 
        '''
        firefox_driver = webdriver.Firefox()
        self.login_leadscloud(firefox_driver)

    def test_ie(self):
        '''
        启动IE执行测试用例
        :return: 
        '''
        ie_driver = webdriver.Ie()
        self.login_leadscloud(ie_driver)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)