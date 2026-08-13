#!/usr/bin/python3
"""
Unittest module for models/base.py.
Tests PEP 8 compliance, docstrings, instantiation, and JSON methods.
"""
import inspect
import json
import os
import unittest
import pycodestyle
from models.base import Base


class TestBaseDocsAndStyle(unittest.TestCase):
    """Tests Base documentation and PEP 8 style conformance."""

    def test_pep8_conformance_base(self):
        """Test that models/base.py conforms to PEP 8 / pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings) in models/base.py."
        )

    def test_pep8_conformance_test_base(self):
        """Test that test_base.py conforms to PEP 8 / pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors in tests/test_models/test_base.py."
        )

    def test_module_docstring(self):
        """Test module docstring existence."""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Test Base class docstring existence."""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Test existence of docstrings in all Base methods."""
        for name, func in inspect.getmembers(Base, inspect.isfunction):
            msg = f"Missing docstring in method {name}"
            self.assertTrue(len(func.__doc__) >= 1, msg)


class TestBaseInstantiation(unittest.TestCase):
    """Tests for Base class instantiation and ID generation."""

    def test_auto_id_increment(self):
        """Test automatic ID incrementation when id is None."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_explicit_id(self):
        """Test explicit ID assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_zero_id(self):
        """Test passing 0 as explicit ID."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_negative_id(self):
        """Test passing negative integer as explicit ID."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_string_id(self):
        """Test passing a string as explicit ID."""
        b = Base("custom_id")
        self.assertEqual(b.id, "custom_id")


class TestBaseJSONMethods(unittest.TestCase):
    """Tests for Base JSON serialization and deserialization."""

    def test_to_json_string_none(self):
        """Test to_json_string with None input."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list input."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string with a valid dictionary list."""
        d = [{'id': 1, 'width': 10, 'height': 4}]
        json_str = Base.to_json_string(d)
        self.assertIsInstance(json_str, str)
        self.assertEqual(json.loads(json_str), d)

    def test_from_json_string_none(self):
        """Test from_json_string with None input."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string input."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        output = Base.from_json_string(json_str)
        expected = [{"id": 89, "width": 10, "height": 4}]
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
