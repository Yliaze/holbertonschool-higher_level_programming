#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    roman_d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for i in range(len(roman_string)):
        if roman_string[i] not in roman_d:
            return 0

        result += roman_d[roman_string[i]]

        if i > 0 and roman_d[roman_string[i - 1]] < roman_d[roman_string[i]]:
            result -= (roman_d[roman_string[i - 1]] * 2)

    return result
