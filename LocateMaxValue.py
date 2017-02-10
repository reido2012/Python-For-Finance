# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:15:58 2017
Locate maximum value.
@author: oreid
"""


import numpy as np


def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    # TODO: Your code here
    max_val = a.max()
    for i in range(0,len(a)):
        if a[i] == max_val:
            return i

def get_max_index_fast(a):
    return a.argmax()

def test_run():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print("Array:", a)
    
    # Find the maximum and its index in array
    print("Maximum value:", a.max())
    print("Index of max:", get_max_index_fast(a))


if __name__ == "__main__":
    test_run()
