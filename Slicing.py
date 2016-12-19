# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:04:14 2016
Slicing Practice
@author: oreid
"""
import pandas as pd
import UtilityFunctions as uf
import matplotlib.pyplot as plt

def test_run():
    #Define a date range
    dates = pd.date_range('2016-01-01', '2016-12-19')
    
    #Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD'] #SPY will be added

    #Get stock data
    df = uf.get_data(symbols, dates)
    
    #Slice by row range (dates) using DataFrame.ix[] selector
    #print(df.ix['2016-01-01' : '2016-01-31']) #The month of January
    
    #Slice by column (symbols)
    #print(df['GOOG']) #A single label selects a single column
    #print(df[['IBM', 'GLD']]) #A list of labels selects multiple columns
    
    #Slice by row and column
    df = df.ix['2016-07-01':'2016-07-14', ['SPY', 'IBM']]
    print(df)
    #df = df/df.ix[0]
    uf.plot_data(df)
    
if __name__ == "__main__":
    test_run()