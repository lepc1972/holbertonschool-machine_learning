#!/usr/bin/env python3
"""Write a function def poly_integral(poly, C=0):
that calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """Performs integrate of a polynom"""
    if poly == [] or type(poly) is not list or type(C) is not int:
        return None
    if poly == [0]:
        return [C]
    for n in poly:
        if type(n) is not int and type(n) is not float:
            return None

    integrals = [C] + [poly[i] / (i + 1) for i in range(len(poly))]

    result = [int(n) if n % 1 == 0 else n for n in integrals]

    return result
