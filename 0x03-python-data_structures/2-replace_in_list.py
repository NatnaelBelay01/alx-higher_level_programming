#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    if idx < 0:
        return my_list
    for j in my_list:
        i += 1
    if idx > i - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
