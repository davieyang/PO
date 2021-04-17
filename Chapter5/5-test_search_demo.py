# encoding = utf-8
from selenium import webdriver
import unittest
import time


class Search_KeyWords(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = "http://www.baidu.com"

    def test_search_davieyang(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("davieyang")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        try:
            self.assertTrue("davieyang" in driver.page_source)
        except AssertionError as e:
            raise e
    def test_search_selenium(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        try:
            self.assertTrue("davieyang" in driver.page_source)
        except AssertionError as e:
            raise e
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Search_KeyWords('test_search_davieyang'))
    suite.addTest(Search_KeyWords('test_search_selenium'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
