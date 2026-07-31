#!/usr/bin/python3
"""
This module contains a function that writes text data to a UTF-8 file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file in UTF-8 encoding and returns character count.

    Args:
        filename (str): The path or name of the target file. Defaults to "".
        text (str): The string content to write into the file. Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
