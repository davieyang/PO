# encoding = utf-8
from selenium.webdriver.common.by import By
from time import sleep
class Page(object):
    """
    基础类，用于页面对象类的继承
    """
    login_url = 'http://www.baidu.com'
    # 初始化类函数，定义属性base.url/driver/timeout
    def __init__(self, driver, base_url=login_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
    # 定义目标页面
    def target_page(self):
        return self.driver.current_url == self.base_url
# 定义打开页面的函数
    def open(self):
        url = self.base_url
        self.driver.get(url)
        print(self.driver.current_url)
    # 定义获取元素基础方法
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

class SearchPage(Page):
    """
    Baidu首页，页面对象类
    """
    url = '/'
    input_loc = (By.NAME, "wd")  # 页面控件对象：input控件
    search_button_loc = (By.ID, "su")  # 页面控件对象：百度一下按钮
    """
    为每个页面元素对象封装其相对应的方法
    """
    def input_search_string(self, search_string):
        self.find_element(*self.input_loc).send_keys(search_string)  #  输入要检索的字符串
    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()  # 点击百度一下按钮
# 定义检索字符串函数
def search_string(driver, string):
    search_Page = SearchPage(driver)
    search_Page.open()
    search_Page.input_search_string(string)
    sleep(3)
    search_Page.click_search_button()
