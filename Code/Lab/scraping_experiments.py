"""
Scraping...

** THIS DOES NOT WORK YET **

References
* https://www.quandl.com/tools/python
* https://www.quandl.com/search?query=options&type=free

Targets (option data)
* https://www.google.com/finance/option_chain?q=NASDAQ%3AAMZN&ei=-1y3VsCOEMiOeeXotaAI
* http://finance.yahoo.com/q/op?s=AAPL&date=1458777600

Prepared for Data Bootcamp course at NYU
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, February 2016
Created with Python 3.5
"""
import sys
import pandas as pd
from bs4 import BeautifulSoup

print('\nPython version: ', sys.version)
print('Pandas version: ', pd.__version__, '\n')

#%%
# needs html5lib
url = 'http://finance.yahoo.com/q/op?s=AAPL&date=1458777600'
html = pd.read_html(url)

#%%
print('\nhtml has type', type(html), 'and length', len(html), '\n')
[print(item) for item in html]

#%%
soup = BeautifulSoup(html, 'html.parser')


