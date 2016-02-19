"""
baseball-reference.com

Their pages have easy links to read.  Here we read in Andrew McCutchen's 
batting record by year.  We use the pandas read_html function, which 
returns a list of dataframes, one for each table on the page.  Some of them
have lots of blank columns. 

Tables:
0: name etc
1: projection
2: batting 
3: player value 

Prepared for Data Bootcamp course at NYU  
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab 

Written by Dave Backus, February 2016 
Created with Python 3.5 
"""
import pandas as pd

print('\nPandas version: ', pd.__version__) 

urlh = 'http://www.baseball-reference.com/players/m/mccutan01.shtml'
bb = pd.read_html(urlh)

print('Type:', type(bb))
print('Length:', len(bb))

print('Table 3\n', bb[3])