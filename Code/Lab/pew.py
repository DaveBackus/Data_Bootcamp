"""
Messing around with data from Pew Research Center data.

Prepared for the NYU Course "Data Bootcamp."
More at https://github.com/DaveBackus/Data_Bootcamp

References
* http://www.pewresearch.org/category/interactives/
* SPSS data?
http://pic.dhe.ibm.com/infocenter/spssstat/v21r0m0/index.jsp?topic=%2Fcom.ibm.spss.statistics.python.help%2Fpython_package_dataset.htm
??* http://pandas.pydata.org/pandas-docs/stable/remote_data.html#world-bank
??* http://quant-econ.net/pandas.html

Written by Dave Backus @ NYU, September 2014
Created with Python 3.4

Shell program, not written yet!!
"""
import spss ???

#%%
import pandas.io.data as web
import datetime as dt
import matplotlib.pylab as plt


OLD PROGRAM FROM HERE
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

