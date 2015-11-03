"""
IMF, World Economic Outlook database.
Program reads in the whole thing and arranges it for easy use.  

Labels 
    ISO = 3-letter country code 
    WEO Subject Code = variable code 

Links
Collection:  https://www.imf.org/external/ns/cs.aspx?id=28
April 2015:  http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/index.aspx  

Written by Dave Backus, August 2015 
Created with Python 3.4 
"""
"""
1. Read in data 
"""
"""
Check versions 
"""
import sys 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

print('\nPython version: ', sys.version) 
print('\nPandas version: ', pd.__version__) 

"""
Read data 
NB:  missing value list is critical, otherwise it doesn't recognize numbers 
Also:  file is tab-delimited, not xls, despite its name 
"""
url1 = 'http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/'
url2 = 'WEOApr2015all.xls'
url = url1 + url2 
weo = pd.read_csv(url, sep='\t', thousands=',', na_values=['n/a', '--']) 

print('\nWEO database read, dimensions (rows, columns) =', weo.shape) 
print('Variable dtypes:\n', weo.dtypes, sep='') 

#%%
"""
Create dictionaries for country codes and variable definitions 
"""
varlist = ['ISO', 'Country']
cty_dict = weo[varlist].drop_duplicates().set_index('ISO').to_dict()['Country']

# ** sorting https://docs.python.org/3.4/tutorial/datastructures.html#dictionaries
print('\nCountry codes and names')
for key, value in cty_dict.items():
    print(key, ': ', value, sep='')

varlist = ['WEO Subject Code', 'Subject Descriptor']
var_dict = weo[varlist].drop_duplicates().set_index(varlist[0]).to_dict()[varlist[1]]

print('\nCountry codes and names')
for key, value in var_dict.items():
    print(key, ': ', value, sep='')

# =============================================================================
#%%
"""
2. Cross-section scatterplot
Per capita GDP growth, 2000-15 v 1985-2000  
"""
# growth rate data
vlist = ['PPPPC']
xs = weo[weo['WEO Subject Code'].isin(vlist)].set_index('ISO')

# compute 15-year growth rates 
g = ['g8500', 'g0015']
xs[g[0]] = 100*(np.log(xs['2000']) - np.log(xs['1985']))/15 
xs[g[1]] = 100*(np.log(xs['2015']) - np.log(xs['2000']))/15 

# drop unnecessary variables, drop missing values, and sort   
xs = xs[g].dropna().sort_index()

# other data:  base-year gdp and gdp per capita  
base = '2000'
xs['gdppc'] = weo[weo['WEO Subject Code'] == 'PPPPC'].set_index('ISO')[base]
xs['gdp'] = weo[weo['WEO Subject Code'] == 'PPPSH'].set_index('ISO')[base]

# some stats
print('\nStatistics for growth rates')
print('\n', xs.describe(), sep='')
print('\n', xs.corr(), '\n', sep='')

# scatterplot 
plt.scatter(xs[g[0]], xs[g[1]], alpha=0.5) 
#plt.scatter(xs[g[0]], xs[g[1]], s=75*xs['gdp'], alpha=0.35) 
#plt.scatter(sub1[g[0]], sub1[g[1]], s=100*sub1['gdp']**(1/2), alpha=0.25) 
plt.plot(xs[g[0]], xs[g[0]], 'k--', lw=0.5)
plt.xlim(-6, 12)
plt.ylim(-2, 12)
plt.xlabel('Per Capita GDP Growth, 1985-2000')
plt.ylabel('Per Capita GDP Growth, 2000-2015')
plt.show()

#%%
# another one, growth v level 
#plt.scatter(sub1[g[0]], sub1[g[1]], alpha=0.5) 
plt.scatter(np.log(xs['gdppc']), xs[g[1]], s=75*xs['gdp']**(1/2), alpha=0.35) 
#plt.scatter(sub1[g[0]], sub1[g[1]], s=100*sub1['gdp']**(1/2), alpha=0.25) 
plt.xlim(6, 12)
plt.ylim(-2, 12)
plt.hlines(0, 6, 12, colors='k')
plt.xlabel('Per Capita GDP (2000, log scale)')
plt.ylabel('Per Capita GDP Growth, 2000-2015')
plt.show()


#%%
# =============================================================================
"""
3. Time series plots 
"""
"""
Rearrange so that columns are variables labeled by variable and country code 
"""
# select desired countries and variables by their codes 
clist = ['USA', 'FRA', 'CHN', 'IND', 'BRA', 'MEX']
vlist = ['PPPPC']

subset = weo[(weo['ISO'].isin(clist)) & 
             (weo['WEO Subject Code'].isin(vlist))]

#%%
# kill some columns 
years = [year for year in range(1980, 2016)]
years_str = [str(year) for year in years]
varlist = ['WEO Subject Code', 'ISO'] + years_str
sub = weo[varlist]

# transpose data
sub = sub.set_index(['WEO Subject Code', 'ISO']).T
sub.index = years

# now do bar chart of GDP per capita 