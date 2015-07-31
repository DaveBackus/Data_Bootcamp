"""
Python fundamentals, part 1, for Data Bootcamp course.  

Repository of materials (including this file): 
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python 
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python  

Written by Dave Backus, August 2015 
Created with Python 3.4 
"""
"""
Check versions 
"""
import sys 
import pandas as pd 

print('\nPython version: ', sys.version) 
print('\nPandas version: ', pd.__version__) """
Check Python version 
"""
# https://docs.python.org/3.4/library/sys.html
import sys 

print('\nWhat version of Python? \n', sys.version, '\n', sep='') 

if float(sys.version_info[0]) < 3.0 :       
    raise Exception('Program halted, old version of Python. \n', 
                    'Sorry, you need to install Anaconda again.')
else:
    print('Congratulations, Python is up to date!')
    
#%%    
"""
Calculations and assignments (best in IPython console)   
"""
2*3
2 * 3
2^3
log(3) 


#%%
"""
Strings  
"""
a = 'some'
b = 'thing'
c = a + b 
print('c = ', c)

print('c[1] is:', c[1])
print('c[1:2] is', c[1:2])
print('c[1:3] is:', c[1:3])
print('c[1:] is:', c[1:])


#%%

#print(['a[1:3]', a[1:3]])

# names 
first, last = 'Dave', 'Backus'
full = first + ' ' + last

#%%
longstring = """
Four score and seven years ago
Our fathers brought forth """
print(longstring)

#%%
"""
Output and input 
"""
print(full)
print(first, last)
print(last, ', ', first)
print(last, ', ', first, sep='')

#x = input('Type your name here --> ')
#print(x, end='\n\n') 

"""
Lists 
"""
numbers = [x, y, z]
strings = [a, b, c]

both = numbers + strings
print(['both[3:]', both[3:]])

#%%
"""
Functions 
"""
def hello(firstname):
    print('Hello, ', firstname)
    
hello('Dave')

#%%
def combine(first, last): 
    lastfirst = last + ', ' + first 
    return lastfirst 

both = combine('Chase', 'Coleman')
print(both)

