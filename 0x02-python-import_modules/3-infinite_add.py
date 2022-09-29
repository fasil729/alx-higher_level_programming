#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if args == 0:
        print(0)
    else:
        sum = 0
        for i in range(args):
            sum += int(argv[i+1])
        print(sum)
