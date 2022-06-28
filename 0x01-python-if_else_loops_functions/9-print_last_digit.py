#!/usr/bin/python3
def print_last_digit(number):
    temp = number % 10 if number >= 0 else (-1 * number) % 10
    print(temp, end="")
    return temp
