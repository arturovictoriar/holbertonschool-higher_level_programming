#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        num = [1, 5, 10, 50, 100, 500, 1000]
        numero = 0
        for l in roman_string:
            for r, n in zip(roman, num):
                if r == l:
                    numero += n
        return numero
    return 0
