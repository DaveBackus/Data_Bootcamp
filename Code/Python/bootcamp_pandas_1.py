"""
Pandas intro for Data Bootcamp course (data input and management)
Topics:  reading csv and xls files, properties of dataframes.

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp

Written by Dave Backus, August 2015
Created with Python 3.4
"""
"""
Packages:  add new tools to Python (libraries, modules)
* Pandas:  data management
* Matplotlib:  graphics
* Many more
Google "anaconda packages"
Add them with import statements
"""
"""
Check versions (ignore this)
"""
import pandas as pd               # the data package
import sys                        # system module (don't ask)

print('\nPython version:', sys.version)
print('Pandas version: ', pd.__version__)

# Exercise.  What if we import pandas twice, once as pd and once as pa.  
# Do they both work?  (Ask yourself:  How would you know?)

#%%
"""
Read csv file from internet (and why we like csv's)
The result is a data frame:  like a sheet with row and column labels
"""
import pandas as pd               # redundant, but it's ok to do it again 

# read file from url
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2
df = pd.read_csv(url)

print('\nurl read (df)\n', df)    # \n tells print to skip a line

# if the internet is down 
#df_fromdict = pd.DataFrame({'name': ['Dave', 'Chase', 'Spencer'], 
#            'x1': [1, 4, 5], 'x2': [2, 3, 6], 'x3': [3.5, 4.3, 7.8]}) 

#%%
"""
Exercises
* xlsx 
* na_values
"""
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2
dfex = pd.read_csv(url, na_values=[1])

#%%
"""
xls annd xlsx files 
"""
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.xls'
url  = url1 + url2
dfx = pd.read_excel(url)

print('\nurl read (df)\n', dfx)    # \n tells print to skip a line



#%%
"""
What type of object do we have?  What are its properties?
"""
type(df)
# aka dataframe 

# Apply these methods, explain what they do: shape, index, columns, dtypes 

# Exercise:  Try df.columns.tolist() and list(df).  


#%%
"""
There are lots of things we can do with dataframes
 head()/tail() [also list(df)]
Also:  dtypes, mean, describe(), transpose()=T, to_csv
"""
# Exercise.  How do I output df as a csv or xls file?
# Exercise.  What other methods do you seed?
# Exercise.  What does the plot method do?

#%%
"""
Read csv file from internet (and why we like csv's)
The result is a data frame:  like a sheet with row and column labels
"""
import pandas as pd     # redundant, there to make cell self-contained

url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2
df = pd.read_csv(url)
print('\nurl read (df)\n', df)


#%%
"""
What type of object do we have?  What are its properties?
Try these methods:  shape, columns, index, head()/tail() [also list(df)]
Also:  dtypes, mean, describe(), transpose()=T, to_csv
"""

# what kind of object do we have?  
print(type(df))

# try these methods:  what do they do?  shape, dtypes, transpose()=T
# also these:  mean, describe(), to_csv  
"""
xxx
"""
# Exercise.  How do I output df as a csv or xls file?
# Exercise.  What other methods do you seed?
# Exercise.  What does the plot method do?

#%%
"""
Playing with variables:  select variables, create new ones, plot them
"""
# what is this?
df['x1']

#%%
# construct new variables
df['y1'] = df['x1']/df['x2']
df['y2'] = df['x2'] + df['x3']

#%%
# Exercise.  Use the dtypes method.  What does it tell us?

# Exercise.  What does this do?
# df = df.set_index('Name')


#%%
# sort by y1
df.sort_values(['y1'])

#%%
# this is cool, but not recommended (goes against the automation mentality)
df.to_clipboard()


#%%
"""
Data input from your computer 
Create or find Data_Bootcamp directory 
Create spreadsheet, save as xlsx, xls, csv 
Locate and set current working directory 
"""
import pandas as pd          # still redundant

# read files from computer
# make sure they're in the current working directory
file1 = 'test.xlsx'
df1 = pd.read_excel(file1)
print('\nxlsx read\n', df1)

file2 = 'test.xls'
df2 = pd.read_excel(file2)
print('\nxls read\n', df2)

file3 = 'test.csv'
df3 = pd.read_csv(file3)
print('\ncsv read\n', df3)



#%%
# plots:  what do they do?
df.plot()
df.plot.bar()
df.plot.scatter('x1', 'y1')

#%%
"""
538 income by college major
http://fivethirtyeight.com/features/the-economic-guide-to-picking-a-college-major/
https://github.com/fivethirtyeight/data/tree/master/college-majors
"""
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/'
url2 = 'college-majors/recent-grads.csv'
url = url1 + url2
df538 = pd.read_csv(url)

# Exercise.  What are the variables here?  How many?

#%%
"""
Brandon Rhodes' IMDb movie data from PyCon 2015
https://github.com/brandon-rhodes/pycon-pandas-tutorial#welcome-to-brandons-pandas-tutorial
Big file, 15-20 seconds on office computer, more with wireless connection
"""
url = 'http://pages.stern.nyu.edu/~dbackus/csv/cast.csv'
cast = pd.read_csv(url, encoding='utf-8')

#%%
print(cast.shape)
print(cast.head(10))

print(cast.shape)

# Try these:
# list(cast)
# ah = cast[cast['title']=='Annie Hall']
# gc = cast[cast['name']=='George Clooney']

#%%
"""
Web interface:  FRED, World Bank, Fama-French, ...
"""
"""
Example:  Fama-French stock returns
* xsm = excess return on market (market minus riskfree rate)
* smb = return on small firms minus return on big firms
* hml = return on high book-to-market firms minus low
* rf  = riskfree rate
All returns are monthly percentages
Google "ken french data"
"""
import pandas.io.data as web

ff = web.DataReader('F-F_Research_Data_factors', 'famafrench')[0]
ff.columns = ['xsm', 'smb', 'hml', 'rf']

ff.describe()

"""
Creating dataframes 
"""
# from list of lists (no one does this) 
#df = pd.DataFrame([['Dave', 1, 2, 3.5], 
#                   ['Chase', 4, 3, 4.3], 
#                   ['Spencer', 5, 6, 7.8]],
#                   columns=['name', 'x1', 'x2', 'x3'])
#print('\nurl read (df)\n', df)
