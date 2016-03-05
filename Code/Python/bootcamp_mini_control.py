"""
For Class #3 of an informal mini-course at NYU Stern, Fall 2014.

Topics:  control flow, functions

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp

Prepared by Dave Backus, Sarah Beckett-Hile, and Glenn Okun
Created with Python 3.4
"""

"""
Reminders
"""
x, y, z = 2*3, 2**3, 2/3    # yes, three at once!
a, b = 'some', 'thing'
c = a + b

numbers = [x, y, z]
strings = [a, b, c]
both = numbers + strings
print(both)
print(both[:3] + both[3:])

[print(element) for element in both]
[print(c[item]) for item in range(9)]
#%%
"""
Conditional statements:  if, else, elif
"""
# if statement
x = 5       # we can change this later and see what happens
if x > 6:
    square = x**2
    print('x**2 =', square)

print('Done!')

#%%
# if and else statements
x = 25
if x > 6:
    square = x**2
    print('x**2 =', square)
    print(x>6)
else:
    print('x is not > 6 ( x =', x, ')')
    print(x>6)

print('Done!')

#%%
name1 = 'Dave'
name2 = 'Allan'

if name1 > name2:
    print(name2)
else:
    print(name1)

#%%
"""
Loops
"""
# simple loop
for number in range(11):
    square = number**2
    print(square)

#%%
# Fibonacci numbers
print('\nFibonacci numbers')    # \n skips to the next line
a, b = 0, 1
for it in range(20):
    a, b = b, a+b
#    print('At iteration', it, 'b =', b)
    print('Ratio', a/b)

#%%
sum = 0
for num in range(1,11):
    sum += num
    print(sum)

#%%
a, b = 0, 1
ratio = a/b
maxit = 20
small_num = 1e-4
for it in range(maxit):
    a, b = b, a+b
    new_ratio = a/b
    print('At iteration', it, 'ratio =', new_ratio)
    if abs(new_ratio-ratio) < small_num:
        break       # stop and exit loop break
    else:
        ratio = new_ratio

#%%
# while loop
a, b = 0, 1
ratio = a/b
maxit = 20
small_num = 1e-4
error = 20
while error > small_num:
    a, b = b, a+b
    new_ratio = a/b
    print('At iteration', it, 'ratio =', new_ratio)
    error = abs(new_ratio-ratio)
    ratio = new_ratio

#%%
a, b = 0, 1
while b < 100:
    print('b =', b)
    a, b = b, a+b

#%%
# looping over strings and lists
vowels = 'aeiouy'
word   = 'anything'
for letter in word:
    if letter not in vowels:
        print(letter)

#%%
# loop over list
fruit = ['apples', 'bananas', 'cherries']
for item in fruit:
    print(item)

#%%
fruit = ['apples', 'bananas', 'cherries']
together = ''       # empty string
for item in fruit:
    print(item)
    together = together + item

print(together)
#%%

# list comprehension
[print(item) for item in fruit]

print('Done!')

#%%
"""
Functions
"""
# some other time

def fibonacci(a, b):
    a, b = b, a+b
    return a, b

a, b = 0, 1
a, b = fibonacci(a, b)

print(a, b)
