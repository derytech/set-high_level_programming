#!/usr/bin/python3
"""
This module contains a function that deserializes a JSON string into an object.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to decode.

    Returns:
        object: The Python data structure represented by my_str.
    """
    return json.loads(my_str)
