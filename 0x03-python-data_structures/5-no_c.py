#!/usr/bin/python3
def no_c(my_string):
    m = str()
    for i in my_string:
        if i != 'c' and i != 'C':
            m = m + i
    return m  
