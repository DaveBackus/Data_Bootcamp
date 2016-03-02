"""
Scratch pad for Data Bootcamp class 
Type everything here rather than the console 
"""
import pandas as pd 

print('Pandas version:', pd.__version__)

#%%
# read file from url
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2
df = pd.read_csv(url)

# if the internet is down 
#df_fromdict = pd.DataFrame({'name': ['Dave', 'Chase', 'Spencer'], 
#            'x1': [1, 4, 5], 'x2': [2, 3, 6], 'x3': [3.5, 4.3, 7.8]}) 

#%%
