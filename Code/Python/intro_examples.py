"""
Examples of the practical possibilities of using Python with economic 
and financial data.  Apps:  
* US GDP growth via FRED 
* GDP per capita in a set of countries via World Bank  
* Fama-French US equity factors via French
* Stock options via Yahoo 
* csv data [??]

Cells are designed to be run independently, which means we have some
redundant package imports.  

Prepared for the NYU Course "Data Bootcamp."  More at 
* https://github.com/DaveBackus/Data_Bootcamp 
We'll give references to the applications along the way.  

Written by Dave Backus @ NYU, August 2014  
Created with Python 3.4 
"""
"""
1. Read in US real GDP from FRED (code GDPC1)

References 
* http://research.stlouisfed.org/fred2/ 
* http://pandas.pydata.org/pandas-docs/stable/ 
* http://pandas.pydata.org/pandas-docs/stable/remote_data.html#fred 
* 
"""
import datetime as dt 
import 
import matplotlib.pyplot as plt

# get data from FRED
fred_series = ["GDPC1"]
start = dt.datetime(1985, 1, 1)
data = web.DataReader(fred_series, "fred", start)
print(data.tail())                  # to see what we've got

# extract most recent n quarters  
nqtrs = 8
recent = data[-1:-8, :]

#%%
# growth rates and stats 
g = data.pct_change()
print(["Mean and std", g.mean(), g.std()])

#g.plot()
#g.hist()

# pyplot apps
gp  = g.ix[1:,0]
gfx = g.ix[1:,1]

gp.plot()

plt.figure()
acf_gp = plt.acorr(gp, maxlags=60)
plt.show()

#%%
"""
2. GDP per capita in selected countries from World Bank 

References 
* http://data.worldbank.org/
* http://pandas.pydata.org/pandas-docs/stable/remote_data.html#world-bank  
* http://quant-econ.net/pandas.html#data-from-the-world-bank
"""
import pandas as pd
from pandas.io import wb
#import numpy as np

# http://www.worldatlas.com/aatlas/ctycodes.htm
country_list = ['US', 'FR', 'JP', 'CN', 'IN', 'BR', 'MX']
variable_list = ['NY.GDP.PCAP.KD']
start = 2011
data = wb.download(indicator=variable_list, 
                   country=country_list, start=start, end=start)
print(data.tail())

#%%
"""
3. Fama-French factors from Ken French's website 

References 



#%%
"""
4. Read in Yahoo stock and options prices for SPY (SP 500 "Spyders")  

References
* http://finance.yahoo.com/q?s=spy
* http://pandas.pydata.org/pandas-docs/stable/remote_data.html#yahoo-finance
* http://pandas.pydata.org/pandas-docs/stable/remote_data.html#yahoo-finance-options
"""
import pandas.io.data as web
from pandas.io.data import Options
import datetime as dt 
import matplotlib as mpl
#mpl.rcParams['figure.figsize'] = 6, 4.5  # default is 6, 4
#mpl.rcParams['legend.fontsize'] = 10  
#mpl.rcParams['legend.labelspacing'] = 0.25
#mpl.rcParams['legend.handlelength'] = 3
import matplotlib.pylab as plt

# pick a stock 
ticker = 'spy' 

ticker = 'spy' 

# stock price first (the underlying) 
# pick a recent date and subtract seven days to be sure we get a quote  
# http://pymotw.com/2/datetime/#date-arithmetic
today = dt.date.today()
one_week = dt.timedelta(days=7)
start = today - one_week
stock = web.DataReader(ticker, 'yahoo', start) 
print(stock)                    # to see what we have

# take the last close (that's what the -1 does)
atm = stock.ix[-1,'Close']      # the -1 takes the last observation   

# now get option prices for same ticker 
option = Options(ticker, 'yahoo')
expiry = dt.date(2014, 11, 20)
calls = option.get_call_data(expiry=expiry)
puts  = option.get_put_data(expiry=expiry)
calls.tail                          # to see what we have 
puts.tail 

# get prices and strikes
# prices are midpoint of bid and ask 
calls_strikes = calls['Strike']
calls_mid = (calls['Bid'] + calls['Ask'])/2
puts_strikes = puts['Strike']
puts_mid = (puts['Bid'] + puts['Ask'])/2

# plot calls and puts 
plt.plot(calls_strikes, calls_mid, 'r', lw=2, label='calls')
plt.plot(puts_strikes, puts_mid, 'b', lw=2, label='puts')

# add some things to dress up the fig: type plt. [tab] for options
plt.axis([140, 240, 0, 50])          
plt.ylabel('Option Price')      
plt.xlabel('Strike Price')
plt.text(125, 4, today)  
# vertical line to mark price of underlying ("at-the-money")           
plt.axvline(x=atm, color='k', linestyle='--', label='ATM')               
plt.legend(loc='upperleft', handlelength=3)
plt.savefig('optionprices.pdf')

#%%
"""
5. Read data in csv format (what??) 

References 
* 
"""


