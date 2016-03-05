"""
Reading fixed format files in Pandas:  an example

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

#%%
"""
Reading fixed width files
http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.read_fwf.html
Input file is
1234567890
2345678901
3456789012
"""
import pandas as pd

fixed = pd.read_fwf('fixedformatdata.txt',
                    colspecs=[(0,2), (3,6)],     # column n1 to n2-1
                    names=['x1', 'x2'],
                    header=None)

print('\nFixed-format file \n', fixed)

