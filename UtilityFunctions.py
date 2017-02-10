# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:20:38 2016
Utility Functions
@author: oreid
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    "Returns CSV file path given a ticker symbol"
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    "Read stock data (adjusted close) for given symbols from csv files"
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')
        
    for symbol in symbols:
        df_temp = pd.read_csv(
                              symbol_to_path(symbol),
                              index_col = 'Date',
                              parse_dates = True,
                              usecols=['Date', 'Adj Close'],
                              na_values=['nan']
                             )
        #rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        
        if symbol == 'SPY': #Drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])
        
    return df

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    df = df.ix[start_index:end_index, columns]
    plot_data(df, title="Selected Data")
    
def plot_data(df, title="Stock prices"):
    #Plot stock prices
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def normalize_data(df):
    #Normalize stock prices using the first row of the dataframe
    return df/df.ix[0,:]

def test_run():
    start_date = '2016-01-01';
    end_date = '2016-12-19';
    #Define a date range
    dates = pd.date_range(start_date, end_date)
    
    #Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD'] #SPY will be added

    #Get stock data
    df = get_data(symbols, dates)
    df = normalize_data(df)
    plot_selected(df, symbols, start_date, end_date)
    
    #compute global statistics for each stock
    #df.mean - Mean for each column
    #df.median, mode,std (standard deviation)
    print(df.std())
    
    

    
if __name__ == "__main__":
    test_run()
    