#!/usr/bin/python3
"""Module for Tests for Class Rectangle
"""
import unittest
import io
import unittest.mock
import pycodestyle
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Test Cases for class Base
    """

    def test_initialization(self):
        """Test is in fact an instance"""
        r1 = Rectangle(2, 3)
        # Instance
        self.assertIsInstance(r1, Rectangle)
        # Mandatory Arguments
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        # Automatic inputs
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        # Optional Arguments set
        r2 = Rectangle(4, 1, 7, 5, 23)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 1)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 5)
        self.assertEqual(r2.id, 23)

    def test_attributes_types(self):
        """Test Validation Attributes types with correct error messages"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", "1")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, [3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 3, 4j)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 3, 5.333)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect0 = Rectangle(1, 1)
            rect0.height = '5'

    def test_attributes_value(self):
        """Test Validation Attributes value with correct error messages"""
        rect1 = Rectangle(1, 1)  # Rectangle for re assignment tests

        # Testing width and height
        # Testing at limit 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        # Testing at negative numbers
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

        # Test by re assignment
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect1.width = -9

        # Testing x and y by re assignment
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect1.x = -5
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect1.y = -7

    def test_area(self):
        """Test Instance Method Area"""
        r4 = Rectangle(8, 9)
        self.assertEqual(r4.area(), (8 * 9))

    def test_display(self):
        """Test Instance Method Display"""
        # Test Is not None
        r = Rectangle(4, 5)
        self.assertIsNotNone(r.display)

        # Test print width and heigth
        output = "#####\n#####\n#####\n#####\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            r4 = Rectangle(5, 4)
            r4.display()
            self.assertEqual(_out.getvalue(), output)

        # Test print width, height, x and y
        output = "\n\n\n\n  #####\n  #####\n  #####\n  #####\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            r4 = Rectangle(5, 4, 2, 4)
            r4.display()
            self.assertEqual(_out.getvalue(), output)

    def _test_str_redefinition(self):
        """Test __str__ re definition"""
        output = "[Rectangle] (12) 2/7 - 5/6\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            r1 = Rectangle(5, 6, 7, 12)
            print(r1)
            self.assertEqual(_out.getvalue(), output)

    def test_update_args(self):
        "Test Update through args"
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(7, 8, 9, 10, 11)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 11)
        self.assertEqual(r.id, 7)

    def test_update_kwargs(self):
        "Test Update through kwargs"
        r = Rectangle(1, 2, 3, 4, 5)
        new_values = {"id": 4, "width": 7, "y": 15}
        r.update(**new_values)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.y, 15)
