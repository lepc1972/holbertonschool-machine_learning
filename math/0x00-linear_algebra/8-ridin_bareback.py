#!/usr/bin/env python3
"""write a function that performs the matrix multiplication"""


def mat_mul(mat1, mat2):
    """mat_mul"""
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for i in range(len(mat1)):
        result.append([])
        for j in range(len(mat2[0])):
            result[i].append(0)
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
