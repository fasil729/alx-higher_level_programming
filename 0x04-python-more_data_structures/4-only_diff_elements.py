#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    odd_set = []
    for element in set_1:
        if element not in set_2:
            odd_set.append(element)
        else:
            continue
    for element in set_2:
        if element not in set_1:
            odd_set.append(element)
        else:
            continue
    return odd_set
