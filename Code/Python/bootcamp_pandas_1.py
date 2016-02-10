"""
Data input with Pandas for Data Bootcamp course.  

Course materials 
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp 

Warning:  This is a working file and has some things in it that aren't
completely debugged.

Written by Dave Backus, August 2015 
Created with Python 3.4 
"""
"""
Read csv file from internet (and why we like csv's)
The result is a data frame:  like a sheet with row and column labels
"""
import pandas as pd               # redundant, but it's ok to do it again 

# read file from url
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2
df = pd.read_csv(url, nrows=2)

print('\nurl read (df)\n', df)    # \n tells print to skip a line

# if the internet is down 
#df_fromdict = pd.DataFrame({'name': ['Dave', 'Chase', 'Spencer'], 
#            'x1': [1, 4, 5], 'x2': [2, 3, 6], 'x3': [3.5, 4.3, 7.8]}) 

#%%
"""
Exercises
* xlsx 
* na_values
"""
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.csv'
url  = url1 + url2
dfex = pd.read_csv(url, na_values=[1])

#%%
"""
xls annd xlsx files 
"""
url1 = 'https://raw.githubusercontent.com/DaveBackus'
url2 = '/Data_Bootcamp/master/Code/Python/test.xls'
url  = url1 + url2
dfx = pd.read_excel(url)

print('\nurl read (df)\n', dfx)    # \n tells print to skip a line

#%%
"""
What type of object do we have?  What are its properties?
"""
type(df)
df.head(2) 
df.columns
df.index
df.index.tolist()
list(df) 

#%%
"""
Playing with variables:  select variables, create new ones, plot them
"""
# what is this?
df['x1']

#%%
# construct new variables
df['y1'] = df['x1']/df['x2']
df['y2'] = df['x2'] + df['x3']

#%%
# Exercise.  Use the dtypes method.  What does it tell us?

# Exercise.  What does this do?
# df = df.set_index('Name')


#%%
# sort by y1
df.sort_values(['y1'])

#%%
# this is cool, but not recommended (goes against the automation mentality)
df.to_clipboard()


#%%
"""
Data input from your computer 
Create or find Data_Bootcamp directory 
Create spreadsheet, save as xlsx, xls, csv 
Locate and set current working directory 
"""
import pandas as pd          # still redundant

# read files from computer
# make sure they're in the current working directory
file1 = 'test.xlsx'
df1 = pd.read_excel(file1)
print('\nxlsx read\n', df1)

file2 = 'test.xls'
df2 = pd.read_excel(file2)
print('\nxls read\n', df2)

file3 = 'test.csv'
df3 = pd.read_csv(file3)
print('\ncsv read\n', df3)

#%%
"""
complete path using os module  
"""
import os 

file = 'test.csv'
path = 'C:/Users/dbackus/Dropbox/Documents/Classes/Data_Bootcamp/Code/Python'

os.chdir(path)
print('Current working directory', os.getcwd())

#%%
# check to see if file exists
#exists = os.path.isfile(path1 + '/' + file) 
exists = os.path.isfile(file) 
print('File exists?', exists)

#%%
if exists==False:
    raise Exception('File does not exist, execution halted')    



file = 'C:\\Users\\dbackus\\Dropbox\\Documents\\Classes\\Data_Bootcamp\\Code\\Python\\test0.csv'

dfhd = pd.read_csv(file)

#%%
"""
Penn World Table:  macroeconomic data for countries, annual from 1950
http://www.rug.nl/research/ggdc/data/pwt/?lang=en
Takes about 15 seconds with a fast ethernet connection 
"""
import pandas as pd 
url = 'http://www.rug.nl/research/ggdc/data/pwt/v81/pwt81.xlsx'
pwt = pd.read_excel(url, sheetname='Data')


#%%
"""
World Economic Outlook:  macroeconomic data for countries, annual from 1980   
https://www.imf.org/external/ns/cs.aspx?id=28
"""
import pandas as pd

