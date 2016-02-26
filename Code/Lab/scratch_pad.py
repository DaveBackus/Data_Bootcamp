# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:31:33 2016

This is class 3 from databootcamp class

@author: dbackus
"""
import pandas as pd
#%%
# read file from url
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2
df = pd.read_csv(url)
df["total"] = df["x1"] + df["x2"] + df["x3"]
df2 = pd.read_csv(url, na_values=[1])

#%% making column names upper case
col_names = list(df)
title_names = [x.title() for x in col_names]
df3 = df.copy()
df3.columns = title_names

# OR... 
# WARNING the code below will change df itself
# df.columns = [x.title() for x in list(df)]

#%% renaming a column
df4 = df.rename(columns={"x1": "Sales"})

#%% extracting multiple columns
namelist = ["Sales", "total"]
sales_df = df4[namelist]

#%% Exercises at the bottom of 66
xx = df["x1"] + df["x2"] + df["x3"]
df["z"] = xx 
print(df)

# 2nd exercise
namelist = ["x1", "x2"]
df[namelist]

df[["x1", "x2"]]  # equivalent to above

# 3rd exercise
df.drop(["z"], axis=1)

# 4th exercise
df.rename(columns={"x3": "X3", 
                   "x2": "X2", 
                   "x1": "X1"})

#%% DataFrame methods
# write data to csv file on computer
df.to_csv("new_file.csv")  # new_file.csv is name

df.head(2)  # new DataFrame with first 2 rows of df
df.tail(2)  # new DataFrame with last 2 rows of df

# set index (row labels) to be the names
named_df = df.set_index("name")

# undo changing of index -- should match df
unnamed_df = named_df.reset_index()




