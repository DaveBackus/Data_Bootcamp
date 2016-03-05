"""
Messing around with Quandl, a popular online collection of economic and
finance data.  Known for easy access and clear links to original sources,
so you know what you have.

Install the Python app by typing in the command line:  pip install Quandl

** THIS DOES NOT WORK YET **

References
* https://www.quandl.com/tools/python
* https://www.quandl.com/search?query=options&type=free

Prepared for Data Bootcamp course at NYU
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, February 2016
Created with Python 3.5
"""
import sys
import pandas as pd
import Quandl as Q
#import datetime as dt

print('\nPython version: ', sys.version)
print('Pandas version: ', pd.__version__, '\n')

"""
# from the docs
import Quandl
mydata = Quandl.get("WIKI/AAPL")
"""
#%%

# not clear what this is
opti = Q.get("GOOG/EBR_OPTI")


