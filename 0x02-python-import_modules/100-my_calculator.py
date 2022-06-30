#!/usr/bin/python3
def selec(op, a, b):
    fun = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div,
            }
    res = fun[op](a, b)
    return(res)


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    leng = len(argv)
    if (leng != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    a, b = int(argv[1]), int(argv[3])
    if (op not in '+-*/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, selec(op, a, b)))
