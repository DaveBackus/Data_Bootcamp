"""
Data Bootcamp test program 
Program checks to see that you're running Python 3.  If not, you get a warning 
message.  

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

print('What version of Python are we running? \n', sys.version, '\n', sep='') 

if float(sys.version_info[0]) < 3.0:       
    raise Exception('Program halted, old version of Python. ' +  
                    'Sorry, you need to install Anaconda again.')
else:
    print('Congratulations, Python is up to date!')
    
#%%
"""
Check path of current working directory (just for the heck of it)  
"""
# https://docs.python.org/2/library/os.path.html
import os 

print('Current path:\n', os.getcwd(), sep='')

#%%
"""
Check for support code 
""" 
# https://docs.python.org/3.4/library/os.html
import os

print('List of files in working directory:')
[print(file) for file in os.listdir()]

if not os.path.isfile('SQL_support_code.py'):
    raise Exception('***** Program halted, support code missing *****')
    
"""
Assignments and copies 
"""
# check 1
a = [1,2,3]
b = a
b[0] = 'WHOA!'
print('\nAfter assignment, a is', a)

# to make a copy 
a = [1,2,3]
b = a.copy()
b[0] = 'WHOA!' 
print('\nAfter copy, a is', a)

# check 2
import numpy as np 
c = np.array([7, 3, 5]) 
d = c 
e = 2*c - 5
print('\nAfter assignment, (d, e) are', d, e)

c[0] = 10
print(d, e)

