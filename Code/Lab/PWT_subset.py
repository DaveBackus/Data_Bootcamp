"""
Penn World Table 
http://www.rug.nl/research/ggdc/data/pwt/ 

Prepared for Data Bootcamp course at NYU  
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Hersh Iyer and Itamar Snir, November 2015 
Created with Python 3.5 
"""
import pandas as pd
import matplotlib.pyplot as plt

# data input
url = 'http://www.rug.nl/research/ggdc/data/pwt/v81/pwt81.xlsx'
pwt = pd.read_excel(url, sheetname='Data')

#%%
#pwt.to_excel('pwt81.xls')