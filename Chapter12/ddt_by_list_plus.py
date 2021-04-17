# encoding = utf-8
from Configuration import ConstantConfig
from selenium import webdriver  # 从selenium模块引入webdriver类
import unittest  # 引入unittest模块
import time  # 引入time模块
import logging  # 引入日志模块
import traceback  # 引入traceback
import ddt  # 引入ddt
# 引入NoSuchElementException异常类
from selenium.common.exceptions import NoSuchElementException

# 定义日志存放路径
test_log_folder = ConstantConfig.parent_directory_path + "\\TestResult\\TestLog\\ddt_by_list_plus.log"
# 初始化日志对象
logging.basicConfig(
    level=logging.INFO,  # 日志级别
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',  # 打印日志的时间
    filename=test_log_folder,
    filemode='w'  # 打开日志的方式
    )


@ddt.ddt
class DataDrivenDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # 定义浏览器驱动

    @ddt.data([u"阿里巴巴", u"腾讯"], [u"美团外卖", u"百度"], [u"饿了么", u"蚂蚁金服"])
    @ddt.unpack
    def test_dataDrivenByDDT(self, testdata, expectdata):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error(u"查找的页面元素不存在，异常堆栈信息:" + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info(u"搜索 '%s',期望 '%s' ,失败" % (testdata, expectdata))
        except Exception as e:
            logging.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
        else:
            logging.info(u"搜索 '%s',期望 '%s' ,通过" % (testdata, expectdata))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
