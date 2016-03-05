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
df2 = pd.read_csv(url, index_col=0)
print(df2)
#%%
df2 = pd.read_csv(url, na_values=[1, 6])
print(df2)
#%%
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.xlsx'
url_xls = url1 + url2
dfx = pd.read_excel(url_xls)
print(dfx)
#%%
# Print data frame
print(df)

# leave space for new list
new_cols = [x.replace("x", "y") for x in df.columns]

df.columns = new_cols

print(df)

#%%
file = 'C:\\Users\\dbackus\\Dropbox\\Documents\\Classes\\Data_Bootcamp\\Code\\Python\\test.csv'
dfhd = pd.read_csv(file)