url1 = 'https://www.imf.org/external/pubs/ft/weo/'
url2 = '2015/02/weodata/WEOOct2015all.xls'
weo = pd.read_csv(url1+url2, 
                  sep='\t',                 # \t = tab 
                  thousands=',',            # kill commas 
                  na_values=['n/a', '--'])  # missing values 

list(weo)


#%%
"""
Government debt:  IMF historical data on ratio of debt to GDP
https://www.imf.org/external/pubs/cat/longres.aspx?sk=24332.0
This doesn't work, won't unzip file in read function.
"""
import pandas as pd

url = 'https://www.imf.org/external/pubs/ft/wp/2010/Data/wp10245.zip'
df = pd.read_excel(url, sheetname=1, na_values=['…', '….', ''])


#%%
"""
PISA education data 
"""
import pandas as pd
url = 'http://dx.doi.org/10.1787/888932937035'
pisa = pd.read_excel(url, 
                     skiprows=18,       # skip the first 18 rows 
                     skipfooter=7,      # skip the last 7 
                     parse_cols=[0,1,9,13],   # select columns of interest 
                     index_col=0,       # set the index as the first column
                     header=[0,1]       # set the variable names 
                     )
pisa = pisa.dropna()                    # drop blank lines 
pisa.columns = ['Math', 'Reading', 'Science']   # simplify names 

pisa['Math'].plot(kind='barh')

#%%
"""
UN population projections 
http://esa.un.org/unpd/wpp/Download/Standard/Population/
"""
url1 = 'http://esa.un.org/unpd/wpp/DVD/Files/'
url2 = '1_Indicators%20(Standard)/EXCEL_FILES/1_Population/'
url3 = 'WPP2015_POP_F07_1_POPULATION_BY_AGE_BOTH_SEXES.XLS'
url = url1 + url2 + url3 

cols = [2, 4, 5] + list(range(6,28))
est = pd.read_excel(url, sheetname=0, skiprows=16, parse_cols=cols)
#prj = pd.read_excel(url, sheetname=1, skiprows=16, parse_cols=cols)

#pop = pd.concat([est, prj])     # changes order 


#%%
"""
538 income by college major
http://fivethirtyeight.com/features/the-economic-guide-to-picking-a-college-major/
https://github.com/fivethirtyeight/data/tree/master/college-majors
"""
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/'
url2 = 'college-majors/recent-grads.csv'
url = url1 + url2
df538 = pd.read_csv(url, nrows=10)

# Exercise.  What are the variables here?  How many?

list(df538)


#%%
sub = df538[[2,4,15,16,17]].set_index('Major')
list(sub)

#%%
sub = sub.sort_values('Total')

#%%
"""
Airbnb
Doesn't work 
"""
import pandas as pd 
url1 = 'http://data.insideairbnb.com/united-states/ny/new-york-city/'
url2 = '2015-09-01/data/listings.csv.gz'
url = url1 + url2 

listings = pd.read_csv(file)

file = 'C:\\Users\\dbackus\\Downloads\\listings.csv'

listings = pd.read_csv(file)

#%%
"""
538 movie ratings 
http://fivethirtyeight.com/features/fandango-movies-ratings/
https://github.com/fivethirtyeight/data/blob/master/fandango/fandango_score_comparison.csv
"""

# Exercise.  What are the variables here?  How many?
#%%
"""
Brandon Rhodes' IMDb movie data from PyCon 2015
https://github.com/brandon-rhodes/pycon-pandas-tutorial#welcome-to-brandons-pandas-tutorial
Big file, 15-20 seconds on office computer, more with wireless connection
"""
url = 'http://pages.stern.nyu.edu/~dbackus/csv/cast.csv'
cast = pd.read_csv(url, encoding='utf-8')

# ah = cast[cast['title']=='Annie Hall']
# gc = cast[cast['name']=='George Clooney']

#%%
"""
Web interfaces/APIs 
"""
"""
Example:  FRED
"""
import pandas as pd 
import pandas.io.data as web    # package to access FRED 
import datetime                 # package to handle dates 

