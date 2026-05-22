#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_case_2(self):
        self.assertEqual(max_integer([1, 3, 2, 4]),4)
    
    def test_case_3(self):
        self.assertEqual(max_integer([8, 3, 2, 5]),8)

    def test_case_4(self):
        self.assertEqual(max_integer([3]),3)

    def test_case_5(self):
        self.assertEqual(max_integer([1, -3, 2, 4]),4)

    def test_case_6(self):
        self.assertEqual(max_integer([-3]),-3)

if __name__ == "__main__":
    unittest.main()
