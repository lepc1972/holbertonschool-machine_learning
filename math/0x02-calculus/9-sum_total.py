#!/usr/bin/env python3
"""Write a function def summation_i_squared(n): that calculates [\sum_{i=1}^{n} i^2] :"""


def summation_i_squared(n):
    """Calculates the summation of the squares of the integers from 1 to n:
    Args:
        n: integer that represents the final value of the summation
    Returns:
        The summation of the squares of the integers from 1 to n
    """
    if type(n) is not int or n < 1:
        return None
    return sum([i**2 for i in range(1, n+1)])
