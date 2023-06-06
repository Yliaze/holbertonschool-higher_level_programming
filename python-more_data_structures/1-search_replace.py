#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == []:
        return None

    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list

# List comprehension possibility:
# new_list = [replace if element == search else element for element in my_list]
# return new_list
