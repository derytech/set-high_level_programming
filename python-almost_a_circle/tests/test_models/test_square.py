#!/usr/bin/python3
"""
Unittest module for models/square.py.
"""
import os
import unittest
import pycodestyle
from models.square import Square


class TestSquareDocsAndStyle(unittest.TestCase):
    """Tests for Square documentation and PEP 8 style."""

    def test_pep8_conformance_square(self):
        """Test that models/square.py conforms to PEP 8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_conformance_test_square(self):
        """Test that test_square.py conforms to PEP 8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Test module docstring existence."""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """Test Square class docstring existence."""
        self.assertTrue(len(Square.__doc__) >= 1)


class TestSquareInstantiation(unittest.TestCase):
    """Tests for Square instantiation and validation."""

    def test_square_args(self):
        """Test Square instantiation with various arguments."""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.size, 5)

        s2 = Square(5, 2, 3, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 10)

    def test_type_and_value_errors(self):
        """Test type and value errors for Square."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)


class TestSquareMethods(unittest.TestCase):
    """Tests for Square methods: str, to_dictionary, update, create, save/load."""

    def test_str(self):
        """Test __str__ representation."""
        s = Square(5, 2, 1, 10)
        self.assertEqual(str(s), "[Square] (10) 2/1 - 5")

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1, 1)
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_update(self):
        """Test update method with args and kwargs."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_create(self):
        """Test Square.create method."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_save_and_load_file(self):
        """Test save_to_file and load_from_file for Square."""
        s = Square(5, 1, 2, 1)
        Square.save_to_file([s])
        output = Square.load_from_file()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].id, 1)
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
