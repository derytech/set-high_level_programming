#!/usr/bin/python3
"""
This module contains a function that appends text to a UTF-8 file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The string content to append. Defaults to "".

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
