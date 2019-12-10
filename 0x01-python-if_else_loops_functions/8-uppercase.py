#!/usr/bin/python3
def uppercase(str):
    newline = ""
    for i in range(len(str)):
        if i == len(str) - 1:
            newline = "\n"
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            print("{:c}{}".format(ord(str[i]) - 32, newline), end="")
        else:
            print("{}{}".format(str[i], newline), end="")
