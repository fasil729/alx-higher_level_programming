#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print(f'{len(argv)} argument:')
    else:
        if len(argv) == 0:
            print(f'{len(argv)} arguments.')
        else:
            print(f'{len(argv)} arguments:')
    for i in range(len(argv)):
        print(f"{i+1}: {argv[i]}")
