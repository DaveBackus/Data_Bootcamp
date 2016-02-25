# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:31:33 2016

This is class 3 from databootcamp class

@author: dbackus
"""
qualified = False


#%%
if qualified:
    print('accept')
else:
    print('reject')

#%%
print('Done!')

#%%
if 1<0:
    print('1 is less than 0')


#%%
name1 = 'Chase'
name2 = 'Dave'

if name1<name2:
    print(name1)
else:
    print(name2)

#%%
l = ['a', 'A', 'Chase', 'c', 'Glenn']
sorted(l)

#%%
namelist = ["Chase", "Dave", "Sarah", "Spencer"]

for item in namelist
    print(item)

#%%
numlist = [4, -2, 5, 7, 1, 3, 4, -15, -20]
total = 0
n = len(numlist)

for x in numlist:
    total = total + x
    
print(total/n)

#%%
vowels = 'aeiouy'
word = 'anything'

for letter in word:
    if (letter in vowels):
        print('Vowel: ', letter)
    else:
        print('Consonant: ', letter)

#%%
stuff = ["Cat", 3.7, 5, "Dog"]

#%%
for thing in stuff:
    print(thing)

#%%
for thing in stuff:
    print(type(thing))
    
#%%
for thing in stuff:
    if type(thing) is str:
        print(thing)

#%%
for el in range(5):
    print(el)
    
for year in range(1980, 2016):
    print(year)
    
#%%
maturity = 5
coupon = 5
ytm = 0.05

price = 0
for year in range(1, maturity+1):
    price = price + coupon/(1+ytm)**year
    
price = price + 100/(1+ytm)**maturity
print('The price of the bond is: $', price)

#%%
fruit = ["apple", "banana", "clementine", "pineapple"]

FRUIT = [item.upper() for item in fruit]

#%%
def hello(firstname):
    print('Hello,', firstname)

hello('Chase')
hello(1)
hello('Class')

#%%
def bondprice(maturity):
    coupon = 5
    ytm = 0.05

    price = 0
    for year in range(1, maturity+1):
        price = price + coupon/(1+ytm)**year

    price = price + 100/(1+ytm)**maturity
    
    return price
    
p = bondprice(5)
print(p)

#%%
def older_than_30(age):
    true_or_false = age >= 30
    return true_or_false

print(older_than_30(5))
print(older_than_30(45))

ages = range(50)
for age in ages:
    if older_than_30(age):
        print(age, "is older than 30")

#%%
def nextyear(year):
    return str(year+1)
    
print(nextyear(2015))

#%%
