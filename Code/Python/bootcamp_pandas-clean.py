"""
Data cleaning with Pandas for Data Bootcamp course.

Course materials
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp

Warning:  This is a working file and has some things in it that aren't
completely debugged.

Written by Dave Backus, February 2016
Created with Python 3.5
"""
import pandas as pd

data = {'EG.ELC.ACCS.ZS': [53.2, 47.3, 85.4, 22.1],    # access to elec (%)
        'IT.CEL.SETS.P2': [153.8, 95.0, 130.6, 74.8],  # cell contracts per 100
        'IT.NET.USER.P2': [11.5, 12.9, 41.0, 13.5],    # internet access (%)
        'Country': ['Botswana', 'Namibia', 'South Africa', 'Zambia']}
af = pd.DataFrame(data)

#%%
"""
entry poll
"""
import pandas as pd

url1 = 'http://pages.stern.nyu.edu/~dbackus/Data/'
url2 = 'Data-Bootcamp-entry-poll_s16.csv'
url = url1 + url2
file = url2

ep = pd.read_csv(url, header=0) #, names=variables)
print('Dimensions:', ep.shape)
print('Variables:\n', list(ep), sep='')

#%%
# new variable names
variables = ['Time', 'Program', 'Career', 'Programming experience',
             'Prob-stat experience', 'Social media', 'Other',
             'Concentration', 'Interests', 'Why', 'Extra Topics']

#%%
"""
Chipotle
"""
url = 'https://raw.githubusercontent.com/TheUpshot/chipotle/master/orders.tsv'
chp = pd.read_csv(url, sep='\t')   # tab (\t) delimited
chp.shape

print('Dimensions:', chp.shape)
print('Variable dtypes:\n', chp.dtypes, sep='')
print(chp.head())

#%%
"""
OECD docs data
"""
url1 = 'http://www.oecd.org/health/health-systems/'
url2 = 'OECD-Health-Statistics-2015-Frequently-Requested-Data.xls'

docs = pd.read_excel(url1+url2,
                   skiprows=3, sheetname='Physicians', index_col=0,
                   skip_footer=21)

#%%
print('Dimensions:', docs.shape)
print('Variable dtypes:\n', docs.dtypes, sep='')
print(docs.head())

#%%
"""
WEO
"""
url1 = 'http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/'
url2 = 'WEOApr2015all.xls'
url = url1 + url2
weo = pd.read_csv(url, sep='\t') #, thousands=',', na_values=['n/a', '--'])

#%%
small = weo[list(weo[list(range(15))])]
print('Variable dtypes:\n', small.dtypes, sep='')
print('\nFirst 9 variables:\n', small[list(range(9))].head(), sep='')
print('\nNext 3 variables (data):\n', small[list(range(9,15))].head(), sep='')

#%%

list(weo[list(range(12))])

#%%
"""
bond yields
Fed url: http://www.federalreserve.gov/econresdata/researchdata/feds200628.xls
Converted manually to csv and uploaded.
Comment:  data has xls extension but is really an xml file, so can't use
read_excel.
"""
url = 'http://pages.stern.nyu.edu/~dbackus/Data/feds200628.csv'
gsw = pd.read_csv(url,
                  skiprows=9,
#                  nrows=50,
                  index_col=0,
                  usecols=list(range(31)),
                  parse_dates=0)

#%%
print('Index:\n', gsw.index, sep='')
print('Variable dtypes:\n', gsw.dtypes, sep='')

