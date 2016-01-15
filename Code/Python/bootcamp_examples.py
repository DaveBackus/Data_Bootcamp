"""
Examples for Data Bootcamp course (data input and graphics)

**Warning**
Web data access will change in the near future, when Pandas spins
off the web access tools into a new package.
http://pandas.pydata.org/pandas-docs/stable/remote_data.html

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp

Written by Dave Backus, November 2015
Created with Python 3.5
"""
"""
Check versions (ignore this)
"""
import pandas as pd      # the data package
import sys

print('\nPython version:', sys.version)
print('Pandas version: ', pd.__version__)

#%%
"""
Example:  World Bank country indicators
* NY.GDP.PCAP.PP.KD = gdp per capita
* NY.GDP.MKTP.PP.KD = gdp
* SE.ADT.LITR.ZS    = adult literacy (%)
* SP.DYN.LE00.IN    = life expectancy
* IT.CEL.SETS.P2    = cell phone penetration (per 100)
See:  http://data.worldbank.org/
"""
# load packages (redundancy is ok)
import pandas as pd                # data management tools
from pandas.io import wb           # World Bank api
import matplotlib.pyplot as plt    # plotting tools

# variable list
var = ['NY.GDP.PCAP.PP.KD', 'NY.GDP.MKTP.PP.KD', 'SP.DYN.LE00.IN']
# country list (ISO codes)
iso = ['USA', 'FRA', 'JPN', 'CHN', 'IND', 'BRA', 'MEX']
year = 2013
df = wb.download(indicator=var, country=iso, start=year, end=year)

# massage data
df = df.reset_index(level='year', drop=True)
df.columns = ['gdppc', 'gdp', 'le']    # rename variables
df['gdp'] = df['gdp']/10**12           # convert to trillions
df['gdppc'] = df['gdppc']/10**3        # convert to thousands
df['order'] = [5, 3, 1, 4, 2, 6, 0]    # reorder countries
df = df.sort(columns='order', ascending=False)

# GDP bar chart
ax = df['gdp'].plot(kind='barh', alpha=0.5)
ax.set_title('GDP', loc='left', fontsize=14)
ax.set_xlabel('Trillions of US Dollars')
ax.set_ylabel('')

#%%
# ditto for GDP per capita (per person)
ax = df['gdppc'].plot(kind='barh', color='m', alpha=0.5)
ax.set_title('GDP Per Capita', loc='left', fontsize=14)
ax.set_xlabel('Thousands of US Dollars')
ax.set_ylabel('')

#%%
# scatterplot of life expectancy vs gdp per capita
plt.scatter(df['gdppc'], df['le'], s=50*df['gdp'],
            cmap=plt.get_cmap(name='Spectral'), alpha=0.5)   # cmap irrelevant
plt.title('Life expectancy vs. GDP per capita', loc='left', fontsize=14)
plt.xlabel('GDP Per Capita')
plt.ylabel('Life Expectancy')
#plt.annotate(x=iso, xy=(df['gdppc'], df['le']))

#%%
"""
Example:  US GDP and GDP growth from FRED
"""
import pandas.io.data as web           # web interface for FRED
import datetime as dt                  # handles dates
import matplotlib.pyplot as plt        # plotting

fred_series = ['GDPC1']                                       # the real GDP code for FRED
start_date = dt.datetime(1960, 1, 1)
fred = web.DataReader(fred_series, 'fred', start_date)/10**3  # convert to trillions of USD
# print last 3 data points to see what we've got (quarterly data)
print(fred.tail(3))

# plot GDP over time
ax = fred.plot(legend=False)
ax.set_title('US Real GDP', fontsize=14, loc='left')
ax.set_xlabel('')
ax.set_ylabel('Trillions of Chained US Dollars')
ax.legend().set_visible(False)

#%%
# quarterly growth rates
g = fred.pct_change()*400               # 400 makes this an annual percentage
print(g.tail(3))
# change label
g.columns = ['US GDP Growth']
gbar = g.mean()

# plot growth rates
start = dt.datetime(1985, 1, 1)
end = g.index[-1]
ax = g[g.index >= start].plot(kind='line')
ax.set_title('US Real GDP Growth', fontsize=14, loc='left')
ax.hlines(y=gbar, xmin=start, xmax=end)
ax.hlines(y=0, xmin=start, xmax=end, linestyles='dashed')
ax.legend().set_visible(False)

#%%
"""
Example:  US economic indicators (monthly data from FRED)
* INDPRO:   industrial production
* PAYEMS:   nonfarm employment
* AWHMAN:   average weekly hours worked in manufacturing
* PERMIT:   premits for new housing
* NAPM:     purchasing managers index
"""
import pandas.io.data as web           # web interface with FRED
import pandas as pd                    # data manipulation
import datetime as dt                  # handles dates

