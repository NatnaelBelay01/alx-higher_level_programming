#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            count = 0
            for i in row:
                if count != 0:
                    print(" ", end="")
                count += 1
                print("{:d}".format(i), end="")
            print()
