#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    i = 1
    l = len(sys.argv) - 1
    if (l == 0):
        print("{} arguments.".format(l))
    else:
        print("{} arguments:".format(l))
        while i <= l:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
