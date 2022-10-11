#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    leng = 0
    for elm in range(x):
        try:
            print(my_list[elm], end="")
            leng += 1
        except IndexError:
            pass
    print("")
    return leng
