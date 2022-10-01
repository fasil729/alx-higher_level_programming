#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    tot_wieght = 0
    total_sum = 0
    for (i, j) in my_list:
        total_sum += i*j
        tot_wieght += j
    return total_sum/tot_wieght
