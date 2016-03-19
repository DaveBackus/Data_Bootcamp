"""
Cryptocurrencies:  market quotes from Poloniex 

Links
* https://poloniex.com/exchange#btc_eth
* https://en.wikipedia.org/wiki/Ethereum

Prepared for Data Bootcamp course at NYU
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, March 2016
Created with Python 3.5
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

print('\nPython version: ', sys.version)
print('Pandas version: ', pd.__version__, '\n')

#%%
"""
read json file of quotes 
"""
url1 = 'https://poloniex.com/public?command=returnChartData&currencyPair='
url2 = 'BTC_ETH&start=1435699200&end=9999999999&period=14400'
url = url1 + url2 

df = pd.read_json(url)

print('\nDataframe dimensions:', df.shape)
print('\nVariables and dtypes:\n', df.dtypes, sep='')
df = df.set_index('date')

#%%
fig, ax = plt.subplots()
df['close'].plot()
ax.set_xlabel('')
