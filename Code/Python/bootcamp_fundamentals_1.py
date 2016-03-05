"""
Python fundamentals, part 1, for Data Bootcamp course.

Course materials
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp

Warning:  This is a working file and has some things in it that aren't
completely debugged.

Written by Dave Backus, August 2015
Created with Python 3.4
"""
"""
Check version (ignore this, just run it)
"""
import sys

print('\nWhat version of Python? \n', sys.version, '\n', sep='')

if float(sys.version_info[0]) < 3.0:
    raise Exception('Program halted, old version of Python. \n',
                    'Sorry, you need to install Anaconda again.')
else:
    print('Congratulations, Python is up to date!')

#%%
"""
Explore Spyder:  editor, IPython console, etc
"""

"""
Calculations:  type in IPython console, practice "Google fu"
"""
# 2*3, 2 * 3, 2/3, 2^3, 2**3, log(3), sqrt(2)

# Exercises

"""
Assignments:  type in IPython console
* what's on the right is "assigned" to the object on the left
* we call the object a "variable"
* variables can be used again, refer to them by name
"""
x = 2
y = 3
z = x/y
z

# Exercises

"""
The print() function
* what's inside the parens gets printed -- the "arguments"
* as many as you like
* for help:  print? or Object explorer
"""
print(z)
print(x, y, z)

"""
Strings = collections of characters between quotes
"""
a = 'some'      # think Excel
b = 'thing'
c = a + b
print(c)        # what happened here?

message = 'The value of z is'
print(message, z)

# Exercises

#%%
"""
Single, double, and triple quotes (are mostly the same)
"""
# how to use single, double, and triple quotes
d = 'example'
e = "example"
d == e           # mysterious but informative

# triple quotes work, too, even over lines

# Exercises

"""
Comments:  everything in a line after a hash (#) is a comment (ignored)
Good practice:  add comments to your code to remind yourself what you did
"""
# this is a comment
x = 2   # so is this

#%%
"""
Running code in Spyder
* type things in the editor
* run with the green triangles in the toolbar
* code cells marked by #%%
Open new file, save as bootcamp_topic2.py in Data_Bootcamp
Add this code and run it
"""
x = 2
y = 3
z = x/y
print('z =', z)
#%%
a = 'some'
b = 'thing'
c = a + b
print('c = ', c)

#%%
"""
Lists:  collections of things in square brackets (numbers, strings, etc)
"""
numberlist = [1, 5, -3]
stringlist = ['hi', 'hello', 'hey']

# try print, what do you see?

a = 'some'
b = 'thing'
c = a + b
variablelist = [a, b, c]

randomlist = [1, 'hello', a]
strings = [a, b, c]

both = numberlist + stringlist
print(both)

# Exercises

#%%
"""
Functions
* print()
* type()
* len()
Getting help:  function? in console, function in Object inspector
"""

# try type on:  2, 2.5, 'something', c, stringlist, '12', '12.34'

# Exercises

# conversions:  float, int, str
f = float('12.34')
type(f)
i = int('12.34')
type(i)

# Exercises

#%%
"""
Objects and methods
* syntax:  function(object), object.method
* find methods using "tab completion" in the console
* get help with object.method? or object explorer
"""
name = 'Spencer'
numbers = [1, 2, 3, 4]

# tab completion, more help

# Example
firstname = 'Chase'
firstname.lower()

# Exercises

"""
Review
"""
