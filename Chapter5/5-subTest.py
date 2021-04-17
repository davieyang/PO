# coding:utf-8
import unittest
class NumbersTest(unittest.TestCase):
    def test_even(self):
        """
        使用subTest上下文管理器，区分细小的变化
        取模运算，返回除法的余数，但是参数是0到5的整数，没必要单独写方法
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
if __name__ == '__main__':
    unittest.main()
