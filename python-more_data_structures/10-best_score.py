#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    big_key = None
    big_value = 0

    for key, value in a_dictionary.items():
        if value > big_value:
            big_key = key
            big_value = value

    return big_key
