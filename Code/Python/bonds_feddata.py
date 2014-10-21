"""
Calculations with the Gurkaynak, Sack, and Wright interest rate data from 
the Fed.  They estimate a smooth forward rate curve and post its parameters. 
We take the parameter values and reconstruct log bond prices for an arbitrary
set of maturities and use them to 
* Construct an animation of bond yields
* Run forecasting regressions.  
Two versions, standard bonds and inflation-protected bonds (TIPS)  

Prepared for the NYU Course "Macroeconomic Foundations for Asset Prices," 
ECO-UB-233.  More at
* https://sites.google.com/site/nyusternmacrofoundations/home
* https://github.com/DaveBackus/MFAP

References
* http://www.federalreserve.gov/pubs/feds/2006/200628/200628abs.html
* http://www.federalreserve.gov/pubs/feds/2008/200805/200805abs.html
* http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv
* http://pandas.pydata.org/pandas-docs/version/0.13.1/timeseries.html

Written by Sarah Beckett-Hile and adapted by Dave Backus, September 2014 
With help, as always, from Chase Coleman and Spencer Lyon  
Created with Python 3.4 
"""
import pandas as pd 
from math import exp
#import datetime as dt 
#import os
#import urllib

"""
1. Read in csv version of Fed data 
""" 
df = pd.read_csv('feds200628.csv', skiprows=9, index_col=0,     # 0!
                     parse_dates=True, na_filter=False)     
#tips = pd.read_csv('feds200805.csv', skiprows=18, index_col=0)

#%%
keep = ['BETA0', 'BETA1', 'BETA2', 'BETA3', 'TAU1', 'TAU2'] 
df = df[keep]

type(df)
df.columns
df.index
df.head()

#%%

# convert to monthly, last obs of month
# this seems to sort it, too
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort.html
resampled_df = df.resample("M", "last").sort()

#%%
# creating a one-row DF in order to build the structure for calculating
# the forward rates and puting them into a graph.
# Later this will be for the entire resampled_df table
sample = resampled_df[:1]
# replacing all empty cells with value 0
sample = sample.replace('', 0, regex=True)
#%%
# this goes through each row of the DF one by one and plugs the values
# into an equation to determine forward rates while N = 1, 2, 5, 12
for index, i in sample.iterrows():
    b0 = i['BETA0']
    b1 = i['BETA1']
    b2 = i['BETA2']
    b3 = i['BETA3']
    t1 = i['TAU1']
    t2 = i['TAU2']
    n_list = [1, 2, 5, 10]
    forward_rates = []
    while len(n_list) > 0:
        n = n_list[0]
        if b3 > 0 and t2 >0:
            f_rate = b0 + b1*exp(-n/t1) + b2*(n/t1)*exp(-n/t1)+b3*(n/t2)*exp(-n/t2)
        else: 
            f_rate = b0 + b1*exp(-n/t1) + b2*(n/t1)*exp(-n/t1)
        forward_rates.append(f_rate)
        n_list.pop(0)
        print f_rate
    val1 = 1, forward_rates[0]
    val2 = 2, forward_rates[1]
    val3 = 5, forward_rates[2]
    val4 = 10, forward_rates[3]    
    
