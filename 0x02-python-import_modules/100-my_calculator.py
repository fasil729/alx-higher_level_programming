#!/usr/bin/python3
if __name__ == "__main__":
    from calculator import add, sub, mul, div
    import sys
    args = sys.argv
    a = int(args[1])
    b = int(args[3])
    op = args[2]
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if op == "+":
            print(f"{a} + {b} = {add(a, b)}") 
            sys.exit(0)
        elif op == "*":
            print(f"{a}*{b}={mul(a, b)}") 
            sys.exit(0)
        elif op == "-":
            print(f"{a} - {b} = {sub(a, b)}") 
            sys.exit(0)
        elif op == "/":
            print(f"{a} / {b} = {div(a, b)}") 
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
