"""
Double indexing experiments 

Prepared for Data Bootcamp course at NYU  
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab 

Written by Dave Backus, February 2016 
Created with Python 3.5 
"""
import pandas as pd 

data = {'countrycode': ['CHN', 'CHN', 'CHN', 'FRA', 'FRA', 'FRA', 'USA', 'USA', 'USA'],
 'pop': [1124.8, 1246.8, 1318.2, 58.2, 60.8, 64.7, 253.3, 282.5, 310.4],
 'rgdpe': [2611027.0, 4951485.0, 11106452.0, 1293837.0, 1752570.125, 
           2031723.25, 7964788.5, 11494606.0, 13151344.0],
 'year': [1990, 2000, 2010, 1990, 2000, 2010, 1990, 2000, 2010]}
pwt = pd.DataFrame(data)
pwt

#%%
data = {'countrycode': ['CHN', 'CHN', 'CHN', 'FRA', 'FRA', 'FRA'],
 'pop': [1124.8, 1246.8, 1318.2, 58.2, 60.8, 64.7],
 'rgdpe': [2.611, 4.951, 11.106, 1.294, 1.753, 2.032],
 'year': [1990, 2000, 2010, 1990, 2000, 2010]}
pwt = pd.DataFrame(data)

#%%
pwt2 = pwt.set_index(['countrycode', 'year'])

pwts = pwt.set_index('year')
pwtu = pwt.unstack()
pwts = pwt.stack()

#%%
ax = pwt2.plot()

#%%
pwt2['CHN'].plot()