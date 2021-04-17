# encoding = utf-8
from selenium import webdriver
import unittest
import time
import logging
import traceback
import ddt
from selenium.common.exceptions import NoSuchElementException
from Configuration import ConstantConfig


# 定义日志存放路径
test_log_folder = ConstantConfig.parent_directory_path + "\\TestResult\\TestLog\\ddt_by_xml.log"
# 初始化日志对象
logging.basicConfig(
level=logging.INFO,  # 日志级别
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',  # 打印日志的时间
    filename=test_log_folder,
    filemode='w'  # 打开日志的方式
    )
json_list_file = ConstantConfig.jsonlistdata
@ddt.ddt
class DataDrivenByJsonList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    @ddt.file_data(json_list_file)
    def test_data_driven_json_list(self, value):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        print(value)
        # 将从.json文件中读取出的数据用“||”分割成测试数据和期望的数据
        test_data, expect_data = tuple(value.strip().split("||"))
        # 设置隐式等待时间
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("kw").send_keys(test_data)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            # 断言期望结果是否出现在页面中
            self.assertTrue(expect_data in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error(u"查找的页面元素不存在，异常堆栈信息为：" + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info(u"搜索 '%s',期望 '%s' ,失败" % (test_data, expect_data))
        except Exception as e:
            logging.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
        else:
            logging.info(u"搜索 '%s',期望 '%s' ,通过" % (test_data, expect_data))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
