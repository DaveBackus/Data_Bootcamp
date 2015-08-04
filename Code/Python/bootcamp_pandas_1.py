"""
Pandas intro for Data Bootcamp course.  

Topics:  reading csv and xls files, properties of dataframes.  

Repository of materials (including this file): 
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python 
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python  

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

#%%
"""
Read csv file into dataframe 
Checks first to see if file is in the current working directory
"""
import os 

# some checks just to be cute 
print('\nCurrent working directory: ', os.getcwd())
print('\n List of files in working directory: ', os.listdir())

# check for file 
file = 'test.csv'
if not os.path.isfile(file):
    raise Exception('***** Program halted, csv file not found *****')

# read from local file  
df1 = pd.read_csv(file)

# read from url 
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/foo.csv'
url  = url1 + url2 
df2 = pd.read_csv(url)

#%%
"""
Other datasets 
"""



#%%
"""
Properties of dataframes
"""
df = df1
# some properties
print('\nContents: \n', df) 
print('Type: ', type(df), '\n')
print('Shape: ', df.shape, '\n')
print('Column labels (variables): \n', df.columns)
print('column labels', df.columns)
print('row labels', df.index)
print(df)

#%%
import pandas as pd 
# read IMF's WEO data from 
url = 'http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/WEOApr2015all.xls'
weo = pd.read_csv(url, sep='\t')    # tab = \t 
print(weo.head())
print(['column labels', weo.columns])
print(['row labels', weo.index])

#%%
countries = ['AFG', 'USA']
variables = ['NGDP_RPCH', 'FLIBOR6']

weo_sub = weo[weo['ISO'].isin(countries) & weo['WEO Subject Code'].isin(variables)]

weo_sub.to_csv('weo.csv')

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
