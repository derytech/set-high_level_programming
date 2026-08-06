#!/usr/bin/python3
"""
This module contain the 'add_integer' function
The function add two numbers (integers or floats)together 
after casting floats or integers
"""

def add_integer(a, b = 98):
    """ add two integers,

    args:
        a: First integer or float.
        b: Second integer or float (default is 98).
    
    Return:
         The sum of a and b as integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return in(a) + int(b)
