# -*- coding: utf-8 -*-
"""
用于解析配置文件，并获取页面元素定位表达式
"""
from configparser import ConfigParser  # 引入
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
class ParseConfigFile:
    """
    初始化解析文件类
    """
    def __init__(self, driver, page_element_locator):
        self.driver = driver
        self.cf = ConfigParser()
        self.cf.read(page_element_locator, encoding='utf-8')
    def get_items_section(self, section_name):
        """
        获取配置文件中指定section下的所有option_name键值对,并以字典类型返回给调用者
        注意：使用self.cf.items(sectionName)此种方法获取到
        配置文件中的options内容均被转换成小写，如loginPage.frame将被转换成loginpage.frame
        """
        options_dict = dict(self.cf.items(section_name))
        return options_dict
    def get_option_value(self, section_name, option_name):
        """
        获取指定section下的指定option的值
        """
        value = self.cf.get(section_name, option_name)
        return value
    def get_element_location(self, section_name, option_name, timeout):
        """
        获取页面元素定位表达式，并以元素对象的形式返回给调用者
        """
        driver = self.driver
        location = self.get_option_value(section_name, option_name)
        location_type = location.split(">")[0]
        location_value = location.split(">")[1]
        print("读取到的定位类型为：" + location_type + "\t读取到的定位信息为：" + location_value)
        try:
            element = WebDriverWait(driver, timeout)\
                .until(lambda x: x.find_element(by=location_type,value=location_value))
            return element
        except Exception as e:
            print("定位元素超过" + str(timeout) + "秒，详细异常信息入下：")
            raise e
    def highlight_element(self, driver, element):
        """
        调用JS，用于高亮控件
        :param driver:
        :param element:
        :return:
        """
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                              "background: yellow; border:2px solid red;")
