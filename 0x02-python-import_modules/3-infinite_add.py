#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ln, i, res = len(sys.argv) - 1, 1, 0
    while i <= ln:
        res += int(sys.argv[i])
        i += 1
    print(res)
