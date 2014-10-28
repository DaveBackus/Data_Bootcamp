# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 12:54:12 2014

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
from math import exp, ceil # for forward rate function
from datetime import datetime
#import os
#import urllib
#%%
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
#Limit resampled_df to the years we're interested in and convert all numbers (some of which are currently objects) to float64
recent_df = resampled_df[resampled_df.index > datetime(1980, 1, 1)].convert_objects(convert_numeric=True)
#%%
#apply function to get forward rates
for index, i in recent_df.iterrows():
    forward_rate_list = []
    b0 = i['BETA0']
    b1 = i['BETA1']
    b2 = i['BETA2']
    b3 = i['BETA3']
    t1 = i['TAU1']
    t2 = i['TAU2']  
    n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for n in n_list:
        column_name = "{}".format(n)
        forward_rate = b0 + b1*exp(-n/t1) + b2*(n/t1)*exp(-n/t1)+b3*(n/t2)*exp(-n/t2)
        recent_df[column_name] = forward_rate
        forward_rate_list.append(forward_rate) #doing this to easily pull out the max value
#%%
keep_columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
stream_df = recent_df[keep_columns][:4] #keeping it short for testing
#%%
max_value = max(forward_rate_list)
y_max = ceil(max_value)
#%%
# Now let's try to stream!
# (*) Import plotly package
import plotly

# Check plolty version (if not latest, please upgrade)
#print plotly.__version__

# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py  
py.sign_in("sebecketthile", "a649z2ue29")

# (*) Useful Python/Plotly tools
import plotly.tools as tls   

# (*) Graph objects to piece together plots
from plotly.graph_objs import *
#%%
tls.set_credentials_file(stream_ids=[
        "dy4p7j6jq5",
        "t8fxiaa0in",
        "kwba1bggon",
        "54qig5k2lg"
    ])
stream_ids = tls.get_credentials_file()['stream_ids']

# Get stream id from stream id list 
stream_id = stream_ids[0]
#%%
# Make instance of stream id object 
stream = Stream(
    token=stream_id,  # (!) link stream id to 'token' key
    maxpoints=4      # (!) keep a max of 80 pts on screen
)

#%%
# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream         # (!) embed stream id, 1 per trace
)

data = Data([trace1])
#%%
# Add title to layout object
layout = Layout(title='Federal Bond Forward Rates')

# Make a figure object
fig = Figure(data=data, layout=layout)
#%%
# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='s7_first-stream')
#%%
# (@) Make instance of the Stream link object, 
#     with same stream id as Stream id object
s = py.Stream(stream_id)

# (@) Open the stream
s.open()
#%%
#%%
for index, i in stream_df.iterrows():
    limit_df = stream_df[stream_df.index == index].transpose().reset_index()
    s_data = {}
    s_data['x'] = limit_df[[0]]  # x-xaxis
    s_data['y'] = limit_df[[1]]  #  y-axis
    s.write(s_data)             
    time.sleep(0.1)                                   
s.close()
