"""
Python fundamentals, part 2, for Data Bootcamp course.

Course materials
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp

Warning:  This is a working file and has some things in it that aren't
completely debugged.

Written by Dave Backus, August 2015
Created with Python 3.4
"""
"""
Check Python version
"""
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

name1 = 'Chase'
name2 = 'Spencer'
check =  name1 >= name2
print('check =', check)

notcheck = not check
print('notcheck =', notcheck)

#%%
"""
Slicing:  picking out elements of strings, lists
Write out string, put numbers under it
"""
# slicing
a = 'some'
b = 'thing'
c = a + b
print('c is', c)

# what is c[1]?  why?  c[0]?  c[-1]


#%%
"""
Loops
"""
sum = 0
for num in range(11):
    sum = sum + num

print('\nSum of first 10 integers =', sum)

#
maxnum = 20 			     # guess number above our limit
sum = 0
for num in range(maxnum):
    sum = sum + num
    if sum > 100:
        break  			# exit loop

print('\nAt num =', num, 'we had sum =', sum)

# loops over lists
numlist = [4, -2, 5]

sum = 0
for num in numlist:
    sum = sum + num

print('\nSum of numbers in list =', sum)

# bond price
maturity = 20
coupon = 2
ytm    = 0.05

price = 0
for year in range(1, maturity+1):
    price = price + coupon/(1+ytm)**year

# add principal
price = price + 100/(1+ytm)**maturity
print('\nThe price of the bond is', price)

# loops over strings
vowels = 'aeiouy'
word   = 'anything'
print('\nVowels in', word, ': ', end='')
for letter in word:
    if letter in vowels:
        print(letter, end=' ')

# consonants:  note the "not"
print('\nConsonants in', word, ': ', end='')
for letter in word:
    if letter not in vowels:
        print(letter, end=' ')

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

#------------------------------------------------------------------------------
# EXTRA STUFF, NOT USED
#------------------------------------------------------------------------------
"""
map, reduce, and filter
"""
anyoldlist = [2, 'Steelers', [1,5]]
t = map(type, anyoldlist)
types = list(t)
print('\nResult of map:\n', types, sep='')

from functools import reduce
numlist = [4, -2, 5]
z = reduce(lambda x,y: x+y, numlist)
print('Result of reduce (sum):', z)

numlist = [4, -2, 5]
f = filter(lambda x:  x > 0, numlist)
newlist = list(f)
print('Result of filter (find positive numbers):', newlist)

anylist = [2, 'Steelers', [1,2,3]]
f = filter(lambda x: type(x) == str, anylist)
newlist = list(f)
print('Result of filter (find strings):', newlist)

#%%
"""
copies
"""
print('\nAssignments and copies')

x = [1,2,3]
print('x =', x)

y = x
x[0] = 'WHOA!'
print('After changing x[0]: y =', y)

y[2] = 'xyzzy'
print('After changing y[2]: x =', x)

x = [1,2,3]
y = x.copy()
x[0] = 'WHOA!'
print('y =', y)

