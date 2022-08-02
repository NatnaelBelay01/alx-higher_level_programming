#!/usr/bin/python3
"""A functionn that creates pascals triangle"""


def pascal_triangle(n):
    lst = [[1], [1, 1]]

    if n < 0:
        return []
    if n <= 2:
        return lst[:n]
    for i in range(n - 2):
        temp = lst[-1]
        new = []
        x = 0
        new.append(temp[0])
        while x < len(temp) - 1:
            new.append(temp[x] + temp[x + 1])
            x += 1
        new.append(temp[-1])
        lst.append(new)
    return lst
