# -*- coding: utf-8 -*-
#%%%
'''
This code shows an example of a simple web scrapping program.
Walk through the following steps before running the code:
1) Go to : http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices
2) Enter the dates you want and hit the get prices button.
3) Once the results are shown, look on the url address.
4) The new url will include several parameters, each one is seperated by the & character.
5) Try to explore the meanning of each parameter (s, a,b,c,d,e,f and g)
6) After some trial and error you can realize that each parameter represents the data you entered as input:
    the day, month and year, the stock sybmol, and the frequency  you chose (daily, weekly etc)
7) Scroll down to the bottom of the page. there is a link which allows downloading the data as a csv file. click on it
8) Open the CSV in excel and see the structure of the file.
9) Go back to the web page, instead of clicking on the csv link, right click on it and copy the link address
10) Paste the address in a notebook - This is the url link we can use to access the data from our coding environment.
'''

#%%
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

symbol='AAPL'  ## change this to any stock symbol you'd like to get
begin_day='01'
begin_month='00' # January (note the months run from 0 to 11)
begin_year='2010'
end_day = '31'
end_month = '11' #December
end_year='2014'
freq='d' #d - daily, w - weekly, m - monthly etc..
## the following three lines will construct a url based on the parameters above:
url = 'http://real-chart.finance.yahoo.com/table.csv?s='+symbol
url+= '&a='+begin_month+'&b='+begin_day+'&c='+begin_year
url+= '&d='+end_month+'&e='+end_day+'&f='+end_year+'&g='+freq+'&ignore=.csv'

print (url)   ## This should show a simliar stucture to the csv file found before.

# pandas allows us to read the csv file dirctly from the url
df=pd.read_csv(url)
# since all the data is read as a string, it'll be good to convert the date column to a datetime type
df['Date']=pd.to_datetime(df['Date'])
# now we can, for exmaple, plot the Adj.Close column vs. the date:
df.plot(x='Date',y='Adj Close')
