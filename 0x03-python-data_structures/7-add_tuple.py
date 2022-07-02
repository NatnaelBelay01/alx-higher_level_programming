#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t = tuple()
    i, ca, cb = 0, 0, 0
    for k in tuple_a:
        ca += 1
    for k in tuple_b:
        cb += 1
    if ca < 2:
        tuple_a += (0, 0)
    if cb < 2:
        tuple_b += (0, 0)
    for j in range(2):
        i = tuple_a[j] + tuple_b[j]
        t += (i,)
    return t
