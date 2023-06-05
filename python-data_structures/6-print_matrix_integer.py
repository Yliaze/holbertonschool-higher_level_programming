#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for line in range(len(matrix)):
            for element in matrix[line]:
                print("{:d}".format(element), end="")
            print()
