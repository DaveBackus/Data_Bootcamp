"""
Scratch pad for Data Bootcamp class 
Type everything here rather than the console 
"""
x=1
y=2
z=3
m=4

def pocket_change(x, y, z, m):
    dollars = (x + y*5 + z*10 + m*25)/100
    return dollars 

ans = pocket_change(1,2,3,4)
print('$', ans, sep='')

#%%
print("$", ans)