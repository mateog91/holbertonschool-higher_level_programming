#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_values(self):
        self.assertEqual(max_integer([2, 4, 10]), 10)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-102, -84, -710]), -84)


class TestMaxInteger2(unittest.TestCase):
    def type_values(self):
        self.assertRaises(TypeError, max_integer, ["string", 10, 87])
