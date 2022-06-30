#!/usr/bin/python3
if __name__ == '__main__':
    from hidden_4 import *
    ls = dir()
    for i in ls:
        if i[0:2] != "__":
            print(i)
