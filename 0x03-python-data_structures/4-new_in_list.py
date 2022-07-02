#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = list()
    j = 0
    for i in my_list:
        new.append(i)
        j += 1
    if idx < 0 or idx > j - 1:
        return new
    else:
        new[idx] = element
        return new
