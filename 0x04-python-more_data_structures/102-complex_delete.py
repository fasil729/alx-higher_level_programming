#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while True:
        try:
            keys = list(a_dictionary.keys())
            values = list(a_dictionary.values())
            key = keys[values.index(value)]
            del (a_dictionary[key])
        except ValueError:
            return a_dictionary
