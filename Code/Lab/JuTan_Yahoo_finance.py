"""
Created on Wed Feb 10 19:39:54 2016
@author: Ju
Modified by Dave Backus
"""
import pandas as pd
from pandas.io.data import DataReader
import datetime

# small test sample
start = datetime.datetime(2015, 12, 21)
end = datetime.datetime(2015, 12, 31)
tickers = ['aapl', 'goog']

# if first argument is a list, this returns a panel
p = DataReader(tickers, 'yahoo', start, end)

print('Type:', type(p))
print('Dimensions:', p.shape)
print('Axis labels:\n', p.describe, sep='')

#%%
close = p['Adj Close']
c = close.stack().sortlevel(level=1).swaplevel(0,1)
c

#%%
# another version:  to_frame does the stacking automatically
# can select variable at the start or the end
df = p.to_frame().swaplevel(0,1).sortlevel(level=0)['Adj Close']
df

#%%
"""
Ju's version (stripped down)
"""
d = {}
for ticker in tickers:  #symbols_list:
    d[ticker] = DataReader(ticker, "yahoo", start, end)

pan = pd.Panel(d)
df = pan.minor_xs('Adj Close')
df

#df.to_csv("yahoo closing price value.csv")

