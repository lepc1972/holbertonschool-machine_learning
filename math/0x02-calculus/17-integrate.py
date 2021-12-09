#!/usr/bin/env python3
"""Write a function def poly_integral(poly, C=0): that calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """
    Returns the integral of a polynomial
    """
    if type(poly) is not list:
        return None
    if any(type(x) is not int for x in poly):
        return None
    if len(poly) == 0:
        return None
    integral = [C]
    for x in range(len(poly)):
        integral.append(poly[x] / (x + 1))
    return integral
