"""
IMF, World Economic Outlook database.
Program reads in the whole thing and arranges it for easy use.

Links
Collection:  https://www.imf.org/external/ns/cs.aspx?id=28
April 2015:  http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/index.aspx

Prepared for Data Bootcamp course at NYU
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, August 2015
Created with Python 3.4
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
url1 = 'http://www.imf.org/external/pubs/ft/weo/2015/02/weodata/'
url2 = 'WEOOct2015all.xls'
url = url1 + url2
weo = pd.read_csv(url, sep='\t', thousands=',', na_values=['n/a', '--'])

print('\nWEO database read, dimensions (rows, columns) =', weo.shape)
print('Variable dtypes:\n', weo.dtypes, sep='')

#weo.head().to_csv('weo_head.csv', index=False)

#%%
"""
Create dfs for country codes and variable definitions
"""
country_guide  = weo[['ISO', 'Country']].drop_duplicates().set_index('ISO')

variable_guide = weo[['WEO Subject Code',
                      'Subject Descriptor',
                      'Subject Notes']
                      ].drop_duplicates().set_index('WEO Subject Code')

variable_guide

#%%
"""
time series plots:  one series, multiple countries
"""
variables = ['GGXWDG_NGDP']
countries = ['ARG', 'DEU', 'FRA', 'GRC', 'USA']
sub  = weo[weo['ISO'].isin(countries) & weo['WEO Subject Code'].isin(variables)]
some = [3] + list(range(9,44))
sub  = sub[some].set_index('Country').T.dropna()
sub

#%%
"""
time series plots:  one series, multiple countries
"""
vars = {'NGSD_NGDP': 'Saving', 'NID_NGDP': 'Investment',
        'BCA_NGDPD': 'Current Account'}
variables = list(vars)
countries = ['CHN']
sub = weo[weo['ISO'].isin(countries) &
          weo['WEO Subject Code'].isin(variables)]
some = [2] + list(range(9,45))
sub  = sub[some].set_index('WEO Subject Code').T.dropna().rename(columns=vars)
#sub['zero'] = sub['Saving'] - sub['Investment'] - sub['Current Account']

sub.to_excel('China-Saving-Investment.xls', index=False)

#%%
"""
Cross-section scatterplot
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

#%%
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
plt.scatter(np.log(xs['gdppc'])/np.log(2), xs[g[1]],
            s=100*xs['gdp']**(1/2), alpha=0.35)
#plt.scatter(sub1[g[0]], sub1[g[1]], s=100*sub1['gdp']**(1/2), alpha=0.25)
plt.xlim(8, 18)
plt.ylim(-2, 12)
#plt.hlines(0, xmin, xmax, colors='k')
plt.title('GDP growth versus starting point', fontsize=14, loc='left')
plt.xlabel('Per Capita GDP (2000, log2 scale)')
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
