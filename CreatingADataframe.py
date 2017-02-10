# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:59:46 2016
Build a dataframe in padas
@author: oreid
"""

import pandas as pd

def test_run():
    start_date = '2016-12-01'
    end_date = '2016-12-06'
    #return an array of date time objects
    dates = pd.date_range(start_date, end_date)

    #Create a new empty datfame with index as dates
    df1 = pd.DataFrame(index=dates)

    #Read SPY data into temporary dataframe
    #Need to change this to work off index of dates
    dfSPY = pd.read_csv(
                        "data/SPY.csv",
                        index_col = "Date", 
                        parse_dates = True,
                        usecols=['Date', 'Adj Close'], 
                        na_values=['nan']
                        )
    
    #Join the two dataframes
    df1 = df1.join(dfSPY, how ='inner')
    print (df1)
    
if __name__ == "__main__":
    test_run()