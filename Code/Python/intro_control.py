"""
Python language basics   

# assignments: x=7, x='foo', 7*5, 'foo'*2, 7**2, multiples, but no log/exp/sqrt
print and strings
lists: examples, type, element numbering
**slicing
loops
list comprehensions
if/then..

References
* https://docs.python.org/3/tutorial/introduction.html
* 

Written by Dave Backus @ NYU, August 2014  
Created with Python 3.4 
"""

"""
Numbers and strings
"""
# numbers 
a = 7
print(a) 
type(a)

b = a/3
print(b)
type(b)

# to square b
b**2

#sqrt?  log? 

# multi assignments 
f, g = 9, 27

# strings 
c = 'Dave'
print(c*2)

# elements 
c[1]
c[0]
c[-1]
c[-4]
# c[-5]?

# slicing
c[0:2]
c[0:-1] 
c[:-1]
c[-1:]
c[:] 

# properties 
n = len(c)

d = 'B'
print(c + d)
print(c + 2*d) 
print(c[0:2]+c[1:n])
print(c[0:2]+c[3:n])
print(c[0:2]+c[2:n])

# more compact notation
print(c[:2]+c[1:])
print(c[:])


#%%
"""
Lists
"""
x = [a, b, c]
print(x)
print(type(x))

print(['The type of x is ', type(x)])

# change or replace an element 

#  what if we multiply x by 2, or square it?

# apply len
len(x)

# lists of lists!
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]


# what is a+n?  

# what is x[0]?  x[0][1]?



#%%