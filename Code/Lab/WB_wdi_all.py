"""
Messing around with World Bank data.  We start by reading in the whole WDI
from the online csv.  Since the online file is part of a zipped collection,
this turned into an exploration of how to handle zip files -- see Section 1.
Section 2 (coming) does slicing and plotting.

Prepared for the NYU Course "Data Bootcamp."
More at https://github.com/DaveBackus/Data_Bootcamp

References
* http://datacatalog.worldbank.org/
* http://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python
* https://docs.python.org/3.4/library/urllib.html

Written by Dave Backus @ NYU, September 2014
Created with Python 3.4
"""
import pandas as pd
import urllib
import zipfile
import os

"""
1. Read data from component of online zip file
"""
# locations of file input and output
url  = 'http://databank.worldbank.org/data/download/WDI_csv.zip'
file = os.path.basename(url)        # cool tool via SBH
# the idea is to dump data in a different directory, kill with data = ''
data = '' # '../Data/'

#%%
# copy file from url to hard drive (big file, takes a minute or two)
urllib.request.urlretrieve(url, data+file)

#%%
# zipfile contains several files, we want WDI_Data.csv
print(['Is zipfile?', zipfile.is_zipfile(file)])
# key step, give us a file object to work with
zf = zipfile.ZipFile(data+file, 'r')
print('List of zipfile contents (two versions)')
[print(file) for file in zf.namelist()]
zf.printdir()

#%%
# copy data file to hard drive's working directory, then read it
csv = zf.extract('WDI_Data.csv')
df1  = pd.read_csv('WDI_Data.csv')
print(df1.columns)

#%%
# alternative:  open and read
csv = zf.open('WDI_Data.csv')
df2 = pd.read_csv(csv)
print(df3.columns)

#%%
# same thing in one line
df3 = pd.read_csv(zf.open('WDI_Data.csv'))
print(df3.columns)

# zf.close()   #??
# do we want to close zf?  do we care?
# seems to be essential with writes, not so much with reads
# if so, can either close or use the "with" construction Sarah used.
# basic open etc:
# https://docs.python.org/3.4/tutorial/inputoutput.html#reading-and-writing-files
# on with (go to bottom):  http://effbot.org/zone/python-with-statement.htm

#%%
# could we further consolidate zip read and extract?  seems not.
#zf = zipfile.ZipFile(url, 'r')

