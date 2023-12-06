#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rslt_matrix = [[0 for _ in range(len(row))] for row in matrix]

    for itm in range(len(matrix)):
        for i in range(len(matrix[itm])):
            rslt_matrix[itm][i] = matrix[itm][i] ** 2
    return rslt_matrix
