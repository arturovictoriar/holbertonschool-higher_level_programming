#!/usr/bin/python3


def best_score(a_dictionary):
    best_k = "Hello"
    if bool(a_dictionary):
        for i in a_dictionary:
            for j in a_dictionary:
                if a_dictionary[j] >= a_dictionary[i]:
                    best_k = j
        return best_k
