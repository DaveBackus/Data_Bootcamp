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
# Define an annotation-generating function (to label year and data source)
def make_anno(date):
    anno_text = '<b>Year: {}</b><br>Data source: GapMinder'.format(date)
    return dict(
        text=anno_text,  # set annotation text
        showarrow=False, # remove arrow 
        xref='paper',  # use paper coords
        yref='paper',  #  for both coordinates
        x=0.95,  # position's x-coord
        y=0.05,  #   and y-coord
        font=Font(size=14),    # increase font size (default is 12)
        bgcolor='#FFFFFF',     # white background
        borderpad=4            # space bt. border and text (in px)
)
#%%
# Get stream_ids/"Stream Tokens" from Plotly
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
# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = Scatter(
    x=[],     # init. data
    y=[], 
    text=[],  # init. hover text
    mode='markers',           
    marker=Marker(
        color=[],  # init. marker color
        size=[],   # init. marker sizes
        opacity=0.6,          # partly transparent markers
        line=Line(width=0.0)  # remove marker borders
    ),
    stream=stream  # (!) embed stream id, 1 per trace
)

data = Data([trace1])
#%%
# Set plot and axis titles
title = "Federal Bond Data Forward Rates Over Time"  # plot's title
x_title = "Maturity [in months]"
y_title = "Forward Rate"
#%%
# Define a dictionary of axis style options
axis_style = dict(     
    zeroline=False,       # remove thick zero line
    gridcolor='#FFFFFF',  # white grid lines
    ticks='outside',      # draw ticks outside axes 
    ticklen=8,            # tick length
    tickwidth=1.5         #   and width
)
#%%
# Initialize layout object
layout = Layout(
    title=title,  # set plot title
    xaxis=XAxis(
        axis_style,            # add style options
        title=x_title,         # set x-axis title
        range=[1,12]  # set range
    ),
    yaxis=YAxis(
        axis_style,            # add style options

        title=y_title,         # y-axis title
        range=[0,y_max]          # set range
    ),  
    showlegend=False,         # remove legend (info in hover)
    hovermode='closest',      # (!) hover -> closest data pt
    plot_bgcolor='#EFECEA',   # set plot color to grey
    autosize=False,  # turn off autosize
    width=650,       # plot width
    height=500,      # plot height
)
#%%
# Make a figure object
fig = Figure(data=data, layout=layout)

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='forward_rates')
#%%
# (@) Make instance of the Stream link object, 
#     with same stream id as Stream id object
s = py.Stream(stream_id)

# (@) Open the stream
s.open()
#%%
for index, i in stream_df.iterrows():
    s_data = {}  # initialize data dict. to be streamed
    s_layout = dict(annotations=[make_anno(index)]) # layout dict. to be streamed
    limit_df = stream_df[stream_df.index == index].transpose().reset_index()
    s_data['x'] = transposed_df[[0]]  # x-xaxis
    s_data['y'] = transposed_df[[1]]  #  y-axis
    #s_data['text'] = i # hover text info
    # (@) Write data and layout dict. to stream, every 0.1 sec
    s.write(s_data, layout=s_layout)                    
    time.sleep(0.1)                                   
    if i!=i[-1]:  # except for last year in the dataframe
        time.sleep(2)   
        s_data = dict(x=[],y=[],marker=dict(color=[],size=[]),text=[])
        s.write(s_data, layout=s_layout) # clear data, keep layout
#%%      
s.close()  # (!) close stream when done