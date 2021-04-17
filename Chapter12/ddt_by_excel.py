# encoding = utf-8
from selenium import webdriver
import unittest
import time
import traceback
import ddt
import logging
from Util.ParseExcel import ParseExcel
from selenium.common.exceptions import NoSuchElementException
from Configuration import ConstantConfig


# 定义日志存放路径
test_log_folder = ConstantConfig.parent_directory_path + "\\TestResult\\TestLog\\ddt_by_list.log"
# 初始化日志对象
logging.basicConfig(
    level=logging.INFO,  # 日志级别
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',  # 打印日志的时间
    filename=test_log_folder,
    filemode='w'  # 打开日志的方式
    )


excelPath = ConstantConfig.exceldata  # 定义Excel文件
sheetName = u"Sheet1"
excel = ParseExcel(excelPath, sheetName)  # 实例化解析Excel类


@ddt.ddt
class TestDataDrivenByExcel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(* excel.getDatasFromSheet())
    def test_dataDrivenByExcel(self, data):
        test_data, expect_data = tuple(data)
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        try:
            self.driver.find_element_by_id("kw").send_keys(test_data)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)  # 强制等待3秒
            self.assertTrue(expect_data in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error(u"查找的页面元素不存在，异常堆栈信息为：" + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info(u"搜索 ‘%s’,期望 ‘%s’ ,失败" % (test_data, expect_data))
        except Exception as e:
            logging.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
        else:
            logging.info(u"搜索 ‘%s’,期望 ‘%s’ ,通过" % (test_data, expect_data))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
