# 用于实现将数据设置到剪切板中
# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import win32clipboard as wc
import win32con

class Simulate_Clipboard:
    # 读取剪切板
    @staticmethod
    def get_clipboard():
        # 打开剪切板
        wc.OpenClipboard()
        # 获取剪切板中的数据
        data = wc.GetClipboardData(win32con.CF_TEXT)
        # 关闭剪切板
        wc.CloseClipboard()
        # 返回剪切板数据给调用者
        return data

    # 设置剪切板内容
    @staticmethod
    def set_clipboard(content):
        # 打开剪切板
        wc.OpenClipboard()
        # 清空剪切板
        wc.EmptyClipboard()
        # 将数据astring写入剪切板
        wc.SetClipboardData(win32con.CF_UNICODETEXT, content)
        # 关闭剪切板
        wc.CloseClipboard()


if __name__ == '__main__':
    Simulate_Clipboard.set_clipboard("set content into clipboard")
    str = Simulate_Clipboard.get_clipboard()
    print(str)
