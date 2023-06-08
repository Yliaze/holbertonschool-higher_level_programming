#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0

    sum_top = 0
    sum_bot = 0

    for pair in my_list:
        sum_top += (pair[0] * pair[1])
        sum_bot += pair[1]

    average = sum_top / sum_bot
    return average
