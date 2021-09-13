#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        first = True
        for element in row:
            if first is False:
                print(" ", end="")
            print("{:d}".format(element), end="")
            first = False
        print()
