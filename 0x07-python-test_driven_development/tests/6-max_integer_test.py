#!/usr/bin/python3
"""A unittest for the function max_integer"""
import unittest


maxx = __import__('6-max_integer').max_integer
class Test_max_integer(unittest.TestCase):
    def test_value(self):
        self.assertEqual(maxx([1, 2, 3]), 3)
        self.assertEqual(maxx([-1, -2, -3]), -1)
        self.assertEqual(maxx([100, 382, 233]), 382)
        self.assertEqual(maxx([1, -312, -323]), 1)
    def test_error(self):
        self.assertRaises(TypeError, maxx, -1)
        self.assertRaises(TypeError, maxx, 100)
        self.assertRaises(TypeError, maxx, 2j)
        self.assertRaises(TypeError, maxx, [1, "hello"])
        self.assertRaises(TypeError, maxx, [1, "2j"])

