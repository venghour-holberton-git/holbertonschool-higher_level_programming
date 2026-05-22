#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

if __name__ == "__main__":
    unittest.main()
