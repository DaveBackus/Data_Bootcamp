"""
Yahoo options data using pandas-datareader

Must install pandas-datareader and html5lib:
conda install pandas-datareader, html5lib

References
* http://finance.yahoo.com/q/op?s=AMZN+Options
* https://pandas-datareader.readthedocs.org/en/latest/

Prepared for Data Bootcamp course at NYU
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, February 2016
Created with Python 3.5
"""
# Spencer wrote the first version of this module
import pandas as pd
import pandas_datareader.yahoo.options as yho
import matplotlib.pyplot as plt

"""
supply ticker, get option prices
"""
ticker = 'amzn'
otk = yho.Options(ticker)
exp = otk.expiry_dates     # get expiration dates

# get option prices
cols = [0, 1, 2, 7]
calls = otk.get_call_data(expiry=exp[7])[cols]
puts  = otk.get_put_data(expiry=exp[7])[cols]

# drop extra index levels
calls = calls.reset_index(level=[1,2,3], drop=True)
puts  = puts.reset_index(level=[1,2,3], drop=True)

# cut off extremes
spot = otk.underlying_price
calls  = calls[(calls.index >= 0.75*spot) & (calls.index <= 1.25*spot)]
puts  = puts[(puts.index >= 0.75*spot) & (puts.index <= 1.25*spot)]

# compute mid-market
calls['Mid'] = (calls['Bid'] + calls['Ask'])/2
puts['Mid']  = (puts['Bid'] + puts['Ask'])/2

#%%
"""
plot put and call prices
* bid-ask mid
* last
* implied vols
"""
fig, ax = plt.subplots()
calls['Mid'].plot(lw=2, color='blue', alpha=0.6, ax=ax)
puts['Mid'].plot(lw=2, color='m', alpha=0.6, ax=ax)
ymin, ymax = ax.get_ylim()
ax.set_title('Prices of Amazon options (bid-ask avg)', fontsize=14, loc='left')
ax.set_ylabel('Option Prices')
ax.set_xlabel('Strike Price')
ax.vlines(x=spot, ymin=ymin, ymax=ymax, linestyle='dashed')
ax.text(1.01*spot, 0.9*ymax, 'Stock price', horizontalalignment='left')
ax.text(545, 80, 'Put prices', horizontalalignment='right', color='m')
ax.text(420, 80, 'Call prices', horizontalalignment='left', color='b')
fig.show()

#%%
fig, ax = plt.subplots()
which = 'last'
calls[which].plot(lw=2, color='blue', alpha=0.6, ax=ax)
puts[which].plot(lw=2, color='m', alpha=0.6, ax=ax)
ymin, ymax = ax.get_ylim()
ax.set_title('Prices of Amazon options (last quote)', fontsize=14, loc='left')
ax.set_ylabel('Option Prices')
ax.set_xlabel('Strike Price')
ax.vlines(x=spot, ymin=ymin, ymax=ymax, linestyle='dashed')
ax.text(1.01*spot, 0.9*ymax, 'Stock price', horizontalalignment='left')
ax.text(545, 80, 'Put prices', horizontalalignment='right', color='m')
ax.text(420, 80, 'Call prices', horizontalalignment='left', color='b')
fig.show()

#%%
# convert IV data to numbers
calls['IV'] = calls['IV'].str.replace('%', '').astype(float)
puts['IV']  = puts['IV'].str.replace('%', '').astype(float)

fig, ax = plt.subplots()
calls['IV'].plot(lw=2, color='blue', alpha=0.6, ax=ax)
puts['IV'].plot(lw=2, color='m', alpha=0.6, ax=ax)
ymin, ymax = ax.get_ylim()
ax.set_title('Implied volatilities of Amazon options', fontsize=14, loc='left')
ax.set_ylabel('Implied Volatility (percent)')
ax.set_xlabel('Strike Price')
ax.vlines(x=spot, ymin=ymin, ymax=ymax, linestyle='dashed')
ax.text(1.01*spot, 0.9*(ymax-ymin)+ymin, 'Stock price', horizontalalignment='left')
ax.text(400, 46, 'Puts', horizontalalignment='right', color='m')
ax.text(450, 46, 'Calls', horizontalalignment='left', color='b')
fig.show()

#%%
#%%
"""
we can also use read_html, but the output is a mess
"""
url = 'http://finance.yahoo.com/q/op?s=AMZN+Options'
ops = pd.read_html(url)

print('Dimensions of ops[1]', ops[1].shape)
print('Dimensions of ops[2]', ops[2].shape)
print('Column labels:', list(ops[1]))
print('Row labels:', ops[1].index.tolist())


#%%
"""
Check whether packages are installed
http://stackoverflow.com/questions/14050281/how-to-check-if-a-python-module-exists-without-importing-it
"""
import importlib

def check_for_package(package):
    lib_spec = importlib.util.find_spec(package)
    found = lib_spec is not None
    print('Package', package, 'found?', found)
    return found

foundpdr = check_for_package('pandas_datareader.yahoo.options')
foundh5  = check_for_package('html5lib')

ready = foundpdr and foundh5


