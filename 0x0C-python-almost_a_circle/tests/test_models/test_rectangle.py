#!/usr/bin/python3
"""Module for Tests for Class Rectangle
"""
import unittest
import io
import os
import unittest.mock
import pycodestyle
from models.rectangle import Rectangle
from models.base import Base


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

    def test_to_dictionary(self):
        """Test to dictionary"""
        r1 = Rectangle(10, 2, 1, 9, 99)
        r1_dictionary = r1.to_dictionary()
        exp_dict = {'x': 1, 'y': 9, 'id': 99, 'height': 2, 'width': 10}
        self.assertIsInstance(r1_dictionary, dict)
        self.assertEqual(r1_dictionary, exp_dict)

    def test_dictionary_to_JSON(self):
        """Test dictionary to Json string"""
        # Test conversion string
        r1 = Rectangle(10, 7, 2, 8, 99)
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
#---------------------------------------------------------------------------------------#

    def test_to_file(self):
        "Test to file"
        json_string = '[{"id": 1, "width": 5, "height": 4, "x": 2, "y": 2}]'
        rect_expected = Rectangle(5, 4, 2, 2, 1)
        Rectangle.save_to_file([rect_expected])
        filename = "Rectangle.json"
        path = os.getcwd()
        self.assertTrue(os.path.isfile(path + "/" + filename))
        with open("Rectangle.json", "r") as file:
            output = file.read()
        self.assertEqual(output, json_string)
        self.assertEqual(file.name, filename)
        self.assertIsInstance(rect_expected, Rectangle)
        self.assertIsInstance(output, str)
        os.remove(path + "/" + filename)

    # def test_from_json_string(self):
    #     """Test from json string"""
    #     self.assertEqual(Rectangle.from_json_string(None), [])
    #     self.assertIsNotNone(Rectangle.from_json_string(None))
#-------------------------------------------------------------------------------------------#

    def test_create(self):
        """Test return of an instance with all attributes already set"""
        r10 = Rectangle(3, 5, 1, 2, 10)
        r10_dictionary = r10.to_dictionary()
        r11 = Rectangle.create(**r10_dictionary)
        output = "[Rectangle] (10) 1/2 - 3/5\n[Rectangle] (10) 1/2 - 3/5\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            print(r10)
            print(r11)
            self.assertEqual(_out.getvalue(), output)
        self.assertIsNot(r10, r11)
        self.assertNotEqual(r10, r11)

    def test_load_from_file(self):
        """Test return of a list of instances"""
        r12 = Rectangle(10, 7, 2, 8, 1)
        r13 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [r12, r13]
        output = "[Rectangle] (1) 2/8 - 10/7\n[Rectangle] (2) 0/0 - 2/4\n"
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            for rect in list_rectangles_output:
                print("{}".format(rect))
            self.assertEqual(_out.getvalue(), output)
        path = os.getcwd()
        os.remove(path + "/" + "Rectangle.json")

    def test_load_from_file_FileNotFoundError(self):
        """Test return of an empty list and FileNotFoundError"""
        self.assertEqual(Rectangle.load_from_file(), [])
