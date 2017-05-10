#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for count in matrix:
        new = []
        for count2 in count:
            new.append(' '.join('{:d}'.format(count2)))
        print(' '.join(new))
