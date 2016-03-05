"""
Messing around in Python for the Data Bootcamp course
Written by Dave Backus, August 2015
Created with Python 3.4
"""
"""
For Laura:  GET MSI stock data prior to their Dutch auction
http://pandas.pydata.org/pandas-docs/stable/remote_data.html#yahoo-finance
"""
import pandas.io.data as web
import datetime as dt

start = dt.datetime(2015, 1, 1)
msi = web.DataReader('msi', 'yahoo', start)
msi['Close'].plot()

#%%
"""
Options data -- doesn't work
http://pandas.pydata.org/pandas-docs/stable/remote_data.html#yahoo-finance-options
"""
import pandas as pd
print('Pandas version:', pd.__version__)

from pandas.io.data import Options

aapl = Options('aapl', 'yahoo')
data = aapl.get_all_data()

#%%
"""
convert do file to pandas format and variable labels
CPS
http://www.nber.org/data/cps_progs.html
MEPS
http://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-155
"""
import pandas as pd
url = 'http://www.nber.org/data/progs/cps/cpsmar2014.dct'
pd.read_csv(url, sep='\s+')

#open(url).read()

#%%
"""
Verify double import
"""
import pandas as pd
print('Pandas version (pd)', pd.__version__)

import pandas as pa
print('Pandas version (pa)', pa.__version__)

print('Pandas version (pd after pa)', pd.__version__)


#%%



#%%
w = 2*3
x = 2**3
y = x/w
z = a/x

#%%
import matplotlib.pyplot as plt

# http://matplotlib.org/users/style_sheets.html
print(plt.style.available)
plt.style.use('ggplot')
plt.style.reload_library()  # does this reset default?



#%%
# http://www.reddit.com/r/Python/comments/3bgjud/you_sit_down_with_your_machine_and_a_person_who/
import turtle
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
