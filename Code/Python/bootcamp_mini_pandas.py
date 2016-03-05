"""
For Class #3 of an informal mini-course at NYU Stern, Fall 2014.

Topics:  pandas data management

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp

Prepared by Dave Backus, Sarah Beckett-Hile, and Glenn Okun
Created with Python 3.4
"""
import pandas as pd

"""
Examples of DataFrames
"""
# 538's income by college major
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/'
url2 = 'data/master/college-majors/recent-grads.csv'
url = url1 + url2
df538 = pd.read_csv(url)

#%%
# check to see what we have
df538.head()        # list first five observations
df538.tail()        # last five
#%%
# look at column names (.tolist() isn't necessary but easier to read)
df538.columns
df538.columns.tolist()

df538.index.tolist()

#%%
# Fama-French equity return data
import pandas.io.data as web
ff = web.DataReader('F-F_Research_Data_Factors', 'famafrench')[0]
ff.columns = ['xsm', 'smb', 'hml', 'rf']

#%%
# constructing a DataFrame from scratch
codes     = ['USA', 'FRA', 'JPN', 'CHN', 'IND', 'BRA', 'MEX']
countries = ['United States', 'France', 'Japan', 'China', 'India',
             'Brazil', 'Mexico']
# Wikipedia, 2013 USD
gdppc = [53.1, 36.9, 36.3, 11.9, 5.4, 15.0, 16.5]  # thousands
gdp   = [16.8, 2.5, 4.7, 16.1, 6.8, 3.0, 2.1]  # trillions

df = pd.DataFrame([gdp, gdppc, countries]).T

#df.columns = ['GDP (trillions of USD)', 'GDP per capita (thousands of USD)',
#              'Country Code']
df.columns = ['gdp', 'gdppc', 'country']
df.index = codes

#%%
# Spencer's version
# Warning:  uses a dictionary, skip if you don't know what that is
data = {"GDP (trillions of USD)": gdp,
        "GDP per capita (thousands of USD)": gdppc,
        "Country": countries}
dfspencer = pd.DataFrame(data, index=codes)

#%%
# Exercise
x = [1, 2, 5, 7, 10]
y = [10, 7, 5, 2, 1]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


"""
Selecting variables and observations
"""
# check
print(df)

some = df[0:3]
print(some)

keep_obs = [0, 1] #['USA', 'BRA', 'JPN']
keep_var = ['gdp', 'country']
other = df[keep_obs]
print(other)

print(df[0:3])


#%%
"""
Constructing new variables
"""
df.pop = df.gdp/df.gdppc
#%%
df['pop'] = df['gdp']/df['gdppc']
print(df)
