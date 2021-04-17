class JS_Assistance:

    def __init__(self, driver):
        self.driver = driver

    def single_click(self, element):
        try:
            #  判断页面元素状态
            if element.is_enabled() and element.is_displayed():
                #  调用js单击元素
                self.driver.execute_script("arguments[0].click();", element)
            else:
                print("该元素不可点击")
        except Exception as e:
            raise e

    def scroll_to_bottom(self):
        """
        滚动条滚动到页面底部
        :return:
        """
        self.driver.execute_script("document.documentElement.scrollTop=10000")

    def scroll_to_top(self):
        """
        滚动条滚动到页面顶部
        :return:
        """
        self.driver.execute_script("document.documentElement.scrollTop=0")

    def scrolltobottom(self):
        """
        滚动条滚动到页面底部
        :return:
        """
        self.driver.execute_script("window.scrollTo(0,100000)")

    def scrolltotop(self):
        """
        滚动条滚动到页面顶部
        :return:
        """
        self.driver.execute_script("window.scrollTo(0,1)")

    def vertical_to_middle(self):
        """
        纵向滚动条滚动到页面中部
        :return:
        """
        self.driver.execute_script("window.scrollBy(0, 0-document.body.scrollHeight *1/2)")

    def horizontal_to_middle(self):
        """
        滚动水平滚动条到页面中部
        :return:
        """
        self.driver.execute_script("window.scrollBy(0, 0-document.body.scrollWidht *1/2)")

    def scroll_to_element(self, element):
        """
        滚动到具体页面元素可见位置
        :param element:
        :return:
        """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_bottom_page(self):
        """
        滚动条滚动到页面底部
        :return:
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")