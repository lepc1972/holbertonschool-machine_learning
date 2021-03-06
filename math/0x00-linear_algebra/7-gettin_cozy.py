#!/usr/bin/env python3
"""Matrix concatenation"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ Concatenates two matrices. Depends on the types axi"""
    concat = [[n for n in row] for row in mat1]

    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None

        for row in mat2:
            concat.append(row)

    elif axis == 1:
        if len(mat1) != len(mat2):
            return None

        for row in range(len(mat1)):
            concat[row].extend(mat2[row])

    return concat
