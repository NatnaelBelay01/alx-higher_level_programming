#!/usr/bin/python3
def roman_to_int(roman_string):
    num, i = 0, 0
    let = roman_string
    if not let or type(let) != str:
        return 0
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for j in let:
        if val.get(j, 0) == 0:
            return 0
    while i < len(let):
        if num == 0:
            num = val[let[i]]
            i += 1
            continue
        elif i <= 2 and val[let[i]] == val[let[i - 1]]:
            if val[let[i]] and val[let[i - 2]] in (10, 100, 1000):
                num *= val[let[i]]
            else:
                num += val[let[i]]
            i += 1
            continue
        elif val[let[i]] > val[let[i - 1]]:
            num = val[let[i]] - num
            i += 1
            continue
        elif val[let[i]] <= val[let[i - 1]]:
            num += val[let[i]]
            i += 1
            continue
    return num
