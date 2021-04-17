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


@ddt.ddt
class DataDrivenDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # 定义浏览器驱动

    #  使用ddt准备三组测试数据，每组都存放在列表中，且每组数据中的数据与测试方法中定义的形参股份数及顺序一一对应
    @ddt.data(["159@163.com", "abcabc"], ["158@163.com", "abcabc"], ["157@163.com", "abcabc"])
    @ddt.unpack  # 对测试数据进行解包
    def test_dataDrivenByDDT(self, username, password):
        url = "http://mail.163.com"
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        frame = self.driver.find_element_by_xpath("//*[@id='loginDiv']/iframe")  # 定义frame，他是页面中的iframe控件
        try:
            self.driver.switch_to.frame(frame)  # 切换进iframe控件
            self.driver.find_element_by_name("email").send_keys(username)  # 输入用户名
            self.driver.find_element_by_name("password").send_keys(password)  # 输入密码
            self.driver.find_element_by_id("dologin").click()  # 点击登陆按钮
            time.sleep(3)  # 等待3秒
            self.assertTrue(u"收信" in self.driver.page_source)  # 断言关键字“收信”
        except NoSuchElementException as e:
            # 将未找到页面元素的异常记录进日志
            logging.error(u"查找的页面元素不存在，异常堆栈信息:" + str(traceback.format_exc()))
        except AssertionError as e:
            #  将登陆失败或断言失败记录进日志
            logging.info(u"邮箱 '%s', 登陆失败" % username)
        except Exception as e:
            #  将未知错误记录进日志
            logging.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
        else:
            #  将登陆成功且断言成功记录进日志
            logging.info(u"邮箱 '%s', 登陆成功" % username)

    def tearDown(self):
        self.driver.quit()  # 关闭浏览器


if __name__ == '__main__':
    unittest.main()

