# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:01:59 2016

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
    
    #Rename 'Adj Close' column to SPY to prevent clas
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
    
    #Join the two datframes - 'inner' performs inner join
    df1 = df1.join(dfSPY, how ='inner')
   
    #read in more stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp = pd.read_csv(
                              "data/{}.csv".format(symbol),
                              index_col = 'Date',
                              parse_dates = True,
                              usecols=['Date', 'Adj Close'],
                              na_values=['nan']
                             )
        #rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp)
        
    print(df1)
    
if __name__ == "__main__":
    test_run()