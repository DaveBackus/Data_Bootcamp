"""
Business Dynamics Statistics (BDS) from the US Census   

Links
* http://www.census.gov/ces/dataproducts/bds/data.html 
* http://www.census.gov/ces/dataproducts/bds/data_firm.html
* http://www.census.gov/ces/pdf/BDS_2013_Codebook.pdf 

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
# read firm size data 
url = 'http://www2.census.gov/ces/bds/firm/bds_f_sz_release.csv'
fsz = pd.read_csv(url) 

print('\nDataframe dimensions:', fsz.shape)
print('\nVariables and dtypes:\n', fsz.dtypes, sep='')
#print('Firm size categories:\n', fsz['fsize'].head(12), sep='') 

# clean up size labels 
# http://pandas.pydata.org/pandas-docs/stable/text.html#splitting-and-replacing-strings
fsz['fsize'] = fsz['fsize'].str.split(n=1).str[1] 
print('\nEdited firm size categories:\n', fsz['fsize'].head(12), sep='') 

#%%
# plot size distributions 

