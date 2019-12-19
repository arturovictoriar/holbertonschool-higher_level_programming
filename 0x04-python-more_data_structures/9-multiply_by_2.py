#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    copyd = a_dictionary.copy()
    for i, num in copyd.items():
        copyd[i] = num * 2
    return copyd
