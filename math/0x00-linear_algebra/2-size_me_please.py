#!/usr/bin/env python3
"""Returns the shape of a matrix wiyh recursion"""


def matrix_shape(matrix):
    """Returns the shape of a matrix wiyh recursion"""
    if type(matrix) is not list:
        return []
    if len(matrix) == 0:
        return []
    if type(matrix[0]) is not list:
        return [len(matrix)]
    return [len(matrix)] + matrix_shape(matrix[0])
