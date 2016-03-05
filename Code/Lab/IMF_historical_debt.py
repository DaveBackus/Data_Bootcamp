"""
IMF historical debt data
https://www.imf.org/External/pubs/cat/longres.aspx?sk=24332.0
rows are countries, columns are dates (1692-2012)

Prepared for Data Bootcamp course at NYU
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python

Written by Hersh Iyer and Itamar Snir, November 2015
Created with Python 3.5
"""
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

# data input
excelFilePath = '../Temp/Debt Database Fall 2013 Vintage.xlsx'
debt = pd.read_excel(excelFilePath, sheetname=1, na_values=['…', '….', ''])

debt = debt.drop([debt.columns[1], debt.columns[2]], axis=1)

countries = ['Greece', 'United Kingdom      ', 'United States']
some = debt[debt['country'].isin(countries)]
some = some.set_index('country').T

ax = some[countries[1]].plot(color='red')
some[countries[0]].dropna().plot(color='blue')
some[countries[2]].dropna().plot(color='green')
ax.set_title('Ratio of government debt to GDP', fontsize=14, loc='left')
ax.set_ylabel('Percent')
ax.legend(['Greece', 'United Kingdom', 'United States'], loc='upperleft', fontsize=10)

#%%
ax = some.dropna().plot()


#%%
# OLD VERSION BELOW

# data input
excelFilePath = '../Temp/Debt Database Fall 2013 Vintage.xlsx'
df = pd.read_excel(excelFilePath, sheetname=1, na_values=['…', '….', '']) #, index_col=-1,
                   #encoding='utf-8')

#%%
"""
plots
"""
### UK debt to GDP since 1800

#construct the years for the x-axis values
years = [year for year in range(1800,2013)]
#get a list of the debt to GDP for the y-axis values
# next line fails, not sure why
dbt_UK = df[df.country=='United Kingdom      '][years] #note the extra spaces in 'United Kingdom     '
dbt_uk_list = dbt_UK.values.tolist()[0] #note the conversion to a list (required to convert data to be 1 dimensional)

#%%
#plot the data
plt.plot(years,dbt_uk_list) #use graph in default color
plt.ylabel ("debt to GDP")
plt.xlim((1800, 2012))  #for aesthetics, make sure x-axis shows only the relevant years
plt.title("United Kingdom Debt to GDP Between 1800 and 2012")
plt.show()

#%%
### Greece debt to GDP since 1980

#get most recent year in the data (instead of 2013):
max_year = max(df.columns.values[4:].tolist())

#get a list of the years for the x-axis values
years = [year for year in range(1980,max_year+1)]
#get a list of the debt to GDP for the y-axis values
dbt_greece = df[df.country=='Greece'][years]
dbt_greece_list = dbt_greece.values.tolist()[0]
#plot the data
plt.plot(years,dbt_greece_list, color='red') #set graph color
plt.ylabel('Debt to GDP')
plt.title ('Greece Debt to GDP Between 1980 and '+ str(max_year))
plt.show()

