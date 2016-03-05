"""
Calculations with Fama-French equity return data (the so-called "FF factors"):
* xsm = excess return on market
* smb = small minus big portfolio
* hml = high minus low book to market
* rf = riskfree rate (so market = xs + rf)
All returns are monthly percentages, not annualized.

Prepared for the NYU Course "Macroeconomic Foundations for Asset Prices,"
ECO-UB-233.  More at
* https://sites.google.com/site/nyusternmacrofoundations/home
* https://github.com/DaveBackus/MFAP

References
* http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
* http://quant-econ.net/pandas.html
* http://pandas.pydata.org/pandas-docs/dev/remote_data.html#fama-french
* http://pandas.pydata.org/pandas-docs/stable/10min.html#selection

Written by Dave Backus @ NYU, August 2014
Created with Python 3.4
"""
import pandas.io.data as web
from numpy import log, exp
import numpy as np
#import datetime as dt
#import matplotlib.pylab as plt

"""
1. Read in Fama-French factors and compute summary stats
"""
# Read data from Ken French's website (built into pandas)
# produces the dataframe ff
ff = web.DataReader('F-F_Research_Data_Factors', 'famafrench')[0]
# NB:  ff.xs is a conflict
ff.columns = ['xsm', 'smb', 'hml', 'rf']

# see what ff looks like
ff.tail()
ff.head(3)
ff.describe()

# compute summary stats
kappa1 = ff.mean()
kappa2sqrt = ff.std()
gamma1 = ff.skew()
gamma2 = ff.kurtosis() - 3

# Note: \n is a control sequence, starts new line
print('Summary stats for Fama-French factors \n(mean, std, skew, ex kurt)',
      end='\n\n')
print(kappa1, end='\n\n')
print(kappa2sqrt, end='\n\n')
print(gamma1, end='\n\n')
print(gamma2, end='\n\n')

## messing around
#ff.plot()
#ff.hist(bins=20)
#ff.boxplot()

#%%
"""
2. Properties of log excess returns
"""
# Note:  log imported from numpy, otherwise use np.log
ff['lxsm'] = log(1+(ff['xsm']+ff['rf'])/100) - log(1+ff['rf']/100)
ff['lsmb'] = np.log(1+(ff['smb']+ff['rf'])/100) - np.log(1+ff['rf']/100)
ff['lhml'] = np.log(1+(ff['hml']+ff['rf'])/100) - np.log(1+ff['rf']/100)

# select log returns
ffl = ff[['lxsm', 'lsmb', 'lhml']]

# print summary stats
print('Summary stats for log excess returns\n')
print(ffl.mean(), end='\n\n')
print(ffl.std(), end='\n\n')
print(ffl.skew(), end='\n\n')
print(ffl.kurtosis()-3, end='\n\n')

"""
3. Play with dates
"""

#??

