#!/usr/bin/python3
def uniq_add(my_list=[]):
    dict = []
    sum = 0
    for num in my_list:
        if num in dict:
            continue
        else:
            sum += num
            dict.append(num)
    return sum
