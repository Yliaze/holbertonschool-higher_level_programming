#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None

    big_one = my_list[0]

    for i in my_list:
        if i > big_one:
            big_one = i

    return (big_one)
