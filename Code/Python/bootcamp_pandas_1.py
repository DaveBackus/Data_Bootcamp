"""
Pandas intro for Data Bootcamp course (data input and management)
Topics:  reading csv and xls files, properties of dataframes.  

Repository of materials (including this file): 
* https://github.com/DaveBackus/Data_Bootcamp 
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python  

Written by Dave Backus, August 2015 
Created with Python 3.4 
"""
"""
Packages:  add new tools to Python (libraries, modules)
* Pandas:  data management
* Matplotlib:  graphics 
* Django:  web apps 
Google "anaconda packages" 
Add them with import statements 
"""
"""
Check versions (ignore this)
"""
import pandas as pd      # the data package
import sys 


print('\nPython version:', sys.version) 
print('Pandas version: ', pd.__version__) 

#%%
"""
Read xls and csv files (and why we like csv's)
"""
import pandas as pd     # redundant, there to make cell self-contained 

# read files from computer 
# make sure they're in the current working directory 
file1 = 'test.csv'
df1 = pd.read_csv(file1)
print('\ncsv read (df1)\n', df1) 

file2 = 'test.xls'
df2 = pd.read_excel(file2)
print('\nxls read (df2)\n', df2) 

# read same file from url 
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2 
df3 = pd.read_csv(url)
print('\nurl read (df3)\n', df3)

#%%
"""
What type of object do we have?  What are its properties?
Try these methods:  shape, columns, index, head()/tail() [also list(df)]
Also:  dtypes, mean, describe(), transpose()=T, to_csv
"""
df = df3 

# Exercise.  How do I output df as a csv or xls file?  
# Exercise.  What other methods do you see?  
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
# sort by y1:  df.sort_values(['y1'])

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
