#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 1 and len(matrix) != 0 and matrix:
        for j in range(len(matrix)):
            for i in range(len(matrix[j])):
                if i != len(matrix[j]) - 1:
                    print("{:d}".format(matrix[j][i]), end=" ")
                else:
                    print("{:d}".format(matrix[j][i]))
    else:
        print()
