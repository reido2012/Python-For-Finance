# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:41:37 2017
Operations on Arrays
@author: oreid
"""

import numpy as np

def test_run():
    np.random.seed(693) #seed the random number generator
    a = np.random.randint(0, 10, size = (5,4)) #5x4 random integers in [0,10]
    print("Array:\n",a)
    print("\n Sum of All Elements :\n",a.sum())
    
    #Iterate over rows, to compute the sum of each column
    print("\n Sum of each column :\n",a.sum(axis=0))
    
    #Iterate over columns, to compute the sum of each row
    print("\n Sum of each row :\n",a.sum(axis=1))
    
    #Iterate over columns, to compute the sum of each row
    print("\n Sum of each row :\n",a.sum(axis=1))
    
    #Statistics: min, max, mean (across rows, cols, and overall)
    print("Minimum of each column:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.max(axis=1))
    print("Mean of all elements: \n", a.mean())
    
if __name__ == "__main__":
    test_run()
    