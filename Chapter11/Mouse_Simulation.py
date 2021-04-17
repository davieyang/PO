# encoding = utf-8
from selenium.webdriver.common.action_chains import ActionChains


class Simulate_Mouse:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    # 单击鼠标左键
    def left_click(self, element):
        self.actions.click(element).perform()

    # 双击鼠标左键
    def double_left_click(self, element):
        self.actions.double_click(element).perform()

    #  单击鼠标右键
    def right_click(self, element):
        self.actions.context_click(element).perform()

    #  移动鼠标到element
    def move_mouse(self, element):
        self.actions.move_to_element(element).perform()

    #  从source移动鼠标到target
    def move_mouse_source_target(self, source, target):
        self.actions.drag_and_drop(source, target).perform()

    #  从source移动鼠标到target
    def move_source_target(self, source, target):
        self.actions.click_and_hold(source).release(target).perform()

    #  拖拽元素到坐标xy
    def drag_element(self, element, x, y):
        self.actions.click_and_hold(element).move_by_offset(x, y).release().perform()

    #  点击并且不释放
    def click_hold(self, element):
        self.actions.click_and_hold(element)
