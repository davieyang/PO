# coding : utf-8
import unittest
import random
import sys
class TestSequenceFunctions(unittest.TestCase):
    a = 1
    b = 2
    def setUp(self):
        self.seq = list(range(10))
        self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]
    @unittest.skip("就跳过了不为什么")
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))
    @unittest.skipIf(a != 1, "如果a不等于1就跳过此测试方法")
    def test_choic(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)
    @unittest.skipUnless(b > 1, "除非b大于1，否则跳过")
    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
    @unittest.expectedFailure
    def test_randomshuffle(self):
        random.shuffle(self.list)
        print(self.list)
        self.assertEqual(self.list, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13])
if __name__ == '__main__':
    unittest.main(verbosity=2)
