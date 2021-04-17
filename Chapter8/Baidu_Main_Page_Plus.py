# -*- coding: utf-8 -*-
from Util import ParseElementLocator
import os
driver = None
# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentDirPath)
# 获取存放页面元素定位表达式文件的绝对路径
baidu_main_page_plus_file= parentDirPath + u"\\PageElementLocator\\baidu_main_page_plus.ini"
class Search_Page_Element():
    def __init__(self, driver):
        self.location_file = baidu_main_page_plus_file
        self.driver = driver
        self.get_element = ParseElementLocator.ParseConfigFile(self.driver, self.location_file)
    def input_search(self):
        input_search = self.get_element.get_element_location("main_baidu", "input_search", 5)
        self.get_element.highlight_element(self.driver, input_search)
        return input_search
    def button_search(self):
        button_search = self.get_element.get_element_location("main_baidu", "button_search", 5)
        self.get_element.highlight_element(self.driver, button_search)
        return button_search
    def input_search_string(self, string):
        baidu_main_page_plus = Search_Page_Element(self.driver)
        baidu_main_page_plus.input_search().send_keys(string)
    def click_search_button(self):
        baidu_main_page_plus = Search_Page_Element(self.driver)
        baidu_main_page_plus.button_search().click()
