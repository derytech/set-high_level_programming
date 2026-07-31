#!/usr/bin/python3
"""
This module contains a function that writes an object to a file in JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized into JSON.
        filename (str): The name of the file to save the JSON to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
