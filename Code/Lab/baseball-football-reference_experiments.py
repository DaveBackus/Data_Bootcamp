"""
baseball-reference.com and pro-football-reference.com

Their pages have easy links to read.  Here we read in Andrew McCutchen's
batting record by year.  We use the pandas read_html function, which
returns a list of dataframes, one for each table on the page, 11 total.
Some of them have lots of blank columns.

Tables:
0: name etc
1: projection
2: batting
3: player value
etc

Prepared for Data Bootcamp course at NYU
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus and Chase Coleman, February 2016
Created with Python 3.5
"""
import pandas as pd

print('\nPandas version: ', pd.__version__)

url = 'http://www.baseball-reference.com/players/m/mccutan01.shtml'
ac = pd.read_html(url)

print('Type:', type(ac))
print('Length:', len(ac))

print('Table 3\n', ac[3])


#%%
"""
works for football, too
"""
url = 'http://www.pro-football-reference.com/players/B/BrowAn04.htm'
ab = pd.read_html(url)

print('Type:', type(ab))
print('Length:', len(ab))

