"""
Created on Wed Feb 10 19:39:54 2016
@author: Ju
Modified by Dave Backus
"""
import pandas as pd
from pandas.io.data import DataReader
import datetime

# small test sample
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2015, 12, 31)
tickers = ['aapl', 'goog']

# if first argument is a list, this returns a panel
p = DataReader(tickers, 'yahoo', start, end)

print('Type:', type(p))
print('Dimensions:', p.shape)
print('Axis labels:\n', p.describe, sep='')

#%%
# convert to df, shift tickers to columns
df = p.to_frame().unstack('minor')['Adj Close']
df.head(20)

#%%
# convert to monthly (first day of month)
dm = df.resample('MS')
dm.head(20)

#%%
# percent change based on start of month 
test = dm.head()
test.pct_change().shift(-1)

