#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print(f'{len(argv)} arguments:')
    for i in range(len(argv)):
        print(f"{i+1}: {argv[i]}")
