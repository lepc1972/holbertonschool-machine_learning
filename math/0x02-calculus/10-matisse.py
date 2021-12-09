#!/usr/bin/env python3
"""Write a function def poly_derivative(poly): that calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial"""
    if len(poly) == 0:
        return []
    elif len(poly) == 1:
        return [0]
    else:
        deriv = []
        for i in range(1, len(poly)):
            deriv.append(i * poly[i])
        return deriv
