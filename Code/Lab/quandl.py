"""
Messing around with Quandl, a popular online collection of economic and 
finance data.  Known for easy access and clear links to original sources, 
so you know what you have.  
   
Install the Python app by typing in the command line:  pip install Quandl

**** Nothing here yet, something to work on **** 

Prepared for the NYU Course "Data Bootcamp." 
More at https://github.com/DaveBackus/Data_Bootcamp 

References 
* http://www.quandl.com/ 
* https://github.com/quandl/Python
* http://www.quandl.com/help/api 

Written by Dave Backus @ NYU, September 2014  
Created with Python 3.4 
"""
import pandas as pd
#import datetime as dt 

# Examples from the GitHub repository 

data = Quandl.get('PRAGUESE/PX', authtoken='xxxxxx', trim_start='2001-01-01',
                  trim_end='2010-01-01', collapse='annual',
                  transformation='rdiff', rows=4, returns='numpy')

#%%
                  
Quandl.search(query = "Search terms", source = "Source you wish to search", 
              page = 1)                  

python
import Quandl
datasets = Quandl.search('OIL')
datasets[0]

data = Quandl.get('GOOG/NYSE_IBM', collapse='weekly')
data.head()

#%%
# the . points to a specific column of the data source, here the close 
data= Quandl.get(['GOOG/NASDAQ_AAPL.4','GOOG/NASDAQ_MSFT.4'])

