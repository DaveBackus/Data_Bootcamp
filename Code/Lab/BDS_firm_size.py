"""
Business Dynamics Statistics (BDS) from the US Census

Links
* http://www.census.gov/ces/dataproducts/bds/data.html
* http://www.census.gov/ces/dataproducts/bds/data_firm.html
* http://www.census.gov/ces/pdf/BDS_2013_Codebook.pdf
* http://fivethirtyeight.com/features/the-next-amazon-or-apple-or-ge-is-probably-failing-right-now/ 
* https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr707.pdf

Prepared for Data Bootcamp course at NYU
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, February 2016
Created with Python 3.5
"""
import sys
import pandas as pd
#import matplotlib.pyplot as plt

print('\nPython version: ', sys.version)
print('Pandas version: ', pd.__version__, '\n')

#%%
"""
firm sizes 
"""
url = 'http://www2.census.gov/ces/bds/firm/bds_f_sz_release.csv'
raw = pd.read_csv(url)

print('\nDataframe dimensions:', raw.shape)
print('\nVariables and dtypes:\n', raw.dtypes, sep='')
#print('Firm size categories:\n', fsz['fsize'].head(12), sep='')

# clean up size labels
# http://pandas.pydata.org/pandas-docs/stable/text.html#splitting-and-replacing-strings
#raw['fsize'] = raw['fsize'].str.split(n=1).str[1]
#print('\nEdited firm size categories:\n', raw['fsize'].head(12), sep='')

#%%
"""
# exam data
d13 = raw[raw['year2']==2013][['fsize', 'Firms', 'Emp']]
d13.to_dict('list')
"""


#%%
"""
year2 = date
fsize = size category
Firms = number of firms in category
firmdeath_firms = number of exits
"""
# take last two years to play with
fsz = raw[raw['year2'] >= 2012]
fsz = fsz[['year2', 'fsize', 'Firms']]
fsz['Firms'] = fsz['Firms']/10**6
fsz

#%%
fszp = fsz.pivot('fsize', 'year2', 'Firms')
fszp.plot(kind='barh')


#%%
print('\nColumn labels\n', fsz.columns, sep='')
print('\nRow labels\n', fsz.index, sep='')

#%%
fsz.plot()

#%%
# =============================================================================
"""
firm ages
"""
url = 'http://www2.census.gov/ces/bds/firm/bds_f_age_release.csv'
raw = pd.read_csv(url)

print('\nDataframe dimensions:', raw.shape)
print('\nVariables and dtypes:\n', raw.dtypes, sep='')
#print('Firm size categories:\n', fsz['fsize'].head(12), sep='')

#%%
# clean up size labels
# http://pandas.pydata.org/pandas-docs/stable/text.html#splitting-and-replacing-strings
raw['fsize'] = raw['fsize'].str.split(n=1).str[1]
#print('\nEdited firm size categories:\n', raw['fsize'].head(12), sep='')

#%%
"""
year2 = date
fsize = size category
Firms = number of firms in category
firmdeath_firms = number of exits
"""
fsz = raw[raw['year2'] >= 2012]
fsz = fsz.set_index(['year2', 'fsize'])
fsz = fsz['Firms']/10**6
fsz

