"""
Messing around with the IMF's WEO dataset.  The first section is an exploration
of various methods of reading data from a url.

Once we've read in the data, we can slice as needed.

Note:  data file is labeled xls but it's really tab-delimited text.

Prepared for the NYU Course "Data Bootcamp."
More at https://github.com/DaveBackus/Data_Bootcamp

References
* http://www.imf.org/external/ns/cs.aspx?id=28
* http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.parsers.read_table.html
* http://pandas.pydata.org/pandas-docs/stable/io.html#io-read-csv-table
* https://docs.python.org/3.4/library/urllib.html
* https://docs.python.org/3.4/library/os.html

Written by Dave Backus @ NYU, September 2014
Created with Python 3.4
"""
import pandas as pd
import urllib.request
import os

"""
1. Read data from url (several approaches illustrated)
"""
# file is labeled xls but it's really tab delimited
url = 'http://www.imf.org/external/pubs/ft/weo/2014/01/weodata/WEOApr2014all.xls'

# two versions (takes 5-10 seconds for both)
df1 = pd.read_table(url)            # tab delimited is the default
df2 = pd.read_csv(url, sep='\t')    # tab = \t

#%%
# copy to hard drive
file = '../Data/WEOApr2014all.xls'
urllib.request.urlretrieve(url, file)

#%%
# Sarah's version
f = urllib.request.urlopen(url)
file_sbh = file[:-4] + '_sbh' + file[-4:]
with open(file_sbh, 'wb') as local_file:
    local_file.write(f.read())

#%%
# cool thing from Sarah:  strips filename from url
base = os.path.basename(url)

"""
2. Slice and dice
"""

