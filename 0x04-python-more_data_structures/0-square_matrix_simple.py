#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    new = [[index ** 2 for index in row] for row in matrix]
    return (new)
