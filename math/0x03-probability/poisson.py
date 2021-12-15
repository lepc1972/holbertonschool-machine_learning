#!/usr/bin/env python3
"""Create a class Poisson that represents a poisson distribution"""


class Poisson:
    """Poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Constructor"""
        self.lambtha = float(lambtha)
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = self.__calculate_lambtha(data)

    def __calculate_lambtha(self, data):
        """Calculate the value of lambtha"""
        mean = sum(data) / len(data)
        return mean

    def pmf(self, k):
        """Calculate the value of the pmf for a given number of successes"""
        if type(k) != int:
            raise TypeError("k must be an integer")
        if k < 0:
            return 0
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        return (self.lambtha ** k) * (e ** -self.lambtha) / factorial

    def cdf(self, k):
        """Calculate the value of the cdf for a given number of successes"""
        if type(k) != int:
            raise TypeError("k must be an integer")
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
