#!/usr/bin/env python3
# write a function that adds two arrays elements-wise


def add_arrays(arr1, arr2):
    """
    Return the sum of two arrays
    """
    if len(arr1) != len(arr2):
        return None
    return [x + y for x, y in zip(arr1, arr2)]
