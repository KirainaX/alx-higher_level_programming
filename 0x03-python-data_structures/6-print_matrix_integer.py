#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("")
    else:
        for elment in range(len(matrix)):
            for i in range(len(matrix[elment])):
                if i != len(matrix[elment]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[elment][i]), end=endspace)
            print("")
