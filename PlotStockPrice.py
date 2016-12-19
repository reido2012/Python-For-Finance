# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:40:17 2016

@author: oreid
"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    df['Adj Close'].plot()
    plt.show() #must be called to show plots

if __name__ == "__main__": #if run by itself
    test_run()