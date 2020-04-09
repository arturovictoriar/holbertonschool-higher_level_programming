#!/usr/bin/python3
"""
    Find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        peak = list_of_integers[0]

    for i, num in enumerate(list_of_integers):
        if num >= list_of_integers[len(list_of_integers) - 1 - i]:
            max_num = num
        else:
            max_num = list_of_integers[len(list_of_integers) - 1 - i]

        if max_num > peak:
            peak = max_num

        if (len(list_of_integers) // 2) - i <= 0:
            break

    return peak
