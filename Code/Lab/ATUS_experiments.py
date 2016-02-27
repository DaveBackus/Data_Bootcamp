"""
American Time Use Survey:  How people spend their time 

Links 
* http://www.bls.gov/tus/#data
* http://www.nytimes.com/interactive/2015/01/06/upshot/how-nonemployed-americans-spend-their-weekdays-men-vs-women.html


Prepared for Data Bootcamp course at NYU  
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab 

Written by Dave Backus, February 2016 
Created with Python 3.5 
"""
import sys 
import pandas as pd 
#import matplotlib.pyplot as plt 
#import numpy as np 
#import matplotlib.pyplot as plt

print('\nPython version: ', sys.version) 
print('Pandas version: ', pd.__version__, '\n') 

#%%


# Now, let's look for the unemployed people.

# The variable in question is TELFS. It has 5 different values: {(1, Employed - At Work), (2, Employed - Absent), (3, Unemployed - on Layoff), (4, Unemployed - Looking), (5, Unemployed - Not in the Labor Force)}.

unemp_resp = resp[resp.TELFS > 2]
unemp_ids = unemp_resp.TUCASEID
unemp_act = act[act.TUCASEID.isin(unemp_ids)]

# Now, you'll observe that, although we're given durations, the actual times 
# are formatted for human consumption: i.e., strings of type 20:48:00). 
# Before beginning, let's format them for machine consumption. 
# We do this by using Python's 'time' module (that way, we can do operations 
# like >, ==, etc.).

# Note: these are only for times in the day, so the year/month/day attributes 
# are defaulted. For absolute times, we'll have to pull in the TUDIARYDATE 
# attribute from the responses dataframe, using the same method (i.e., find the
# row in unemp_resp with the same CASE ID, grab the date, convert to string, 
# add the string to the string we parse, and edit the format).

# It takes time, so we comment it out.

'''
import time
f = lambda x: time.strptime(str(x), "%H:%M:%S")
unemp_act['TUSTARTTIM'].map(f)
unemp_act['TUSTOPTIME'].map(f)
'''

# Arnav Sood, 2015.
# Ref: StackExchange, for many techniques included here. Specifically: iteration syntax, isin(), time, map.