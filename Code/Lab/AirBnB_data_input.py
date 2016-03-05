"""
AirBnB

Reads data, what's next?

Link to scraped data
* http://insideairbnb.com/new-york-city/
* http://insideairbnb.com/get-the-data.html

Prepared for Data Bootcamp course at NYU
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, February 2016
Created with Python 3.5
"""
"""
import packages, check versions
"""
import sys
import pandas as pd
#import matplotlib.pyplot as plt

print('\nPython version: ', sys.version)
print('Pandas version: ', pd.__version__, '\n')

#%%
"""
read data
"""
urllst  = 'http://data.insideairbnb.com/united-states/'
urllst += 'ny/new-york-city/2016-02-02/data/listings.csv.gz'

urlrev  = 'http://data.insideairbnb.com/united-states/'
urlrev += 'ny/new-york-city/2016-02-02/data/reviews.csv.gz'

# listings
airlst = pd.read_csv(urllst, compression='gzip')
print('\nListings data')
print('Dimensions:', airlst.shape)
print('Variables:\n', list(airlst), sep='')

# reviews
airrev = pd.read_csv(urlrev, compression='gzip')
print('\nReviews data')
print('Dimensions:', airrev.shape)
print('Variables:\n', list(airrev), sep='')

