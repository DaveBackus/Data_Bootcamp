"""
Test program for Data Bootcamp course.

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python

Written by Dave Backus, March 2015
Created with Python 3.4
"""
print('\nWelcome to Data Bootcamp!')

import datetime
print('Today is: ', datetime.date.today(), '\n')

"""
Check Python version
"""
import sys

print('\nWhat version of Python are we running? \n', sys.version, '\n', sep='')

if float(sys.version_info[0]) < 3.0:
    raise Exception('Program halted, old version of Python. ' +
                    'Sorry, you need to install Anaconda again.')
else:
    print('Congratulations, Python is up to date!')
    sys.exit(0)      # this halts execution

#%%
"""
Check path of current working directory (just for the heck of it)
"""
# https://docs.python.org/2/library/os.path.html
import os

print('Current path:\n', os.getcwd(), sep='')
