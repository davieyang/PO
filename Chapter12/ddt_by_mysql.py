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
from Util.ParseMysql import Parse_Mysql
from TestData import SQL_Script
# 定义日志存放路径
test_log_folder = ConstantConfig.parent_directory_path + "\\TestResult\\TestLog\\ddt_by_mysql.log"
# 初始化日志对象
logging.basicConfig(
level=logging.INFO,  # 日志级别
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',  # 打印日志的时间
    filename=test_log_folder,
    filemode='w'  # 打开日志的方式
    )


def get_test_data():
    db = Parse_Mysql(
        host="localhost",
        port=3306,
        dbName="automation",
        username="root",
        password="",
        charset="utf8mb4"
    )
    searchdata = SQL_Script.selectdata
    # 从数据库中获取测试数据
    testData = db.select_data_from_table("automation", searchdata)
    db.close_database()
    return testData

@ddt.ddt
class DataDrivenByMySQL(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(* get_test_data())
    def test_ddt_by_mysql(self, testData):
        # 对获得的数据进行解包
        dataid, testdata, expectdata =testData
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        print(testdata, expectdata)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error(u"查找的页面元素不存在，异常堆栈信息为：" + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info(u"搜索 ‘%s’,期望 ‘%s’ ,失败" % (testdata, expectdata))
        except Exception as e:
            logging.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
        else:
            logging.info(u"搜索 ‘%s’,期望 ‘%s’ ,通过" % (testdata, expectdata))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

