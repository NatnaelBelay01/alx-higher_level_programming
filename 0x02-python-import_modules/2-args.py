#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    i = 1
    ln = len(sys.argv) - 1
    if (ln == 0):
        print("{} arguments.".format(ln))
    else:
        if (ln == 1):
            print("{} argument:".format(ln))
        else:
            print("{} arguments:".format(ln))
        while i <= ln:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
