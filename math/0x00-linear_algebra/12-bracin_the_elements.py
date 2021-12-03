#!/usr/bin/env python3
"""Write a function def np_elementwise(mat1, mat2):
that performs element-wise addition, subtraction, multiplication,
and division"""


def np_elementwise(mat1, mat2):
    """Return the element-wise addition, subtraction, multiplication,
    and division of two matrices"""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
