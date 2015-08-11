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
Check versions 
"""
import sys 
import pandas as pd 

print('\nPython version: ', sys.version) 
print('\nPandas version: ', pd.__version__) 

url = 'http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/WEOApr2015all.xls'
weo = pd.read_csv(url, sep='\t', thousands=',')   # tab = \t 

print('\nDatabase read, dimensions are ', weo.shape)

#%%
"""
Create country and variable dictionaries 
"""
varlist = ['ISO', 'Country']
country_dict = weo[varlist].drop_duplicates().set_index('ISO').to_dict()

varlist = ['WEO Subject Code', 'Subject Descriptor']
variable_dict = weo[varlist].drop_duplicates().set_index(varlist[0]).to_dict()

#%%
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
