#!/usr/bin/env python3
"""write a function  that returns the transpose of a matrix""


def matrix_transpose(matrix):
    """
    Returns the transpose of a matrix.
    """
    return [list(i) for i in zip(*matrix)]
