#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = [key for key, v in a_dictionary.items() if v == value]
    for k in key:
        del a_dictionary[k]
    return a_dictionary
