"""
Chipotle data from NYT

Links
http://www.nytimes.com/interactive/2015/02/17/upshot/what-do-people-actually-order-at-chipotle.html
https://github.com/TheUpshot/chipotle
http://www.danielforsyth.me/pandas-burritos-analyzing-chipotle-order-data-2/

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

# data entry
url = 'https://raw.githubusercontent.com/TheUpshot/chipotle/master/orders.tsv'
chp = pd.read_csv(url, sep='\t')
chp.shape

# fix formatting of prices (kill the $)
chp['item_price'] = chp['item_price'].str.replace('$', '').astype(float)

#%%
"""
Plots from Daniel Forsyth
"""

# numbers sold by item
ax = chp['item_name'].value_counts().plot(kind='bar', figsize=(9,4.5))
ax.set_ylabel('Number Sold')
fig = ax.get_figure()
fig.show()

#%%
ax = chp['item_name'].value_counts(ascending=True).plot(kind='barh',
        figsize=(4.5, 12))
ax.set_title('Number of units sold', fontsize=14, loc='left')
fig = ax.get_figure()
fig.show()

#%%
# top 10
ax = chp['item_name'].value_counts(ascending=True)[-10:].plot(kind='barh')
ax.set_title('Top ten products', fontsize=14, loc='left')
ax.set_xlabel('Units Sold')
fig = ax.get_figure()
fig.show()

#%%
orders = chp.groupby(by='order_id').sum()
orders.plot(kind='hist', subplots=True)
orders.describe()

#%%
desc = chp.groupby(['item_name', 'choice_description'])['order_id'].count().reset_index(name='count')

# kinds of chicken bowls
cb = desc[desc['item_name'].str.contains('Chicken Bowl')][-3:]
#cb.sort(['count']), ascending=False)[:10]


