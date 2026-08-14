#!/usr/bin/python3
"""
Unittest module for models/rectangle.py.
"""
import io
import os
import sys
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleDocsAndStyle(unittest.TestCase):
    """Tests for Rectangle documentation and PEP 8 style."""

    def test_pep8_conformance_rectangle(self):
        """Test that models/rectangle.py conforms to PEP 8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_conformance_test_rectangle(self):
        """Test that test_rectangle.py conforms to PEP 8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Test module docstring existence."""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Test Rectangle class docstring existence."""
        self.assertTrue(len(Rectangle.__doc__) >= 1)


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for Rectangle instantiation and attributes."""

    def test_rectangle_args(self):
        """Test Rectangle instantiation with various arguments."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.x, 3)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)

        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

    def test_type_and_value_errors(self):
        """Test type errors and value errors for Rectangle attributes."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)


class TestRectangleMethods(unittest.TestCase):
    """Tests for Rectangle methods: area, display, __str__, update, etc."""

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        """Test display method stdout output."""
        capture = io.StringIO()
        sys.stdout = capture
        r = Rectangle(2, 2)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture.getvalue(), "##\n##\n")

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update(self):
        """Test update method positional and keyword args."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create(self):
        """Test Rectangle.create method."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_save_and_load_file(self):
        """Test save_to_file and load_from_file methods."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].id, 1)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
