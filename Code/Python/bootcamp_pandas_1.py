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
Read csv files into dataframe 
Checks first to see if file is in the current working directory
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

# read from url 
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
# change column label
oldlabel = df.columns.tolist()
newlabel = oldlabel
newlabel[0] = 'xyz'
df.columns = newlabel
print(df)

df = df.rename(columns={'x2': 'zyx'})  # or inplace=True

# http://stackoverflow.com/questions/20868394/changing-a-specific-column-name-in-pandas-dataframe

#%%
"""
Properties of dataframes
"""
df = df1
# some properties

def df_props(df):
    """
    Various properties of dataframe df    
    """
    print('Type: ', type(df))
    print('Shape (dimensions): ', df.shape)
    print('Column labels (variables): ', df.columns.tolist())
    print('Variable types: \n', df.dtypes, sep='')
    print('Index labels (observations): ', df.index.tolist())

#df_props(df)

#%%
# 538 college majors data
# more at https://github.com/fivethirtyeight/data/tree/master/college-majors  
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/'
url2 = 'college-majors/recent-grads.csv'
url = url1 + url2 
df538 = pd.read_csv(url) 

df_props(df538)

#%%
# read IMF's WEO data (tab-delimited despite its xls extension)
# more at https://www.imf.org/external/pubs/ft/weo/2015/01/weodata/index.aspx
# takes about 10 seconds at homne over wireless network 
url = 'http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/WEOApr2015all.xls'
weo = pd.read_csv(url, sep='\t', thousands=',')   # tab = \t 

weo.shape
weo.head()

#%%
# trim this down 
countries = ['USA']
years = [str(year) for year in range(1980, 2016)]
columns = [..]
weo_sub = weo[weo['ISO'].isin(countries)]
print('Shape of weo_sub:', weo_sub.shape)
weo


#print('Top 5 observations\n', weo.head())
print('Type: ', type(weo))
print('Shape (dimensions): ', weo.shape)
print('Column labels (variables): ', weo.columns.tolist())
print('Variable types: \n', weo.dtypes, sep='')

#%%
# Brandon Rhodes' movie data from PyCon 2015 
# 15-20 seconds on office computer 
url = 'http://pages.stern.nyu.edu/~dbackus/csv/cast.csv'
cast = pd.read_csv(url, encoding='utf-8')

#%%
print(cast.shape) 
print(cast.head(10))
h = cast.head()

#%%


#%%
# select subset of dataframe 
variables = ['NGDP_RPCH', 'FLIBOR6']



#%%
#%%
# read from xls 
file = '../backup/test.xlsx'
xls = pd.read_excel(file)       # default is first sheet





#%%
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
file = '../backups/' + os.path.basename(url)            # strip out file name 
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
