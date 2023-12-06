#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda z: list(map(lambda u: u**2, z)), matrix))
