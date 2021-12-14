#!/usr/bin/env python3
"""Create a class Poisson that represents a poisson distribution"""


import numpy as np
class Poisson:
    """Poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        """Initialize Poisson class"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = lambtha
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = np.mean(data)

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of events"""
        if type(k) != int:
            raise TypeError("k must be an integer")
        if k < 0:
            return 0
        return (np.math.factorial(k) / (self.lambtha ** k * np.math.exp(1)))

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of events"""
        if type(k) != int:
            raise TypeError("k must be an integer")
        if k < 0:
            return 0
        sum = 0
        for i in range(k + 1):
            sum += self.pmf(i)
        return sum
