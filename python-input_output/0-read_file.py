#!/usr/bin/python3
"""
This module provides a utility to read and display file contents.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to standard output.

    Args:
        filename (str): The path to the text file. Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