start = datetime.datetime(2010, 1, 1)
codes = ['GDPC1', 'PCECC96']    # real GDP, real consumption 
fred  = web.DataReader(codes, 'fred', start) 
fred = fred/1000                # convert billions to trillions

fred.plot()


#%%
"""
Example:  World Bank
* NY.GDP.PCAP.PP.KD = gdp per capita
* SP.DYN.LE00.IN    = life expectancy
http://data.worldbank.org/
"""
import pandas as pd                 
from pandas.io import wb            # World Bank api

var = ['NY.GDP.PCAP.PP.KD']         # GDP per capita 
iso = ['USA', 'FRA', 'JPN', 'CHN', 'IND', 'BRA', 'MEX']  # country codes 
year = 2013
wb = wb.download(indicator=var, country=iso, start=year, end=year)

wb = wb.reset_index(level='year', drop=True)
wb.plot(kind='barh') #, legend=False) 

#%%
"""
Example:  Fama-French stock returns
* xsm = excess return on market (market minus riskfree rate)
* smb = return on small firms minus return on big firms
* hml = return on high book-to-market firms minus low
* rf  = riskfree rate
All returns are monthly percentages
Google "ken french data"
"""
import pandas.io.data as web

ff = web.DataReader('F-F_Research_Data_factors', 'famafrench')[0]
ff.columns = ['xsm', 'smb', 'hml', 'rf']

ff.describe()

#%%
ff.plot()
ff.boxplot()

#%%
"""
WB data for review 
* EG.ELC.ACCS.ZS = access to electricity 
* IT.NET.USER.P2 = internet users per 100 
* IT.CEL.SETS.P2 = cell phones per 100 
http://data.worldbank.org/
"""
import pandas as pd                 
from pandas.io import wb            # World Bank api

var = ['EG.ELC.ACCS.ZS', 'IT.NET.USER.P2', 'IT.CEL.SETS.P2']
iso = ['BWA', 'NAM', 'ZAF', 'ZMB']  
year = 2012
wb = wb.download(indicator=var, country=iso, start=year, end=year)
wb = wb.reset_index(level='year', drop=True)
wb.to_dict('list')

#%%
import pandas as pd 
data = {'EG.ELC.ACCS.ZS': [53.2, 47.3, 85.4, 22.1],   # access to elec (%) 
        'IT.CEL.SETS.P2': [153.8, 95.0, 130.6, 74.8], # cell contracts per 100 
        'IT.NET.USER.P2': [11.5, 12.9, 41.0, 13.5],   # internet access per 100 
        'Country': ['Botswana', 'Namibia', 'South Africa', 'Zambia']} 
wb = pd.DataFrame(data)

#%%
"""
data for code practice 
"""
import pandas as pd

url1 = 'http://www.imf.org/external/pubs/ft/weo/2015/01/weodata/'
url2 = 'WEOApr2015all.xls'
url = url1 + url2 
weo = pd.read_csv(url, sep='\t', thousands=',', na_values=['n/a', '--']) 
weo.shape

variables = ['PPPPC']
countries = ['BRA', 'JPN', 'USA']
sub = weo[weo['ISO'].isin(countries) & weo['WEO Subject Code'].isin(variables)]
somevars = [3] + list(range(37,44))
sub = sub[some].set_index('Country').T.dropna()
sub = sub/10**3

sub.plot(lw=2)

sub.to_dict('list')

#%%
import pandas as pd 
data = {'BRA': [13.37, 13.30, 14.34, 15.07, 15.461625, 15.98, 16.10],
        'JPN': [33.43, 31.83, 33.71, 34.29, 35.60, 36.79, 37.39],
        'USA': [48.30, 46.91, 48.31, 49.72, 51.41, 52.94, 54.60], 
        'Year': [2008, 2009, 2010, 2011, 2012, 2013, 2014]}
weo  = pd.DataFrame(data)
weo 
