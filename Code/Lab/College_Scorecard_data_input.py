"""
College Scorecard
US college data from Dept of Education

Sources
* https://collegescorecard.ed.gov/data/

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp/

Written by Dave Backus, December 2015
Created with Python 3.5
"""
"""
Check Python version
"""
import pandas as pd               # the data package
import sys                        # system module (don't ask)

print('\nPython version:', sys.version)
print('Pandas version: ', pd.__version__)

#%%
"""
Read csv file (large file, takes a while)
"""
import pandas as pd

url = 'https://s3.amazonaws.com/ed-college-choice-public/Most+Recent+Cohorts+(Scorecard+Elements).csv'

sc = pd.read_csv(url, nrows=10)

list(sc)

#%%
"""
Plot
"""
# extract mean math score, sort top to bottom


