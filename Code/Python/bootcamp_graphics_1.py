"""
Matplotlib intro for Data Bootcamp course (graphics)

Three approaches to graphics
* apply plot method to dataframe
* plot(x,y) function
* create figure object, apply plot methods to it

Graphics inherently complicated, see these options to get a sense:
http://matplotlib.org/users/customizing.html

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp

Written by Dave Backus, August 2015
Created with Python 3.5
"""
"""
Check versions
"""
import sys                             # system module
import pandas as pd                    # data package
import matplotlib as mpl               # graphics package

print('\nPython version:', sys.version)
print('Pandas version: ', pd.__version__)
print('Matplotlib version: ', mpl.__version__)

#%%
"""
Datasets
* US GDP and consumption ("personal consumption expenditures")
* Fama-French equity returns
"""
# US GDP and consumption
gdp  = [13271.1, 13773.5, 14234.2, 14613.8, 14873.7, 14830.4, 14418.7,
        14783.8, 15020.6, 15369.2, 15710.3]
pce  = [8867.6, 9208.2, 9531.8, 9821.7, 10041.6, 10007.2, 9847.0, 10036.3,
        10263.5, 10449.7, 10699.7]
year = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]

# create dataframe from dictionary
us = pd.DataFrame({'gdp': gdp, 'pce': pce}, index=year)

# Fama-French
import pandas.io.data as web

# read annual data from website and rename variables
ff = web.DataReader('F-F_Research_Data_factors', 'famafrench')[1]
ff.columns = ['xsm', 'smb', 'hml', 'rf']
ff = ff[['xsm', 'rf']]     # extract xsm and rf

#%%
"""
Approach 1:  apply plot methods to dataframe
"""
# US GDP
us.plot()
us.plot(kind='bar')
us.plot.barh()

# what would you change?
# what other kinds of graphs are available?  use



#%%
"""
Approach 2:  Pyplot's simple (x,y) interface
"""
import matplotlib.pyplot as plt        # pyplot module

#plt.style.use('dark_background')

# Exercise:  try each of these
plt.plot(year, gdp, color='blue', linewidth=2, alpha=0.8)
plt.plot(year, pce, color='magenta', linewidth=2, alpha=0.5)
# comment:  if you do this in the console, it comes out as two sep charts

# dress up the figure
plt.title('US Real GDP and Consumption')
plt.ylabel('Billions of 2009 USD')
plt.legend(('GDP', 'Consumption'), loc=0)   # legend
plt.show()                                  # this closes the plot

# Exercise.  What does linewidth=2 do?  What happens if you change it?

# Exercise.  What does alpha=0.8 do?  What happens if you change it?

# Aside:  a "kwarg" is a "keyword argument" like color="blue" or alpha=0.8
# Use Object explorer to get information about plt.plot, scroll down to kwargs

# Exercise:  change color of lines, add the marker 'o'
# add y-axis text ('Billions of USD'), turn legend off,
# change font of title, left justify it
# suggest other options:  what would make this look better?

#%%
# bar chart version
plt.bar(year, gdp, width=0.8, color='blue', align='center', alpha=0.5)
plt.show()

#%%
"""
Example:  GDP per capita in selected countries
"""
# data
codes     = ['USA', 'FRA', 'JPN', 'CHN', 'IND', 'BRA', 'MEX']
countries = ['United States', 'France', 'Japan', 'China', 'India',
             'Brazil', 'Mexico']
# World Bank data, thousands of 2013 USD, PPP adjusted
gdppc     = [53.1, 36.9, 36.3, 11.9, 5.4, 15.0, 16.5]
other_axis = range(len(gdppc))

# bar chart
plt.bar(other_axis, gdppc, align='center')

# prettify it
plt.xticks(other_axis, codes, fontsize=12)
plt.xlim((-0.75, 6.75))
plt.ylabel('GDP Per Capita (thousands of USD)')
plt.title('GDP Per Capita', fontsize=16, loc='left')
plt.show()

# Exercise.  Make the bars lighter, change color (what would you suggest?)

#%%
# horizontal bars
plt.barh(other_axis, gdppc, align='center', edgecolor='red',
         linewidth=2, alpha=0.75)
plt.ylim((-0.6, 6.6))
plt.yticks(other_axis, countries, fontsize=14)
plt.show()

# Exercise.  What would you do to make this look better?

#%%
"""
Approach 2:  Create figure objects
"""
# repeat import and data
import matplotlib.pyplot as plt             # redundant if already done
gdp  = [13271.1, 13773.5, 14234.2, 14613.8, 14873.7, 14830.4, 14418.7,
        14783.8, 15020.6, 15369.2, 15710.3]
pce  = [8867.6, 9208.2, 9531.8, 9821.7, 10041.6, 10007.2, 9847.0, 10036.3,
        10263.5, 10449.7, 10699.7]
year = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]

# set up a plot
fig, ax = plt.subplots()                    # sets up single plot
print([type(fig), type(ax)])                # see what we have

# add content to the object ax
ax.plot(year, gdp, color='blue', linewidth=2, alpha=0.8)
ax.plot(year, pce, color='magenta', linewidth=2, alpha=0.25)
ax.set_ylim(bottom=0.0)
plt.show(fig)                                  # close plot

# Exercise.  How can I make the y axis start at zero?

#%%
# multiple plots

# object oriented version
fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)

# first figure
ax[0].plot(year, gdp, color='blue', linewidth=2, alpha=0.8)
ax[0].text(2010, 14000, 'GDP')

# second figure
ax[1].plot(year, pce, color='magenta', linewidth=2, alpha=0.8)
ax[1].text(2010, 9200, 'Consumption')

plt.show()                                  # close plot

#%%
"""
Approach 3:  apply methods directly to data
Example:  Fama-French data
"""
import pandas.io.data as web

ff = web.DataReader('F-F_Research_Data_factors', 'famafrench')[0]
ff.columns = ['xsm', 'smb', 'hml', 'rf']

ff.boxplot()
ff.hist(sharex=True, bins=25)


#%%
"""
Bonus material:  "styles" set basic layout parameters
We can set them one at a time, but this is easier
plt.style.available gives options:
['ggplot', 'bmh', 'dark_background', 'fivethirtyeight', 'grayscale']
"""
import pandas as pd                # data management tools
from pandas.io import wb           # World Bank api
import matplotlib.pyplot as plt    # plotting tools

# variable list
var = ['NY.GDP.PCAP.PP.KD', 'NY.GDP.MKTP.PP.KD']
# country list (ISO codes)
iso = ['USA', 'FRA', 'JPN', 'CHN', 'IND', 'BRA', 'MEX']
year = 2014
df = wb.download(indicator=var, country=iso, start=year, end=year)

# massage data
df = df.reset_index(level='year', drop=True)
df.columns = ['gdppc', 'gdp']          # rename variables
df['gdp'] = df['gdp']/10**12           # convert to trillions
df['gdppc'] = df['gdppc']/10**3        # convert to thousands
df['order'] = [5, 3, 1, 4, 2, 6, 0]    # reorder countries
df = df.sort(columns='order', ascending=False)

#%%
plt.style.use('fivethirtyeight')

# GDP bar chart
ax = df['gdp'].plot(kind='barh', alpha=0.5)
ax.set_title('GDP', loc='left', fontsize=14)
ax.set_xlabel('Trillions of US Dollars')
ax.set_ylabel('')
plt.show()

#%%
# reset to default style
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)
# In the console:  %matplotlib inline

