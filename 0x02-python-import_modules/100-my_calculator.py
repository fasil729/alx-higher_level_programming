#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(args[1])
        b = int(args[3])
        op = args[2]
        if op == "+":
            print("{} {} {} = {}".format(a, args[2], b, add(a, b)))
            sys.exit(0)
        elif op == "*":
            print("{} {} {} = {}".format(a, args[2], b, mul(a, b)))
            sys.exit(0)
        elif op == "-":
            print("{} {} {} = {}".format(a, args[2], b, sub(a, b)))
            sys.exit(0)
        elif op == "/":
            print("{} {} {} = {}".format(a, args[2], b, div(a, b)))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
