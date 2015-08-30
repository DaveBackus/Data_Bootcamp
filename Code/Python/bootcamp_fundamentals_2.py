"""
Python fundamentals, part 2, for Data Bootcamp course.  

Repository of materials (including this file): 
* https://github.com/DaveBackus/Data_Bootcamp/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python  

Written by Dave Backus, August 2015 
Created with Python 3.4 
"""
"""
Check Python version
"""
import sys 
import pandas as pd 

print('\nPython version: ', sys.version) 

import sys 

print('\nWhat version of Python? \n', sys.version, '\n', sep='') 

if float(sys.version_info[0]) < 3.0 :       
    raise Exception('Program halted, old version of Python. \n', 
                    'Sorry, you need to install Anaconda again.')
else:
    print('Congratulations, Python is up to date!')
    
#%%    
"""
Comparisons 
"""
x = 2*3
y = 2**3 
test = x >= y
print('x >= y = ', test, 'and has type', type(test))

#%%
name1 = 'Chase' 
name2 = 'Spencer' 
check =  name1 >= name2 

#%%
print(not check)

#%%
"""
Loops
"""
sum = 0 
for num in range(11):
    sum = sum + num 

print(sum)

#%%
maxnum = 20 			     # guess number above our limit 

sum = 0 
for num in range(maxnum):
    sum = sum + num 
    if sum > 100:
        break  			# exit loop 

print('At num =', num, 'we had sum =', sum)
#%%
numlist = [4, -2, 5] 

sum = 0
for num in numlist:
    sum = sum + num 
    
print(sum)     
#%%

maturity = 20 			
coupon = 2 			 
ytm    = 0.05 

price = 0 
for year in range(1, maturity+1):
    price = price + coupon/(1+ytm)**year

price = price + 100/(1+ytm)**maturity 
print('The price of the bond is', price)

#%%
vowels = 'aeiouy'
word   = 'anything'
for letter in word:
    if letter in vowels:
        print(letter)
#%%
vowels = 'aeiouy'
word   = 'anything'
for letter in word:
    if letter not in vowels:
        print(letter)
        
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

#%%
"""
map, reduce, and filter 
"""
anyoldlist = [2, 'Steelers', [1,5]]
t = map(type, anyoldlist) 
types = list(t)

from functools import * 
numlist = [4, -2, 5]
z = reduce(lambda x,y: x+y, numlist)

numlist = [4, -2, 5]
f = filter(lambda x:  x >= 0, numlist) 
newlist = list(f)

#%%
anylist = [2, 'Steelers', [1,2,3]]
f = filter(lambda x: type(x) == str, anylist)
newlist = list(f)

#%%
"""
copies 
"""
x = [1,2,3]
y = x
x[0] = 'WHOA!'
print(y)

y[2] = 'xyzzy'
print(x)


x = [1,2,3]
y = x.copy()
x[0] = 'WHOA!'
print(y)
