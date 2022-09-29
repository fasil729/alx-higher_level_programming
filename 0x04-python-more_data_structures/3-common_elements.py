#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = []
    for element in set_1:
        print(element)
        if element in set_2:
            common_set.append(element)
        else:
            continue
    return common_set
