#!/usr/bin/python3
"""Module for Tests for Class Square
"""
import unittest
import io
import unittest.mock
import pycodestyle
from models.square import Square
from models.base import Base


class Test_Rectangle(unittest.TestCase):
    """Test Cases for class Base
    """

    def test_initialization(self):
        """Test is in fact an instance"""
        r1 = Square(2)
        # Instance
        self.assertIsInstance(r1, Square)
        # Mandatory Arguments
        self.assertEqual(r1.size, 2)

        # Optional Arguments set
        r2 = Square(4, 1, 5, 23)
        self.assertEqual(r2.size, 4)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 5)
        self.assertEqual(r2.id, 23)

    def test_attributes_types(self):
        """Test Validation Attributes types with correct error messages"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect0 = Square(1)
            rect0.size = '5'

    def test_attributes_value(self):
        """Test Validation Attributes value with correct error messages"""
        rect1 = Square(1, 1)  # Square for re assignment tests

        # Testing width and height
        # Testing at limit 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

        # Testing at negative numbers
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)

        # Test by re assignment
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect1.size = -9

        # Testing x and y by re assignment
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect1.x = -5
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect1.y = -7

    def test_area(self):
        """Test Instance Method Area"""
        r4 = Square(8)
        self.assertEqual(r4.area(), (8 * 8))

    def test_display(self):
        """Test Instance Method Display"""
        # Test Is not None
        r = Square(4)
        self.assertIsNotNone(r.display)

        # Test print width and heigth
        output = "####\n####\n####\n####\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            r4 = Square(4)
            r4.display()
            self.assertEqual(_out.getvalue(), output)

        # Test print width, height, x and y
        output = "\n\n\n\n  ####\n  ####\n  ####\n  ####\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            r4 = Square(4, 2, 4)
            r4.display()
            self.assertEqual(_out.getvalue(), output)

    def _test_str_redefinition(self):
        """Test __str__ re definition"""
        output = "[Square] (12) 2/7 - 5\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            r1 = Square(5, 7, 12)
            print(r1)
            self.assertEqual(_out.getvalue(), output)

    def test_update_args(self):
        "Test Update through args"
        r = Square(1, 3, 4, 5)
        r.update(7, 9, 10, 11)
        self.assertEqual(r.size, 9)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 11)
        self.assertEqual(r.id, 7)

    def test_update_kwargs(self):
        "Test Update through kwargs"
        r = Square(1, 3, 4, 5)
        new_values = {"id": 4, "size": 7, "y": 15}
        r.update(**new_values)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.size, 7)
        self.assertEqual(r.y, 15)

    def test_to_dictionary(self):
        """Test to dictionary"""
        r1 = Square(10, 1, 9, 99)
        r1_dictionary = r1.to_dictionary()
        exp_dict = {'x': 1, 'y': 9, 'id': 99, 'size': 10}
        self.assertIsInstance(r1_dictionary, dict)
        self.assertEqual(r1_dictionary, exp_dict)

    def test_dictionary_to_JSON(self):
        """Test dictionary to Json string"""
        # Test conversion string
        r1 = Square(10, 2, 8, 99)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

        # test edge cases
        self.assertIsInstance(Base.to_json_string([]), str)
        self.assertEqual(Base.to_json_string(None), '[]')
    # def test_JSON_str_to_file

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
