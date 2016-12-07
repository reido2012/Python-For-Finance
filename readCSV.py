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
    print(df.head())

if __name__ == "__main__":
        test_run()