# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:56:41 2017
Accessing Elements - Indexing an array with another array
@author: oreid
"""

import numpy as np

def test_run():
    
    a = np.random.rand(5)
    
    #accessign using list of indices
    indices = np.array([1,1,2,3])
    print(a[indices])
    
    a = np.array([1,2,3,4,5,6,7,8,9,10])
    mean = a.mean()
    
    print(a[a<mean])
    
if __name__ == "__main__":
     test_run()