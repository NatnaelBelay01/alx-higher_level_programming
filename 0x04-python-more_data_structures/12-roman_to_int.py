#!/usr/bin/python3
def roman_to_int(roman_string):
    num, i = 0, 0
    if not roman_string or type(roman_string) != str:
        return 0
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for j in roman_string:
        if val.get(j, 0) == 0:
            return 0
    while i < len(roman_string):
        if num == 0:
            num = val[roman_string[i]]
            i += 1
            continue
        elif i <= 2 and val[roman_string[i]] == val[roman_string[i - 1]]:
            if val[roman_string[i]] and val[roman_string[i - 2]] in (10, 100, 1000):
                num *= val[roman_string[i]]
            else:
                num += val[roman_string[i]]
            i += 1
            continue
        elif val[roman_string[i]] > val[roman_string[i - 1]]:
            num = val[roman_string[i]] - num
            i += 1
            continue
        elif val[roman_string[i]] <= val[roman_string[i - 1]]:
            num += val[roman_string[i]]
            i += 1
            continue
    return num
