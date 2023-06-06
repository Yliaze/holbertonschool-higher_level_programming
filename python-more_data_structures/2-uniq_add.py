#!/usr/bin/python3
def uniq_add(my_list=[]):

    uniq_sum = 0
    uniq_set = set()

    for element in my_list:
        if element not in uniq_set:
            uniq_set.add(element)
            uniq_sum += element
    return uniq_sum

# List comprehension possibility:
# uniq_set = set()
# uniq_sum = sum([uniq_set.add(element) or element for element in my_list if
# element not in uniq_set])
# return uniq_sum
