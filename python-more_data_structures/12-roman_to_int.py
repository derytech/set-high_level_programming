#!/usr/bin/python3

def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i in range(len(roman_string)):
        value = roman_values[roman_string[i]]

        if i + 1 < len(roman_string):
            next_value = roman_values[roman_string[i + 1]]

            if value < next_value:
                total -= value
            else:
                total += value
        else:
            total += value

    return total
