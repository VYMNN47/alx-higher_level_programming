#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for x in matrix:
        if len(x) == 0:
            print()
        for y in range(len(x)):
            print("{:d}".format(x[y])),end="\n"
                  if y is len(x) - 1 else " "
