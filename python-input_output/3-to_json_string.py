#!/usr/bin/python3
"""
This module contains a function that serializes an object to JSON format.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to be converted into a JSON string.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
