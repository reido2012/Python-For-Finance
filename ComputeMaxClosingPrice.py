# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:20:15 2016

@author: oreid
"""

import pandas as pd

def get_max_close(symbol):
    """Return the maximum closing value of stock indicated by the symbol
    Note: Data for a stock is stored in file: data/ <symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol)) #Read in data
    return df['Close'].max() #Compute and return max

def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.
    
    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    # TODO: Compute and return the mean volume for this stock
    return df['Volume'].mean()

    
def test_run():
    for symbol in ['AAPL', 'IBM']:
        print("Max Close")
        print( symbol, get_max_close(symbol))


        
if __name__ == "__main__": #if run by itself
    test_run()