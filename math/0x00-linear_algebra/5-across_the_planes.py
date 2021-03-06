#!/usr/bin/env python3
"""write a function that adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """
    Function that adds two matrices element-wise
    """
    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        new_matrix.append([])
        for j in range(len(mat1[0])):
            new_matrix[i].append(mat1[i][j] + mat2[i][j])
    return new_matrix
