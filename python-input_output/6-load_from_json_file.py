#!/usr/bin/python3
"""
This module contains a function that loads an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python data structure created from the JSON file.
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
