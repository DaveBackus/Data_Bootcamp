"""
Python fundamentals, part 1, for Data Bootcamp course.  

Repository of materials (including this file): 
* https://github.com/DaveBackus/Data_Bootcamp/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python  

Written by Dave Backus, August 2015 
Created with Python 3.4 
"""
"""
Check version (ignore this, just run it)
Or just type:  import sys, sys.version 
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
Calculations:  type in IPython console
"""
# 2*3, 2 * 3, 2/3, 2^3, 2**3, log(3), sqrt(2)

"""
Assignments:  type in IPython console 
* what's on the right is "assigned" to the object on the left 
* we call the object a "variable"
* variables can be used again, refer to them by name 
"""
x = 2   
y = 3 
z = x/y

# Exercise: Suppose we borrow 200, pay interest of 5%.  
# If we pay interest plus principal after one year, what do we pay? 
# Use the variables "principal" and "i". 

# Exercise: GDP was 15.58 in 2013, 15.96 in 2014.  What was the growth rate?
# Use the variables "gdp13", "gdp14", and "growth" 

"""
Hashes (#):  everything in a line after a hash is a comment, ignored by Python
Good practice:  add comments to your code to remind yourself what you did
"""
# this is a comment
x = 2   # so is this 

#%%
"""
The print() function 
* what's inside the parens is what we print -- the "arguments" 
* as many as you like 
* for help:  print?
"""
# type these lines in IPython console 
print(x)
print(x, y)
print('The variable x is', x)

#%%
"""
Running code in Spyder 
* Type things in the editor
* code cells marked by #%%
"""

#%%
"""
Strings = collections of characters 
They show up a lot in data work (variables, data) 
"""
a = 'some'      # think Excel 
b = 'thing'
c = a + b 
print(c)        # what happened here?  

#%%
"""
Single, double, and triple quotes (are mostly the same)
"""
# how to use single, double, and triple quotes 
d = 'example'
e = "example"
d == e                      # just to check, ignore how this works 
longstring = """
Four score and seven years ago
Our fathers brought forth """

# combining strings
first = 'Sarah'
last  = 'Beckett-Hile'
bothnames = first + last 
print(bothnames)

# Exercise:  How do I fix bothnames?

# Exercise:  Construct the string:  last name, comma, space, first name 

#%%
"""
Lists:  collections of things (numbers, strings, etc) 
"""
x = 2
y = 2**3
z = x/y 

a = 'some'
b = 'thing'
c = a + b

numbers = [x, y, z]
strings = [a, b, c]

both = numbers + strings
print(both)

#%%
"""
Built-in functions:  like print, but we have others 
Favs:  type, len
Getting help:  type? in console, type in Object inspector
"""
d = '11.32'

# Exercise.  What type is d?  What is its length?

# Exercise.  What do the functions int and str do?  
# Convert d to a float. 

#%%
"""
Objects and methods 
* find methods using "tab completion" in the console
* get help with object.method? or object explorer 
"""
name = 'Spencer'
numbers = [1, 2, 3, 4]

# Exercise.  What do name.lower() and name.upper() do?  

# Exercise. Replace e's with *'s.  

