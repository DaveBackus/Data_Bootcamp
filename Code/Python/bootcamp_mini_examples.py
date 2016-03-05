"""
Examples for Class #1 of an informal mini-course at NYU Stern, Fall 2014.
Examples are
* US GDP growth via FRED
* GDP per capita in a set of countries via World Bank
* Fama-French US equity factors via French
* Stock options via Yahoo (not yet)

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp

Prepared by Dave Backus, Sarah Beckett-Hile, and Glenn Okun
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
import pandas.io.data as web       # data import tools
import matplotlib.pyplot as plt    # plotting tools

# get data from FRED
fred_series = ["GDPC1"]
start = dt.datetime(1985, 1, 1)
data = web.DataReader(fred_series, "fred", start)
print(data.tail())                  # to see what we've got

# compute annualized growth rate, change label, and print stats
g = 4*data.pct_change()
g.columns = ['US GDP Growth']
print(['Mean and std dev', g.mean(), g.std()])

# quick and dirty plot
g.plot()
plt.show()

#%%
"""
2. Fama-French equity factors from Ken French's website

References
* http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
* http://quant-econ.net/pandas.html
* http://pandas.pydata.org/pandas-docs/dev/remote_data.html#fama-french
* http://pandas.pydata.org/pandas-docs/stable/10min.html#selection
* http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.boxplot
* http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.hist.html
"""
# load packages (if it's redundant it'll be ignored)
import pandas.io.data as web

# read data from Ken French's website
ff = web.DataReader('F-F_Research_Data_Factors', 'famafrench')[0]
# NB:  ff.xs is a conflict, rename to xsm
ff.columns = ['xsm', 'smb', 'hml', 'rf']

print(type(ff))

# see what we've got
print(ff.head(3))
print(ff.describe())

# stats
moments = [ff.mean(), ff.std(), ff.skew(), ff.kurtosis() - 3]
print('Summary stats for Fama-French factors (mean, std, skew, ex kurt)') #, end='\n\n')
print(moments)

# some plots
ff.hist(bins=50, sharex=True)
plt.show()

ff.boxplot(whis=0, return_type='axes')
plt.show()

#%%
"""
3. GDP per capita and life expectancy in selected countries (World Bank data)

References
* http://data.worldbank.org/
* http://pandas.pydata.org/pandas-docs/stable/remote_data.html#world-bank
* http://quant-econ.net/pandas.html#data-from-the-world-bank
* http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html
"""
# load packages (ignored if redundant)
# load package under name wb
from pandas.io import wb
import numpy as np
import matplotlib.pyplot as plt

# specify dates, variables, and countries
start = 2011
# GDP per capita, population, life expectancy
variable_list = ['NY.GDP.PCAP.KD', 'SP.POP.TOTL', 'SP.DYN.LE00.IN']
country_list  = ['US', 'FR', 'JP', 'CN', 'IN', 'BR', 'MX']

# Python understands we need to go to the second line because ( hasn't been closed by )
data = wb.download(indicator=variable_list,
                   country=country_list, start=start, end=start).dropna()
# see what we've got
print(data)

# check the column labels, change to something simpler
print(data.columns)
data.columns = ['gdppc', 'pop', 'le']
print(data)

# scatterplot
# life expectancy v GDP per capita
# size of circles controlled by population

plt.scatter(data['gdppc'], data['le'], s=0.000001*data['pop'], alpha=0.5)
plt.ylabel('Life Expectancy')
plt.xlabel('GDP Per Capita')
plt.show()
