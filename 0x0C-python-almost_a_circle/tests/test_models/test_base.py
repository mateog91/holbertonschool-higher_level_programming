#!/usr/bin/python3
"""Module for Tests for Class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Cases for class Base
    """

    def test_instance(self):
        """Tests is in fact an instance"""
        b_instance = Base()
        self.assertIsInstance(b_instance, Base)

    def test_correct_initialization_id(self):
        """Tests correct initialization of id"""
        # intitializing if id as None and see automatic handling
        inst1 = Base()
        inst2 = Base()
        inst3 = Base(15)
        inst4 = Base()

        self.assertEqual(inst1.id, 1)
        self.assertEqual(inst2.id, 2)
        self.assertEqual(inst3.id, 15)
        self.assertEqual(inst4.id, 3)

        inst5 = Base(-20)
        self.assertEqual(inst5.id, -20)


if __name__ == "__main__":
    unittest.main()
