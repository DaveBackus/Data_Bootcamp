"""
Messing around with World Bank data.   

Prepared for the NYU Course "Data Bootcamp." 
More at https://github.com/DaveBackus/Data_Bootcamp 

References 
* http://data.worldbank.org/
* http://pandas.pydata.org/pandas-docs/stable/remote_data.html#world-bank
* http://quant-econ.net/pandas.html 

Written by Dave Backus @ NYU, August 2014  
Created with Python 3.4 
"""
import pandas.io.data as web
import datetime as dt 

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = 6, 4.5  # default is 6, 4
mpl.rcParams['legend.fontsize'] = 10  
mpl.rcParams['legend.labelspacing'] = 0.25
mpl.rcParams['legend.handlelength'] = 3

import matplotlib.pylab as plt

"""
1. Read in GDP per capita 
"""
from pandas.io import wb

wb.search('gdp.*capita.*const').iloc[:,:2]
dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], 
                  start=2005, end=2008)
dat['NY.GDP.PCAP.KD'].groupby(level=0).mean()

wb.search('cell.*%').iloc[:,:2]
ind = ['NY.GDP.PCAP.KD', 'IT.MOB.COV.ZS']
dat = wb.download(indicator=ind, country='all', start=2011, end=2011).dropna()
dat.columns = ['gdp', 'cellphone']

"""
2. Read in complete csv (see Sargent-Stachurski)  
"""


#%%
# OLD PLOTS FROM ANOTHER PROGRAM
plt.plot(calls_strikes, calls_mid, 'r', lw=2, label='calls')
#plt.plot(calls_strikes, calls_ask, 'r', lw=2, label='calls ask')
plt.plot(puts_strikes, puts_mid, 'b', lw=2, label='puts')
plt.axis([120, 250, 0, 50])
plt.axvline(x=atm, color='k', linestyle='--', lw=2, label='atm')
plt.xlabel('Strike')               
plt.ylabel('Option Price')
plt.legend(loc='upperleft')

