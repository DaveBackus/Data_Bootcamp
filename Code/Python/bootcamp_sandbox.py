"""
Miscellaneous experiments for Data Bootcamp course.  

Repository of materials (including this file): 
* https://github.com/DaveBackus/Data_Bootcamp/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python  

Written by Dave Backus, March 2015  
Created with Python 3.4 
"""
print('\nWelcome to Data Bootcamp!')

import datetime as dt 
print('Today is', dt.date.today())

"""
Check Python version 
"""
import sys

print('\nWhat version of Python are we running? \n', sys.version, '\n', sep='') 

if float(sys.version_info[0]) < 3.0:       
    raise Exception('Program halted, old version of Python. ' +  
                    'Sorry, you need to install Anaconda again.')
else:
    print('Congratulations, Python is up to date!')  
#    sys.exit(0)      # this halts execution

#%%    
"""
Assignments and copies 
http://stackoverflow.com/questions/10844493/dataframe-apply-in-python-pandas-alters-both-original-and-duplicate-dataframes
"""
# check 1
a = [1,2,3]
b = a
b[0] = 'WHOA!'
print('\nAfter assignment, a is', a)

# to make a copy 
a = [1,2,3]
b = a.copy()
b[0] = 'WHOA!' 
print('\nAfter copy, a is', a) 

# check 2
import numpy as np 
c = np.array([7, 3, 5]) 
d = c 
e = 2*c - 5
print('\nAfter assignment, (d, e) are', d, e)

c[0] = 10
print(d, e)

#%%    
"""
Check path of current working directory (just for the heck of it)  
"""
# https://docs.python.org/2/library/os.path.html
import os 

print('\nCurrent path:\n', os.getcwd(), sep='') 

"""
Check for specific file 
""" 
import os

print('\nList of files in working directory:')
[print(file) for file in os.listdir()]

file = 'SQL_support_code.py'
if not os.path.isfile(file):
    raise Exception('***** Program halted, file missing *****')
    
#%%    
"""
IMF's historical database on public debt 
https://www.imf.org/External/pubs/cat/longres.aspx?sk=24332.0
rows are countries, columns are dates (1692-2012) 
"""
import pandas as pd 
import urllib              # handles internet files 
import zipfile             # handles zip files 
import os 

# copy zip file to hard drive 
print('\nCopy IMF historical debt data to hard drive')
url = 'https://www.imf.org/external/pubs/ft/wp/2010/Data/wp10245.zip'
zname = '../Temp/' + os.path.basename(url)   # strip out file name 
urllib.request.urlretrieve(url, zname)       # copy file from url to disk 

# extract spreadsheet
zf = zipfile.ZipFile(zname, 'r')
zf.printdir()
xlsname = zf.namelist()[0]
xls = zf.extract(xlsname)

df = pd.read_excel(xls, sheetname=1, na_values=['…', '….', ''], index_col=0, 
                   encoding='utf-8') 

print('Type: ', type(df))
print('Shape (dimensions): ', df.shape)
print('Column labels (variables): ', df.columns.tolist()) 
print('Variable types: \n', df.dtypes, sep='')

#%%
# select years 1980 to 2013 and ifscode 
years = [year for year in range(1980, 2013)]
years_str = [str(year) for year in years]
vars = ['ifscode'] + years

some = df[vars]



#%%
"""
# manual version 
xlsfile = 'Debt Database Fall 2013 Vintage.xlsx'
df = pd.read_excel('../Temp/' + xlsfile, sheetname=1) 
"""
# ok, some legit ways 

#%%
"""
urrlib version:  the hard way relative to Pandas 
"""
# copy file from url to hard drive 
import urllib.request           
file = 'foo.csv'
url1 = 'https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/'
url2 = 'Code/Data/test1.csv'
url = url1 + url2 
urllib.request.urlretrieve(url, file)

# Sarah's version 
f = urllib.request.urlopen(url)
file = 'foo_sbh.csv'
with open(file, 'wb') as local_file:
    local_file.write(f.read())

#%%
"""
World Bank WDI from zip file 
File is too big, takes too long to read (but has great stuff!) 
"""
import pandas as pd
import urllib
import zipfile
import os 

# this is a big file, best to test with something smaller 
url  = 'http://databank.worldbank.org/data/download/WDI_csv.zip'
file = '../Temp/' + os.path.basename(url)   # strip out file name 
urllib.request.urlretrieve(url, file)        # copy to disk 

# see what's there
print(['Is zipfile?', zipfile.is_zipfile(file)])
zf = zipfile.ZipFile(file, 'r')
#print('List of zipfile contents (two versions)')
zf.printdir()

# extract a component 
csv = zf.extract('WDI_Data.csv')        # copy to disk  
df1 = pd.read_csv(csv)       # read
print(df1.columns)                      # check contents 

# alternative:  open and read
csv = zf.open('WDI_Data.csv')
df2 = pd.read_csv(csv)
print(df2.columns)




