#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list where the max value is at the beginning."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_max_in_middle(self):
        """Test a list where the max value is in the middle."""
        max_in_middle = [1, 2, 5, 3, 4]
        self.assertEqual(max_integer(max_in_middle), 5)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floating-point numbers."""
        floats = [1.53, 6.33, -1.12, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of integers and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_negatives(self):
        """Test a list with all negative numbers."""
        negatives = [-1, -5, -10, -2]
        self.assertEqual(max_integer(negatives), -1)

    def test_string(self):
        """Test a single string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "the", "best"]
        self.assertEqual(max_integer(strings), "the")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_no_args(self):
        """Test passing no arguments to max_integer."""
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
