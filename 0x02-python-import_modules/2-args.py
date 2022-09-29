#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if args == 1:
        print(f'{args} argument:')
    else:
        if args == 0:
            print(f'{args} arguments.')
        else:
            print(f'{args} arguments:')
    for i in range(args):
        print(f"{i+1}: {argv[i+1]}")
