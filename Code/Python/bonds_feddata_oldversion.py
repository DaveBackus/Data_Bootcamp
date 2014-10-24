# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 10:58:14 2014

@author: sarahbeckett-hile
"""

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
import pandas as pd # for dataframe
from math import exp, pow # for function
from datetime import datetime

# (*) Import plotly package
import plotly

# Check plolty version (if not latest, please upgrade)
#print plotly.__version__

# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py  

# (*) Useful Python/Plotly tools
import plotly.tools as tls   

# (*) Graph objects to piece together plots
from plotly.graph_objs import *

import numpy as np  # (*) numpy for math functions and arrays
py.sign_in("sebecketthile", "a649z2ue29")
#import datetime as dt 
#import os
#import urllib
#%%
"""
1. Read in csv version of Fed data 
""" 
df = pd.read_csv('Dropbox/data_bootcamp/code/Python/feds200628.csv', skiprows=9, index_col=0,     # 0!
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
# replacing all empty cells with value 0
# resampled_df = resampled_df.replace('', 0, regex=True) 
#%%
"""
creating a one-row DF in order to build the structure for calculating
the forward rates and puting them into a graph.
Later this will be for the entire resampled_df table
"""
sample = resampled_df[:1]

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
    n_list = [1, 2, 5, 10] # months
    forward_rates = []
    while len(n_list) > 0:
        n = n_list[0]
        if b3 > 0 and t2 >0: #need if statement becuase b3 andd t2 data missing for first several rows
            f_rate = b0 + b1*exp(-n/t1) + b2*(n/t1)*exp(-n/t1)+b3*(n/t2)*exp(-n/t2)
        else: 
            f_rate = b0 + b1*exp(-n/t1) + b2*(n/t1)*exp(-n/t1)
        forward_rates.append(f_rate)
        n_list.pop(0)
        print f_rate
    # create simple graph in plotly 
    # https://plot.ly/python/line-and-scatter-plots-tutorial/
    trace1 = Scatter(
        x=[1, 2, 5, 12],
        y=[forward_rates[0], forward_rates[1], forward_rates[2], forward_rates[3]]
        )
    data = Data([trace1])
    plot_url = py.plot(data, filename='basic-line')
 #%%   
# now to try streaming

#First, limit resampled_df to the years we're interested in
recent_df = resampled_df[resampled_df.index > datetime(1980, 1, 1)].convert_objects(convert_numeric=True)
recent_df.head()
#%%
#apply function to get forward rates
for index, i in recent_df.iterrows():
    b0 = i['BETA0']
    b1 = i['BETA1']
    b2 = i['BETA2']
    b3 = i['BETA3']
    t1 = i['TAU1']
    t2 = i['TAU2']  
    n_list = [1, 2, 5, 10]
    for n in n_list:
        column_name = "{}".format(n)
        recent_df[column_name] = b0 + b1*exp(-n/t1) + b2*(n/t1)*exp(-n/t1)+b3*(n/t2)*exp(-n/t2)

#%%
recent_df.head()

#%%
# First, get stream_ids/"Stream Tokens" from Plotly
# https://plot.ly/python/streaming-tutorial/#Get-your-stream-tokens
tls.set_credentials_file(stream_ids=[
        "dy4p7j6jq5",
        "t8fxiaa0in",
        "kwba1bggon",
        "54qig5k2lg"
    ])
stream_ids = tls.get_credentials_file()['stream_ids']
#%%
# (!) Get stream id from stream id list, 
#     only one needed for this plot
stream_id = stream_ids[0]

# Make a stream id object linking stream id to 'token' key
stream = Stream(token=stream_id) 
#%%
# create an empty dataframe to 
