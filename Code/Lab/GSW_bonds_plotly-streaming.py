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

Data references
* http://www.federalreserve.gov/pubs/feds/2006/200628/200628abs.html
* http://www.federalreserve.gov/pubs/feds/2008/200805/200805abs.html

Python references
* http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv
* http://pandas.pydata.org/pandas-docs/version/0.13.1/timeseries.html

Written by Sarah Beckett-Hile and adapted by Dave Backus, September 2014
With help, as always, from Chase Coleman and Spencer Lyon
Created with Python 3.4
"""
import pandas as pd # for dataframe
from math import exp, ceil, floor # for forward rate function
from datetime import datetime # to deal with the date format in the table
import time # to limit the time each graph is shown while streaming
#import os
#import urllib
#%%
"""
<<<<<<< Updated upstream:Code/Lab/GSW_bonds_plotly-streaming.py
1. Read in csv version of Fed data
"""
df = pd.read_csv('../Data/feds200628.csv', skiprows=9, index_col=0,     # 0!
                     parse_dates=True, na_filter=False)
=======
1. Read in csv version of Fed data 
""" 
df = pd.read_csv('/Users/sarahbeckett-hile/Desktop/feds200628.csv', skiprows=9, index_col=0,     # 0!
                     parse_dates=True, na_filter=False)     
>>>>>>> Stashed changes:Code/Python/bonds_feddata_streaming.py
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
recent_df = resampled_df[resampled_df.index > datetime(1990, 1, 1)].convert_objects(convert_numeric=True)
#%%
#apply function to get forward rates
forward_rate_list = []
for index, i in recent_df.iterrows():
    b0 = i['BETA0']
    b1 = i['BETA1']
    b2 = i['BETA2']
    b3 = i['BETA3']
    t1 = i['TAU1']
    t2 = i['TAU2']
    n_list = [0, 1, 3, 12, 24, 60, 120]
    for n in n_list:
        column_name = "{}".format(n)
        forward_rate = b0 + b1*exp(-n/t1) + b2*(n/t1)*exp(-n/t1)+b3*(n/t2)*exp(-n/t2)
        recent_df.ix[index, column_name] = forward_rate
        forward_rate_list.append(forward_rate) # doing this to easily pull out the min and max value
#%%
stream_df = recent_df[['0', '1', '3', '12', '24', '60', '120']] # get rid of the beta/tau info
#%%
# set limits for the graph
x_max = max(n_list)
x_min = min(n_list)
y_max = ceil(max(forward_rate_list)) # ceil rounds up
y_min = floor(min(forward_rate_list)) # floor rounds down

#%%
# Now let's try to stream!
# (*) Import plotly package
#import plotly     # hashed out because it doesn't seem to be necesary, although plotly's documentation says we should import it

# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py
#%%
py.sign_in("sebecketthile", "a649z2ue29")

#%%

# (*) Useful Python/Plotly tools
import plotly.tools as tls

# (*) Graph objects to piece together plots
from plotly.graph_objs import *
#%%
# get streaming tokens https://plot.ly/python/streaming-tutorial/
tls.set_credentials_file(stream_ids=["dy4p7j6jq5"])
stream_ids = tls.get_credentials_file()['stream_ids']

# Get stream id from stream id list
stream_id = stream_ids[0]
#%%
# Make instance of stream id object
stream = Stream(
    token=stream_id,  # (!) link stream id to 'token' key
    maxpoints=12      # (!) keep a max of 80 pts on screen
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
# Eastblishes the layout of the graph. Instead of deleting lines that I don't want to use, I've hashed them out so we still know they are options
layout = Layout(
    title='Federal Bond Forward Rates',  # set plot title
    xaxis=XAxis(
        #axis_style,            # add style options
        title='Maturity [in months]',         # set x-axis title
        range=[x_min,x_max]  # set range
    ),
    yaxis=YAxis(
        #axis_style,            # add style options
        title='Forward Rate',         # y-axis title
        range=[y_min,y_max]          # set range
    ),
    showlegend=False,         # remove legend (info in hover)
    hovermode='closest',      # (!) hover -> closest data pt
    #plot_bgcolor='#EFECEA',   # set plot color to grey
    autosize=True,  # turn on autosize
    #width=750,       # plot width if autosize = False
    #height=700,      # plot height if autosize = False
)
#%%
# function to be able to plug the index (date of each forward rate), convert it to a string...
# and display it in the bottom right of the graph
def make_anno(date):
    date_string = date.strftime('%Y-%m-%d')
    anno_text = '{}'.format(date_string) # we can add any additional text here
    return dict(
        text=anno_text,  # set annotation text
        showarrow=False, # remove arrow
        xref='paper',  # use paper coords
        yref='paper',  #  for both coordinates
        x=0.95,  # position's x-coord
        y=0.05,  #   and y-coord
        font=Font(size=14),    # increase font size (default is 12)
        bgcolor='#EFFBFB',     # light blue background
        borderpad=6            # space bt. border and text (in px)
)
#%%
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
x = 0
while x < 2:
    i += 1
    for index, i in stream_df.iterrows():
        limit_df = stream_df[stream_df.index == index].transpose().reset_index()
        limit_df['stand_in'] = limit_df[[1]]    # this was a hacky way to get around the issues I was having with the date format of the column head, which didn't want to play nice when put into a dictionary
        s_data = {} # data to be passed to plotly's graph has to be in a dict
        s_data['x'] = limit_df['index'].tolist()    # x-xaxis
        s_data['y'] = limit_df['stand_in'].tolist() #  y-axis
        #s_data['text'] = limit_df['stand_in'].tolist()     # can be used to add to the hover text
        s_layout = dict(annotations=[make_anno(index)]) # this uses make_anno to put the index (the date) on the graph
        s.write(s_data, layout=s_layout)
        time.sleep(0.08)
s.close()
