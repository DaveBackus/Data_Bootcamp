# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 14:56:42 2014

@author: sarahbeckett-hile
"""

"""
For Class #1 of an informal mini-course at NYU Stern, Fall 2014.

Repository of materials (including this file): 
* https://github.com/DaveBackus/Data_Bootcamp 

Prepared by Dave Backus, Sarah Beckett-Hile, and Glenn Okun 
Created with Python 3.4 
"""

"""
Calculations and assignments (best in IPython console)   
"""
x = 2*3 
y = 2**3 
z = 2/3 

"""
Strings  
"""
a = 'some'
b = 'thing'
c = a + b 
print(['a[1:3]', a[1:3]])

# names 
first, last = 'Dave', 'Backus'
full = first + ' ' + last

"""
Lists 
"""
numbers = [x, y, z]
strings = [a, b, c]

all = numbers + strings
print(['all[3:]', all[3:]])

#%%
"""
Inputting data 
"""
import pandas as pd 

# read from local file  
file = '../Data/test1.csv'
df = pd.read_csv(file)
#%%
# some properties
print(df) 
#%%
print(type(df))
#%%
print(['Shape is', df.shape])
#%%
print(df.mean()) 
#%%
print(df.columns)
#%%
print(['column labels', df.columns])
#%%
print(['row labels', df.index])

#%%
# read from url 
url = 'https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/Data/test1.csv'
dfurl = pd.read_csv(url)

#%%
# read IMF's WEO data from 
url = 'http://www.imf.org/external/pubs/ft/weo/2014/01/weodata/WEOApr2014all.xls'
weo = pd.read_csv(url, sep='\t')    # tab = \t 
print(weo.head())
print(['column labels', weo.columns])
print(['row labels', weo.index])

#%%
# copy file from url to hard drive 
import urllib.request           # this is a module from the package urllib 
file = 'foo.csv'
url = 'https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/Data/test1.csv'
urllib.request.urlretrieve(url, file)

#%%
# Sarah's version 
f = urllib.request.urlopen(url)
file = 'foo_sbh.csv'
with open(file, 'wb') as local_file:
    local_file.write(f.read())

#%%
# read from xls 
file = '../Data/test2.xlsx'
xls = pd.read_excel(file)       # default is first sheet

#%%
# zip files 
import pandas as pd
import urllib
import zipfile
import os 

# this is a big file, best to test with something smaller 
url  = 'http://databank.worldbank.org/data/download/WDI_csv.zip'
file = os.path.basename(url)            # strip out file name 
urllib.request.urlretrieve(url, file)   # copy to disk 

# see what's there
print(['Is zipfile?', zipfile.is_zipfile(file)])
zf = zipfile.ZipFile(file, 'r')
print('List of zipfile contents (two versions)')
[print(file) for file in zf.namelist()]
zf.printdir()

# extract a component 
csv = zf.extract('WDI_Data.csv')        # copy to disk  
df1 = pd.read_csv('WDI_Data.csv')       # read
print(df1.columns)                      # check contents 

# alternative:  open and read
csv = zf.open('WDI_Data.csv')
df2 = pd.read_csv(csv)
print(df2.columns)
