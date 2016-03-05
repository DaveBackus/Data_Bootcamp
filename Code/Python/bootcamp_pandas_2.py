"""
Pandas advanced tools for Data Bootcamp course.

Topics:  reading csv and xls files, properties of dataframes.

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python

Written by Dave Backus, August 2015
Created with Python 3.4
"""
"""
the usual checks
"""
import sys
import pandas as pd

print('\nPython version: ', sys.version)
print('\nPandas version: ', pd.__version__, '\n')

#%%
"""
Remote data access
"""
from pandas.io.data import Options
aapl = Options('aapl', 'yahoo')
data = aapl.get_all_data()



#%%
"""
Set up simple dataframes to play with
"""
# create arbitrary dataframe
gdp = [2, 5, 7, 9]
pop = [9, 6, 3, 10]
cty = ['USA', 'USA', 'FRA', 'FRA']
year = ['2010', '2011', '2012', '2013']

data = {'gdp': gdp, 'pop': pop, 'cty': cty}
df = pd.DataFrame(data=data, index=year)
print('Sample dataframe\n', df)

#%%
what = df.head(2)
print(what)

#%%
import pandas as pd
# create dataframe with data and structure from WEO
variable = ['emp', 'emp', 'pop', 'pop', 'gdppc', 'gdppc']
country  = ['FRA', 'USA', 'FRA', 'USA','FRA', 'USA']
x2013    = [25.8, 142.5, 63.4, 314.4, 32.3, 48.8]
x2014    = [25.8, 146.3, 63.9, 319.0, 32.2, 50.4]
x2015    = [26.0, 148.7, 64.2, 321.2, 32.5, 51.6]

# this is a dictionary
weodata = {'country': country, 'variable': variable,
           '2013': x2013, '2014': x2014, '2015': x2015}
weo = pd.DataFrame(data=weodata)
print('WEO-like dataframe\n', weo)

#%%
# whip into shape:  version #1
wsi = weo.set_index(['variable', 'country'])
print('\nSet index version:\n', wsi)

wsr = wsi.reset_index(level='country')
print('\nReset:\n', wsr)

wsit = wsi.T
print('\nTransposed:\n', wsit)

#%%

# whip into shape:  version #2
wsi = weo.set_index(['variable', 'country'])
print('\nSet index version:\n', wsi)

wu = wsi.unstack()
print('\nUnstacked:\n', wu)

#%%
"""
zip
"""
l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']
d = dict(zip(l1, l2))


#%%
"""
groupby
"""
g = df.groupby('cty').size()        # not the best example of this


#%%
"""
.set_index and .reset_index
"""
df1 = df.set_index('cty', append=True)      # or inplace=True
print(df1)

df2 = df1.reset_index('cty')
print(df2)

#%%
"""
.stack and .unstack
"""

dfu = df.unstack()
dfs = df.stack()

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

"""
Checks to see if file is in current working directory
"""
import os

# some checks just to be cute
print('\nCurrent working directory: ', os.getcwd())
#print('\n List of files in working directory: ', os.listdir())

# check for file
file = 'test.csv'
if not os.path.isfile(file):
    raise Exception('***** Program halted, csv file not found *****')

#%%
"""
Properties of the input
"""
print('\nProperties of text.csv')
print('Type:', type(df1))
print('Dimensions:', df1.shape)
print('\nIndex (row labels)\n', df1.index, sep='')
print('\nColumns (column labels)\n', df1.columns, sep='')
print('\nVariable types\n', df1.dtypes, sep='')

#%%
"""
List properties with a function
"""
def dfprops(df):
    """
    Various properties of dataframe df
    """
    print('\n\nType: ', type(df))
    print('Dimensions (shape)): ', df.shape)
    print('Column labels (variables): ', df.columns.tolist())
    print('Variable types: \n', df.dtypes, sep='')
    print('Index labels (observations): ', df.index.tolist())

#df_props(df1)
