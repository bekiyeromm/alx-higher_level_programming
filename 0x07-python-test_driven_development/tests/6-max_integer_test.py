#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def max_empty(self):
        self.assertEqual([], None)
    def max_posetive(self):
        self.assertEqual([10, 30, 3, 60, 15], 60)
    def max_negative(self):
        slef.assertEqual(max_integer([-1, -5, -6, -10, -3]), -1)
    def neg_pos_max(self):
        slef.assertEqual(max_integer([1, -50, -60, 10, 3]), 10)
if __name__ == "__main__":
    unittest.main()
