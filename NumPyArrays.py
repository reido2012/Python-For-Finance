# -*- coding: utf-8 -*-
"""
Creating NumPy Arrays
- Useful when you want to take sequence 
- of data and put into an array

Created on Mon Jan 30 11:28:58 2017

@author: oreid
"""

import numpy as np

def test_run():
    print("List to 1D arrray")
    print(np.array([2,3,4]))
    
    print("\nList of tuples to 2d array")
    print(np.array([(2,3,4),(5,6,7)]))
    
    print("\nEmpty array")
    #Can do N-dimensional
    print(np.empty(5))
    print(np.empty((5,4)))
    
    print("\nArray of 1's")
    #Can do N-dimensional
    print(np.ones((5,4), dtype=np.int))
    
    print("\nArray of 0's")
    #Can do N-dimensional
    print(np.zeros((5,4)))

if __name__ == "__main__":
    test_run()