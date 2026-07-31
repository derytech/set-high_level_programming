#!/usr/bin/python3
"""
This module contains a function that inserts a line of text to a file
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing
    a specific search string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after matching lines.
    """
    text = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
