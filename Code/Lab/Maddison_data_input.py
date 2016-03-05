"""
Maddison project
Long histories of GDP per person

Links
http://www.ggdc.net/maddison/maddison-project/home.htm
http://www.ggdc.net/maddison/maddison-project/data.htm

Prepared for Data Bootcamp course at NYU
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, January 2016
Created with Python 3.5
"""
"""
import packages, check versions
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.pyplot as plt

print('\nPython version: ', sys.version)
print('Pandas version: ', pd.__version__, '\n')

"""
read data from internet source
"""
url = 'http://www.ggdc.net/maddison/maddison-project/data/mpd_2013-01.xlsx'
mpd = pd.read_excel(url, skiprows=2, index_col=0, na_values=[' '])
# strip trailing blanks in country names
# use comprehension instead? string methods?
mpd.columns = map(str.rstrip, mpd.columns)

print('Dataframe dimensions:', mpd.shape)

#%%
# select countries
countries = ['England/GB/UK', 'USA', 'Japan', 'China', 'India', 'Argentina']
mpd = mpd[countries]
mpd = mpd.rename(columns={'England/GB/UK': 'UK'})
mpd = np.log(mpd)/np.log(2)

#%%
"""
log base-2 plot
"""
subset = mpd.dropna().copy()

fig, ax = plt.subplots()
subset.plot(lw=2, ax=ax)
ax.set_title('GDP per person', fontsize=14, loc='left')
ax.set_ylabel('GDP Per Capita (1990 USD, log2 scale)')
# legend parameters: http://matplotlib.org/users/customizing.html
ax.legend(loc='upper left', fontsize=10, handlelength=2, labelspacing=0.15)
#fig.savefig('Maddison-GDP-1870-on.pdf', bbox_inches='tight')

#%%
"""
UK plot
"""
fig, ax = plt.subplots()
mpd['UK'].dropna().plot(lw=2, ax=ax)
ax.set_title('GDP per person in the UK', fontsize=14, loc='left')
ax.set_ylabel('GDP Per Capita (1990 USD, log2 scale)')
fig = ax.get_figure()
#fig.savefig('Maddison-GDP-1870-on.pdf', bbox_inches='tight')

