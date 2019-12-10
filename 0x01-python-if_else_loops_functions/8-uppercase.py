#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if i == len(str) - 1:
            if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
                print("{:c}".format(ord(str[i]) - 32))
            else:
                print("{}".format(str[i]))
        elif ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            print("{:c}".format(ord(str[i]) - 32), end="")
        else:
            print("{}".format(str[i]), end="")
