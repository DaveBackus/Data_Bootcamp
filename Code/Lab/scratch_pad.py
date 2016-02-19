# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:31:33 2016

@author: dbackus
"""
#%%
import pandas as pd
import datetime as dt

print('Pandas version:', pd.__version__)
print('Today:', dt.date.today())

#%%
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2
df = pd.read_csv(url)
print(df)
#print("df is a ", type(df))

#%%
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.xlsx'
url  = url1 + url2
pd.read_excel(url)

