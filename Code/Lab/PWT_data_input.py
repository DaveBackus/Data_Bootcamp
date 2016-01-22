"""
Penn World Table 
http://www.rug.nl/research/ggdc/data/pwt/ 

Prepared for Data Bootcamp course at NYU  
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab 

Written by Dave Backus, January 2016  
Created with Python 3.5 
"""
import pandas as pd

# data input
url = 'http://www.rug.nl/research/ggdc/data/pwt/v81/pwt81.xlsx'
pwt = pd.read_excel(url, 
                    sheetname='Data', 
                    parse_cols=[0,1,3,5,6,7,8,14])

list(pwt)

#%%
# create smaller spreadsheet for teaching 
nyu = pwt[[1,0,2]].copy()
nyu['POP'] = pwt['pop']
nyu['L/POP'] = pwt['emp']/pwt['pop']
nyu['Y/POP'] = pwt['rgdpo']/pwt['pop']
nyu['Y/L'] = pwt['rgdpo']/pwt['emp']
nyu['K/L'] = pwt['ck']/pwt['emp']
nyu['K/Y'] = pwt['ck']/pwt['rgdpo'] 
nyu['Hours'] = pwt['avh']

nyu.to_excel('pwt81_nyustern.xls', index=False, sheetname='PWT 8.1')

#%%