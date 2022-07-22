#!/usr/bin/python3
"""Matrix division"""


def matrix_divided(matrix, div):
    """Divides every element of a matrix by a number
    Args:
        matrix(list): a list of lists of ints
        div(int/float): the divisor.
    """
    leng = -1
    new = []
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if leng != -1 and len(i) != leng:
            raise TypeError("Each row of the matrix must have the same size")
        leng = len(i)
        for j in i:
            if type(j) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        new.append(list(map(lambda x: x / div, matrix[i])))
    for i in range(len(new)):
        for j in range(len(new[i])):
            new[i][j] = round(new[i][j], 2)
    return new
