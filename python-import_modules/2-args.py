#!/usr/bin/python3
import sys
if __name__ == "__main__":

    i = len(sys.argv) - 1
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
        print("1: {}".format(sys.argv[1]))
    else:
        i = 1
        print("{} arguments:".format(i))
        for arg in (sys.argv):
            if arg != 0:
                print("{}: {}".format(i, arg))
                i += 1
