"""
Messing around with World Bank data.

Prepared for the NYU Course "Data Bootcamp."
More at https://github.com/DaveBackus/Data_Bootcamp

NIPA codes
General government final consumption expenditure (current LCU)	NE.CON.GOVT.CN
Household final consumption expenditure, etc. (current LCU)	NE.CON.PETC.CN
Household final consumption expenditure (current LCU)	NE.CON.PRVT.CN
Final consumption expenditure, etc. (current LCU)	NE.CON.TETC.CN
Final consumption expenditure (current LCU)	NE.CON.TOTL.CN
Gross national expenditure (current LCU)	NE.DAB.TOTL.CN
Exports of goods and services (current LCU)	NE.EXP.GNFS.CN
Gross fixed capital formation, private sector (current LCU)	NE.GDI.FPRV.CN
Gross fixed capital formation (current LCU)	NE.GDI.FTOT.CN
Changes in inventories (current LCU)	NE.GDI.STKB.CN
Gross capital formation (current LCU)	NE.GDI.TOTL.CN
Imports of goods and services (current LCU)	NE.IMP.GNFS.CN
External balance on goods and services (current LCU)	NE.RSB.GNFS.CN
GDP (current LCU)	NY.GDP.MKTP.CN
Discrepancy in expenditure estimate of GDP (current LCU)	NY.GDP.DISC.CN


http://web.worldbank.org/WBSITE/EXTERNAL/DATASTATISTICS/0,,contentMDK:20451590~isCURL:Y~menuPK:64133156~pagePK:64133150~piPK:64133175~theSitePK:239419~isCURL:Y~isCURL:Y,00.html

References
* http://data.worldbank.org/
* http://pandas.pydata.org/pandas-docs/stable/remote_data.html#world-bank
* http://quant-econ.net/pandas.html

Written by Dave Backus @ NYU, September 2014
Created with Python 3.4
"""
import pandas.io.data as web
from pandas.io import wb
import datetime as dt

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = 6, 4.5  # default is 6, 4
mpl.rcParams['legend.fontsize'] = 10
mpl.rcParams['legend.labelspacing'] = 0.25
mpl.rcParams['legend.handlelength'] = 3

import matplotlib.pylab as plt



"""
1. Read in GDP and expenditure components from World Bank
"""
country_list  = ['CN']
variable_list = ['NE.CON.GOVT.CN', 'NE.CON.PETC.CN', 'NE.CON.PRVT.CN',
                 'NE.CON.TETC.CN', 'NE.CON.TOTL.CN',
                 'NE.DAB.TOTL.CN',
                 'NE.EXP.GNFS.CN', 'NE.GDI.FTOT.CN', 'NE.GDI.STKB.CN',
                 'NE.GDI.TOTL.CN', 'NE.IMP.GNFS.CN', 'NE.RSB.GNFS.CN',
                 'NY.GDP.MKTP.CN', 'NY.GDP.DISC.CN']
df = wb.download(indicator=variable_list, country=country_list,
                 start=1990, end=2014)

# simplify variable names
# http://stackoverflow.com/questions/11346283/renaming-columns-in-pandas
nicknames = {'NE.CON.GOVT.CN': 'g', 'NE.CON.PETC.CN': 'c1',
             'NE.CON.PRVT.CN': 'c2', 'NE.CON.TETC.CN': 'c3',
             'NE.CON.TOTL.CN': 'c4',
             'NE.DAB.TOTL.CN': 'a', 'NE.EXP.GNFS.CN': 'x',
             'NE.GDI.FTOT.CN': 'i', 'NE.GDI.STKB.CN': 'v',
             'NE.GDI.TOTL.CN': 'gcf', 'NE.IMP.GNFS.CN': 'm',
             'NE.RSB.GNFS.CN': 'nx',
             'NY.GDP.MKTP.CN': 'y', 'NY.GDP.DISC.CN': 'disc'}
df = df.rename(columns=nicknames)

#%%
"""
2. Check that things add up
All set as long as we include the statistical discrepancy
"""

check_iv = df['i'] + df['v'] - df['gcf']            # ok
check_nx = df['x'] - df['m'] - df['nx']             # ok

check_c1 = df['g'] + df['c1'] - df['c4']            # ok
check_c2 = df['g'] + df['c2'] - df['c4']            # exact

check_a1 = df['c4'] + df['gcf'] - df['a']           # ok
check_a2 = df['c2'] + df['g'] + df['gcf'] - df['a'] # ok

check_y1 = df['c2'] + df['g'] + df['gcf'] + df['nx'] - df['y']  # ok
check_y2 = df['c2'] + df['g'] + df['gcf'] + df['nx'] + df['disc'] - df['y']

#%%
"""
3. Plot expenditure shares, saving and investment
"""
cy  = df['c2']/df['y']
iy  = df['gcf']/df['y']
gy  = df['g']/df['y']
nxy = df['nx']/df['y']
sy  = (df['y']-df['c2']-df['g'])/df['y']

#%%

plt.plot(calls_strikes, calls_mid, 'r', lw=2, label='calls')
#plt.plot(calls_strikes, calls_ask, 'r', lw=2, label='calls ask')
plt.plot(puts_strikes, puts_mid, 'b', lw=2, label='puts')
plt.axis([120, 250, 0, 50])
plt.axvline(x=atm, color='k', linestyle='--', lw=2, label='atm')
plt.xlabel('Strike')
plt.ylabel('Option Price')
plt.legend(loc='upperleft')