# list of indicators (FRED codes)
indicators = ['INDPRO', 'PAYEMS', 'AWHMAN', 'PERMIT', 'NAPM']
start_date = dt.datetime(1970, 1, 1)
inds = web.DataReader(indicators, "fred", start_date)
print(inds.tail(3))

# yoy growth rates
g = inds.pct_change(periods=12).dropna()
# standardize
g_std = (g - g.mean()) / g.std()

# plot
ax = g_std.plot()
ax.set_title('Various economic indicators', fontsize=14, loc='left')
#ax.set_ylabel('Standard deviations from mean')
ax.set_xlabel('')
ax.hlines(y=[-1, 0, 1], xmin=start_date, xmax=end, linestyles='dashed')
ax.legend().set_visible(False)

#%%
"""
Government debt:  IMF historical data
Thanks to Itamar Snir
"""
import pandas as pd
import matplotlib.pyplot as plt

# data input
excelFilePath = '../Temp/Debt Database Fall 2013 Vintage.xlsx'
df = pd.read_excel(excelFilePath, sheetname=1, na_values=['…', '….', ''])
    #, index_col=-1, encoding='utf-8')

#%%
#get most recent year in the data (instead of 2013):
max_year = max(df.columns.values[4:].tolist())

#get a list of the years for the x-axis values
years = [year for year in range(1980,max_year+1)]
#get a list of the debt to GDP for the y-axis values
dbt_greece = df[df.country=='Greece'][years]
dbt_greece_list = dbt_greece.values.tolist()[0]
#plot the data
plt.plot(years,dbt_greece_list, color='red') #set graph color
plt.ylabel('Debt to GDP')
plt.title ('Greece Debt to GDP Between 1980 and '+ str(max_year))
plt.show()

#%%
"""
US bond yields
Video?
"""


#%%
"""
Example:  Stock prices from Yahoo finance (VIX)
"""
import pandas as pd
import pandas.io.data as web
import datetime as dt

# ticker
ticker = 'aapl'
today = dt.date.today()
#one_week = dt.timedelta(days=7)
#start = today - one_week
start = dt.datetime(2000, 1, 1)
vix = web.DataReader(ticker, 'yahoo', start)

ax = vix['Close'].plot()
ax.set_xlabel('')

#%%
"""
Example:  Fama-French stock returns
* xsm = excess return on market (market minus riskfree rate)
* smb = return on small firms minus return on big firms
* hml = return on high book-to-market firms minus low
* rf  = riskfree rate
All returns are monthly percentages
"""
import pandas.io.data as web

ff = web.DataReader('F-F_Research_Data_factors', 'famafrench')[0]
ff.columns = ['xsm', 'smb', 'hml', 'rf']

ff.describe

# plots of mean and std
ffbar = ff.mean()
ffstd = ff.std()

ff.plot(kind='kde', subplots=True)

#fig, ax = plt.
#ffbar.plot(kind='barh', alpha=0.5)
#plt.title('Mean returns', fontsize=14, loc='left')
#
#ffstd.plot(kind='barh', alpha=0.5)
#plt.title('Standard deviation of returns', fontsize=14, loc='left')


#%%
"""
Example:  Stock options from Yahoo finance
Currently **broken**:  asks for html5lib, which conflicts with Python 3.5
"""
import pandas as pd
import pandas.io.data as web
from pandas.io.data import Options
import datetime as dt
#import matplotlib.pylab as plt

# ticker
ticker = 'spy'
today = dt.date.today()
one_week = dt.timedelta(days=7)
start = today - one_week
stock = web.DataReader(ticker, 'yahoo', start)
# take the last close (-1 is the last, 'Close' is the close)
atm = stock.ix[-1,'Close']      # the -1 takes the last observation
print('Stock price (at the money): ', atm)

# get option prices for same ticker
option = Options(ticker, 'yahoo')
expiry = dt.date(2016, 2, 19)
#data_calls = option.get_call_data(expiry=expiry).dropna()
#data_puts  = option.get_put_data(expiry=expiry).dropna()

# compute mid of bid and ask and arrange series for plotting
calls_bid = data_calls['Bid']
calls_ask = data_calls['Ask']

calls_strikes = data_calls['Strike']
calls_mid = (data_calls['Bid'] + data_calls['Ask'])/2
puts_strikes = data_puts['Strike']
puts_mid = (data_puts['Bid'] + data_puts['Ask'])/2

# plot call and put prices v strike
plt.plot(calls_strikes, calls_mid, 'r', lw=2, label='calls')
plt.plot(puts_strikes, puts_mid, 'b', lw=2, label='puts')

# prettify it
#plt.axis([120, 250, 0, 50])
plt.axvline(x=atm, color='k', linestyle='--', label='ATM')
plt.legend(loc='best')
plt.show()

