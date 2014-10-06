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
resampled_df = df.resample("M", "last")
resampled_df.head()

#%%
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort.html
resampled_df.sort()

#%%
df.head()

#%%
