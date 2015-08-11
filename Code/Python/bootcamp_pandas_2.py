"""
Pandas advanced tools for Data Bootcamp course.  

Topics:  reading csv and xls files, properties of dataframes.  

Repository of materials (including this file): 
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python 
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python  

Written by Dave Backus, August 2015 
Created with Python 3.4 
"""
"""
the usual checks 
"""
import sys 
import pandas as pd 

print('\nPython version: ', sys.version) 
print('\nPandas version: ', pd.__version__, '\n') 

"""
Set up simple dataframes to play with 
"""
# create arbitrary dataframe 
gdp = [2, 5, 7, 9]
pop = [9, 6, 3, 10]
cty = ['USA', 'USA', 'FRA', 'FRA']
year = ['2010', '2011', '2012', '2013']

data = {'gdp': gdp, 'pop': pop, 'cty': cty}
df = pd.DataFrame(data=data, index=year) 
print('Sample dataframe\n', df) 

#%%
what = df.head(2)
print(what) 

#%%
import pandas as pd 
# create dataframe with data and structure from WEO 
variable = ['emp', 'emp', 'pop', 'pop', 'gdppc', 'gdppc']
country  = ['FRA', 'USA', 'FRA', 'USA','FRA', 'USA']
x2013    = [25.8, 142.5, 63.4, 314.4, 32.3, 48.8] 
x2014    = [25.8, 146.3, 63.9, 319.0, 32.2, 50.4]
x2015    = [26.0, 148.7, 64.2, 321.2, 32.5, 51.6] 

# this is a dictionary 
weodata = {'country': country, 'variable': variable, 
           '2013': x2013, '2014': x2014, '2015': x2015}
weo = pd.DataFrame(data=weodata) 
print('WEO-like dataframe\n', weo)

#%%
# whip into shape:  version #1  
wsi = weo.set_index(['variable', 'country'])
print('\nSet index version:\n', wsi)

wsr = wsi.reset_index(level='country')
print('\nReset:\n', wsr)

wsit = wsi.T
print('\nTransposed:\n', wsit)

#%%

# whip into shape:  version #2  
wsi = weo.set_index(['variable', 'country'])
print('\nSet index version:\n', wsi)

wu = wsi.unstack()
print('\nUnstacked:\n', wu)

#%%
"""
zip
"""
l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']
d = dict(zip(l1, l2))


#%%
"""
groupby 
"""
g = df.groupby('cty').size()        # not the best example of this


#%%
"""
.set_index and .reset_index 
"""
df1 = df.set_index('cty', append=True)      # or inplace=True 
print(df1) 

df2 = df1.reset_index('cty')
print(df2)

#%%
"""
.stack and .unstack 
"""

dfu = df.unstack()
dfs = df.stack()