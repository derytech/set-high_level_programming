#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()
        else:
            for index, number in enumerate(row):
                if index == len(row) - 1:
                    print("{:d}".format(number))
                else:
                    print("{:d}".format(number), end=" ")
