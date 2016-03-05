"""
Code Practice #3 template
Data Bootcamp course, NYU Stern, http://databootcamp.nyuecon.com/
"""

"""
Question 1
"""
import pandas as pd
data = {'BRA': [13.37, 13.30, 14.34, 15.07, 15.46, 15.98, 16.10],
        'JPN': [33.43, 31.83, 33.71, 34.29, 35.60, 36.79, 37.39],
        'USA': [48.30, 46.91, 48.31, 49.72, 51.41, 52.94, 54.60],
        'Year': [2008, 2009, 2010, 2011, 2012, 2013, 2014]}
weo  = pd.DataFrame(data)


#%%
"""
Question 2
"""
url1  = 'http://pages.stern.nyu.edu/~dbackus/Data/'
url2 = 'Data-Bootcamp-entry-poll_s16.csv'
url = url1 + url2

ep = pd.read_csv(url)
print('Data types:\n', ep.dtypes, sep='')

#%%
"""
Question 3
"""
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/'
url2 = 'college-majors/recent-grads.csv'
url = url1 + url2

df538 = pd.read_csv(url)
