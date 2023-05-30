#!/usr/bin/python3
def uppercase(str):
    for i in str:
        convert = ord(i)
        if ord(i) in range(97, 123):
            convert = convert - 32
        print("{}".format(chr(convert)), end="")
    print()
