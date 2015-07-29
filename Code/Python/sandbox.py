# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:58:56 2015

@author: dbackus
"""
w = 2*3 
x = 2**3 
y = x/w
z = a/x 

#%%
import matplotlib.pyplot as plt

# http://matplotlib.org/users/style_sheets.html
print(plt.style.available)
plt.style.use('ggplot')
plt.style.reload_library()  # does this reset default?  



#%%
# http://www.reddit.com/r/Python/comments/3bgjud/you_sit_down_with_your_machine_and_a_person_who/
import turtle 
turtle.forward(100)
turtle.left(90) 
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)