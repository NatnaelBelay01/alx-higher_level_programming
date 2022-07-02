#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        i = my_list[0]
        for k in my_list:
            if k > i:
                i = k
        return i
    return None
