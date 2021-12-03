#!/usr/bin/env python3
"""Write a function def np_slice(matrix, axes={}):
that slices a matrix along specific axes"""



def np_slice(matrix, axes={}):
    """Slices a matrix like a ninja"""
    ax_values = {}
    max_axis = max(axes.keys())

    for j in range(max_axis):
        ax_values[j] = (None, None, None)

    for key in axes.keys():
        ax_values[key] = axes[key]

    return(matrix[tuple(slice(*ax_values[i]) for i in ax_values.keys())])
