# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:56:22 2017
Accessing array elements
@author: oreid
"""
import numpy as np

def test_run():
    a = np.random.rand(5,4)
    print("Array:\n", a)
    
    #Acessing element at position (3,2)
    element = a[3,2]
    print(element)
    
    #Slicing
    #Note: Slice n:m:t specifies a range that starts n,
    #and stops before m in t jumps
    print(a[:, 0:3:2])

if __name__ == "__main__":
    test_run()