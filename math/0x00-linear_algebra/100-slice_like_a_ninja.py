#!/usr/bin/env python3
"""Write a function def np_slice(matrix, axes={}):
that slices a matrix along specific axes"""


def np_slice(matrix, axes={}):
    import numpy as np
    """Write a function def np_slice(matrix, axes={}): that slices a matrix along specific axes"""
    return matrix[tuple(axes.values())]
