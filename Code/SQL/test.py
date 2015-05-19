"""
SQL Bootcamp test program 
The IPython notebook SQL_Intro.ipnb uses SQL_support_code.py.  
This program checks to see that it's in the same directory, also some
other checks while we're at it.  

Written by Dave Backus, March 2015  
Created with Python 3.4 
"""
"""
Check Python version 
"""
# https://docs.python.org/3.4/library/sys.html
import sys
print('What version of Python? \n', sys.version, '\n', sep='') 
if float(sys.version_info[0]) < 3.0 :       
    raise Exception('***** Program halted, old version of Python *****')

#%%
"""
Check path of current working directory (just for the heck of it)  
"""
# https://docs.python.org/2/library/os.path.html
import os 

print('Current path:\n', os.getcwd(), sep='')
#print('Full name of this file:\n', __file__, '\n', sep='')

"""
Check for support code 
""" 
# https://docs.python.org/3.4/library/os.html
import os

print('List of files in working directory:')
[print(file) for file in os.listdir()]

if not os.path.isfile('SQL_support_code.py'):
    raise Exception('***** Program halted, support code missing *****')

#%%
"""
Crude fix for missing support code (add to above, automate?)
"""
# https://docs.python.org/3/library/urllib.request.html
import urllib.request           
file = 'foo.py'
url1 = 'https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/'
url2 = 'master/SQL/SQL_support_code.py'
url = url1 + url2
urllib.request.urlretrieve(url, file)   # copy url to file 

print('Is file there now?', os.path.isfile('foo.py'))

#%%
"""
Combination: check for file, download if missing  
"""
import urllib.request     
import os

# Add '_x' to name so we can test without destroying the original 
file = 'SQL_support_code_x.py'
if not os.path.isfile(file):
    print('\n***** Support code missing, downloading replacement *****')
    url1 = 'https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/'
    url2 = 'master/SQL/SQL_support_code.py'
    url = url1 + url2
    urllib.request.urlretrieve(url, file)    
    if os.path.isfile(file): 
        print('***** File successfully downloaded *****')
