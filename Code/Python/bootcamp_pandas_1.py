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

print('\nPython version:', sys.version) 
print('Pandas version: ', pd.__version__) 

#%%
"""
Read csv file into dataframe 
Check first to see if file is in the current working directory
"""
import os 

# some checks just to be cute 
print('\nCurrent working directory: ', os.getcwd())
#print('\n List of files in working directory: ', os.listdir())

# check for file 
file = 'test.csv'
if not os.path.isfile(file):
    raise Exception('***** Program halted, csv file not found *****')

# read from local drive  
df1 = pd.read_csv(file)
print('\nFile test.csv read from hard drive', '\n\nContents\n', df, sep='')

"""
Properties of the input
"""
print('\nProperties of text.csv') 
print('Type:', type(df1))
print('Dimensions:', df1.shape) 
print('\nIndex (row labels)\n', df1.index, sep='') 
print('\nColumns (column labels)\n', df1.columns, sep='') 
print('\nVariable types\n', df1.dtypes, sep='') 

"""
List properties with a function 
"""
def df_props(df):
    """
    Various properties of dataframe df    
    """
    print('\n\nType: ', type(df))
    print('Dimensions (shape)): ', df.shape)
    print('Column labels (variables): ', df.columns.tolist())
    print('Variable types: \n', df.dtypes, sep='')
    print('Index labels (observations): ', df.index.tolist())

df_props(df1)

#%%
# read same file from url 
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2 
df2 = pd.read_csv(url)

# transpose (switch rows and columns)
dft = df2.T
print(dft)

df = df1 

# Write as csv 
df.to_csv('foo.csv')

#%%

#%%
# 538 college majors data
# more at https://github.com/fivethirtyeight/data/tree/master/college-majors  
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/'
url2 = 'college-majors/recent-grads.csv'
url = url1 + url2 
df538 = pd.read_csv(url) 

df_props(df538)

#%%
"""
Read IMF's WEO data (tab-delimited despite its xls extension)
more at https://www.imf.org/external/pubs/ft/weo/2015/01/weodata/index.aspx
Takes about 10 seconds at homne over wireless network 
"""
import pandas as pd 
import numpy as np 

url = 'http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/WEOApr2015all.xls'
weo = pd.read_csv(url, sep='\t', thousands=',')   # tab = \t 

weo.shape
weo.dtypes

#%%
"""
GDP growth scatterplot
"""
weo = weo[]
weo['g8000'] = (np.log(weo['1995']) - np.log(weo['1980']))/15 

#%%
# trim this down 
countries = ['USA']
years = [str(year) for year in range(1980, 2015)]
#columns = [..]
weo_sub = weo[weo['ISO'].isin(countries)]
print('Shape of weo_sub:', weo_sub.shape)
weo


#print('Top 5 observations\n', weo.head())
print('Type: ', type(weo))
print('Shape (dimensions): ', weo.shape)
print('Column labels (variables): ', weo.columns.tolist()) 
print('Variable types: \n', weo.dtypes, sep='')

#%%
"""
IMF historical data database 
"""
xlsfile = 'Debt Database Fall 2013 Vintage.xlsx'
debt = pd.read_excel('../Temp/' + xlsfile, sheetname=1) 


#%%
"""
Brandon Rhodes' movie data from PyCon 2015 
Big files, 15-20 seconds on office computer 
"""
url = 'http://pages.stern.nyu.edu/~dbackus/csv/cast.csv'
cast = pd.read_csv(url, encoding='utf-8')

print(cast.shape) 
print(cast.head(10))
h = cast.head()


#%%
"""
urllib versions
most are for the WDI, which is way too big and takes too long 
"""
# copy file from url to hard drive 
import urllib.request           # this is a module from the package urllib 
file = 'foo.csv'
url1 = 'https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/'
url2 = 'Code/Data/test1.csv'
url = url1 + url2 
urllib.request.urlretrieve(url, file)

#%%
# Sarah's version 
f = urllib.request.urlopen(url)
file = 'foo_sbh.csv'
with open(file, 'wb') as local_file:
    local_file.write(f.read())

#%%
# zip files  
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
[print(file) for file in zf.namelist()]
zf.printdir()

# extract a component 
csv = zf.extract('WDI_Data.csv')        # copy to disk  
df1 = pd.read_csv(csv)       # read
print(df1.columns)                      # check contents 

# alternative:  open and read
csv = zf.open('WDI_Data.csv')
df2 = pd.read_csv(csv)
print(df2.columns)
