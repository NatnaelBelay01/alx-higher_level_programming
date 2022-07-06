#!/usr/bin/python3
def best_score(a_dictionary):
    best = None
    key = None
    if a_dictionary is None:
        return best
    for i in list(a_dictionary):
        if best is None:
            best = a_dictionary[i]
            key = i
        elif a_dictionary[i] > best:
            best = a_dictionary[i]
            key = i
    return key
