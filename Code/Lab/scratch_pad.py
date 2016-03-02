"""
Scratch pad for Data Bootcamp class 
Type everything here rather than the console 
"""
import matplotlib.pyplot as plt 
import pandas.io.data as web

ff = web.DataReader('F-F_Research_Data_factors', 'famafrench')[1]
ff.columns = ['xsm', 'smb', 'hml', 'rf']
ff['rm'] = ff['xsm'] + ff['rf']
ff = ff[['rm', 'rf']]               # extract rm (market) and rf (riskfree)
ff.head(5)


fig, ax = plt.subplots()
ff.plot(ax=ax, kind='line', title='Fama-French market and riskfree returns')


#%%
import pandas as pd
import matplotlib.pyplot as plt  
data = {'Food': ['French Fries', 'Potato Chips', 'Bacon', 'Pizza', 'Chili Dog'], 
        'Calories per 100g':  [607, 542, 533, 296, 260]}
cal  = pd.DataFrame(data)
cal  = cal.set_index('Food')
cal

#%%
fig, ax = plt.subplots()
cal.plot(kind='barh', ax=ax, legend=False)

#%%
