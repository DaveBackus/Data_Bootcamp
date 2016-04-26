"""
Adelaide Wine data 
https://www.adelaide.edu.au/wine-econ/databases/

Written by Dave Backus and Alex Zhong, April 2016
Created with Python 3.5
"""
import sys
import pandas as pd
#import matplotlib.pyplot as plt

print('\nPython version: ', sys.version)
print('Pandas version: ', pd.__version__, '\n')

url = 'https://www.adelaide.edu.au/wine-econ/papers/Section_I.xlsx'
raw = pd.read_excel(url, 
                    sheetname='Table 1', 
                    skiprows=1, 
                    header=[0,1,2],    # sets column labels
                    parse_cols=[1]+list(range(3,14)),
                    na_values=['na']
                    )

print('Dimensions of raw data:', raw.shape)
print('Variable dtypes:\n', raw.dtypes, sep='')

#%%
# splice variable names together (list of 3-tuples -> list) 
df = raw.copy()
names = list(df)
df.columns = [name[0]+name[1]+name[2] for name in names]

# name index 
df.index.name = 'Country'

# drop rows with NaN index 
df = df.reset_index('Country')
df = df[df['Country'].notnull()]

print('Dimensions after dropping bad rows:', df.shape)

# optional:  drop subtotal columns
#df = df[~df['Country'].str.startswith('Total')]

# set the index as Country 
df = df.set_index('Country')

df = df.astype(float)
df.dtypes

#%%
df[[1]]

