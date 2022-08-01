#!/usr/bin/python3
"""a class the inherits from list"""


class MyList(list):
    def print_sorted(self):
        self.sort()
        print(self)
