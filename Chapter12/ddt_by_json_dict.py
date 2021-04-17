# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from ddt import ddt, file_data
import time
# 引入NoSuchElementException异常类
from selenium.common.exceptions import NoSuchElementException
from Configuration import ConstantConfig
#  定义测试数据文件
login_json = ConstantConfig.jsondictdata

@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://mail.163.com"
        self.driver.implicitly_wait(10)

    def user_login_163(self, username, password):
        driver = self.driver
        driver.get(self.url)
        # 定义frame，他是页面中的iframe控件
        frame = self.driver.find_element_by_xpath("//*[@id='loginDiv']/iframe")
        time.sleep(1)
        try:
            self.driver.switch_to.frame(frame)  # 切换进iframe控件
            self.driver.find_element_by_name("email").send_keys(username)  # 输入用户名
            self.driver.find_element_by_name("password").send_keys(password)  # 输入密码
            self.driver.find_element_by_id("dologin").click()  # 点击登陆按钮
        except NoSuchElementException as e:
            # 将未找到页面元素的异常记录进日志
            raise e
        except Exception as e:
            raise e

    @file_data(login_json)
    def test_login(self, username, password, assert_text):  # 定义测试方法
        self.user_login_163(username, password)  # 调用登陆163的方法
        message = self.driver.find_element_by_id("nerror").text
        self.assertEqual(message, assert_text)  # 断言

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
