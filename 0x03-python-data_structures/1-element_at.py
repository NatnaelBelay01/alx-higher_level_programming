#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0:
        return None
    for j in my_list:
        i += 1
    if idx > i - 1:
        return None
    else:
        return my_list[idx]
