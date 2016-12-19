# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:04:31 2016

@author: oreid
"""

import pandas as pd

def test_run():
    #    Store Apple stock data as CSV
    df = pd.read_csv("data/AAPL.csv")
    #print entire dataframe
    #print(df) 
    
    #Print top 5 lines of csv
    print("\nHEAD")
    print("#################")
    print(df.head())
    
    #Print last 5 lines of 
    print("\nTAIL")
    print("#################")
    print(df.tail())
    
    #Print select rows - called slicing
    print("\n Between index 10 and 20")
    print(df[10:21])
    

if __name__ == "__main__":
        test_run()