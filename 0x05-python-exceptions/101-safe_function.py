#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    p = 0
    try:
        result = fct(args[0], args[1])
        p = 1
    except (ZeroDivisionError) as z:
        print("Exception: {}".format(z), file=sys.stderr)
    except (IndexError) as i:
        print("Exception: {}".format(i), file=sys.stderr)
    if p:
        return result
