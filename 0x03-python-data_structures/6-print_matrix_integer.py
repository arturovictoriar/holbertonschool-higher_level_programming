#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 1 and len(matrix) != 0:
        for j in range(len(matrix)):
            for i in range(len(matrix[j])):
                if i != len(matrix[j]) - 1:
                    print("{}".format(matrix[j][i]), end=" ")
                else:
                    print("{}".format(matrix[j][i]))
    else:
        print()
