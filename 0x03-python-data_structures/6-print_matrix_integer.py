#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for arr in matrix:
            row = " ".join(["{:d}".format(num) for num in arr])
            print(row)
