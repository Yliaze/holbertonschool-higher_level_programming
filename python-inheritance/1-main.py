#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

"""main with tests for 1-my_list"""
my_list = MyList()
print(my_list)
my_list.append(1)
my_list.append(4)
my_list.append(2)
print(my_list)
my_list.print_sorted()

my_list.append(2.3)
my_list.append(1.3)
my_list.print_sorted()

my_list = MyList("string")
print(my_list)
my_list.print_sorted()

my_list = MyList([3, 6, 2])
print(my_list)
my_list.print_sorted()

new_list = MyList()
new_list.print_sorted()

my_list = MyList(None)
print(my_list)
