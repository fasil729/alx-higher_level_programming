#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary.values())
        keys = list(a_dictionary.keys())
        key = keys[list(a_dictionary.values()).index(max_value)]
        return key
    return None
