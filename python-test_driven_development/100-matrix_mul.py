#!/usr/bin/python3
"""
This module contains the `matrix_mul` function.

The function multiplies two matrices after validating their format.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices (lists of lists of integers or floats).

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        A new matrix containing the result of m_a * m_b.

    Raises:
        TypeError: If m_a or m_b are not lists, not lists of lists,
            contain non-int/float elements, or are not rectangular.
        ValueError: If m_a or m_b are empty, or cannot be multiplied.
    """
    # 1. Must be lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Must be list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Can't be empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Elements must be ints or floats
    for row in m_a:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    # 5. Must be rectangular
    len_a = len(m_a[0])
    if not all(len(row) == len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    len_b = len(m_b[0])
    if not all(len(row) == len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Multiplication compatibility check (cols of m_a == rows of m_b)
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication logic
    new_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            val = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(val)
        new_matrix.append(row)

    return new_matrix
