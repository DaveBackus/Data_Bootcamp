"""
Read the Doing Business rankings.  Created for the Data Bootcamp course
at NYU Stern.

Link
http://www.doingbusiness.org/
http://www.doingbusiness.org/rankings

Course materials
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp

Written by Dave Backus, February 2016
Created with Python 3.5
"""
import pandas as pd

url = 'http://www.doingbusiness.org/rankings'
db = pd.read_html(url)
df = db[0]
list(df)

#%%
df.columns = ['Economy', 'Rank', 'Starting a Business',
              'Construction', 'Electricity', 'Property',
              'Credit', 'Protecting Investors', 'Taxes',
              'Trade', 'Enforcing Contracts', 'Resolving Insolvency']

#%%
df = df.set_index(['Economy'])
df[[0,1,2]].head(10)
#%%
df[[3,4,5]].head(10)
#%%
df[[6,7,8]].head(10)

#%%
df[[9,10]].head(10)

#%%
"""
Can we access DB numbers through the World Bank API?
"""


