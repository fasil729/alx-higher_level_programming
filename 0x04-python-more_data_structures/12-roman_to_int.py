#!/usr/bin/python3
def roman_to_int(roman_string):
    value = {"I": 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, "M": 1000}
    int_value = 0
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    i = 0
    while i < len(roman_string):
        try:
            if value[roman_string[i]] >= value[roman_string[i+1]]:
                int_value += int(value[roman_string[i]])
                i += 1
            else:
                int_value += value[roman_string[i+1]] - value[roman_string[i]]
                i += 2
        except IndexError:
            int_value += int(value[roman_string[i]])
            i += 1
    return int_value
