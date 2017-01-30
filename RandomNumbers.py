# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:50:32 2017
Generating Random Numbers
@author: oreid
"""

import numpy as np

def test_run():
    #Generate an array full of random numbers uniformly sampled from [0.0, 1.0
    print("Random - Basic")
    print(np.random.random((5,4)))
    
    #Sample numbers from a Gaussian distribution
    print("\nRandom - Gaussian (Normal) Distribution")
    print(np.random.normal(size=(2, 3))) #Standard normal (mean = 0, sd = 1)
    
    #2x3 array of random integers
    print("\nUniform Distribution")
    uniform = np.random.randint(0,10, size=(2, 3))
    print(uniform) #Standard normal (mean = 0, sd = 1)
    print("Shape of nparray uniform: ")
    print(uniform.shape)
    
    #Number of rows
    print(uniform.shape[0])
    
    #Number of columns
    print(uniform.shape[1])
    
    #Number of dimensions
    print(len(uniform.shape))
    print(uniform.size)
    
    
    
if __name__ == "__main__":
     test_run()