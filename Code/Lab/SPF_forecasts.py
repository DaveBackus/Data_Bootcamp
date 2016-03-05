"""
Survey of Professional Forecasters
The Philly Fed has been polling forecasters for years and posting both
summary statistics (mean forecasts, for example) and individual numbers
(suitably anonymized).  We take a look at the recent data, see what's there.

Link
* https://www.philadelphiafed.org/research-and-data/real-time-center/survey-of-professional-forecasters/

Prepared for Data Bootcamp course at NYU
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus and Chase Coleman, March 2016
Created with Python 3.5
"""
"""
import packages, check versions
"""
import sys
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

print('\nPython version: ', sys.version)
print('Pandas version: ', pd.__version__, '\n')

#%%
"""
read data
"""
url1 = 'https://www.philadelphiafed.org/-/media/research-and-data/'
url2 = 'real-time-center/survey-of-professional-forecasters/'
url3 = 'historical-data/micro5.xls'
url = url1 + url2 + url3

spf = pd.read_excel(url)
print('Dimensions:', spf.shape)
print('\nData types:\n', spf.dtypes, sep='')


#%%

#%%
