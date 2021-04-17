# coding:utf-8
import unittest


class NumbersTest(unittest.TestCase):

    def test_even(self):
        for i in range(0, 6):
            # with self.subTest(i=i):
            print("当前参数是：%d" % i)
            self.assertEqual(i % 2, 0)


if __name__ == '__main__':
    unittest.main()
