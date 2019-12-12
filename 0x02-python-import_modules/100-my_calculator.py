#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    operator = ['+', '-', '*', '/']
    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == operator[0]:
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif sys.argv[2] == operator[1]:
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif sys.argv[2] == operator[2]:
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif sys.argv[2] == operator[3]:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
if __name__ == "__main__":
    main()
