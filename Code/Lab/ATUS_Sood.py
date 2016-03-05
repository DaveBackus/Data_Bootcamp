"""
Python program to play around with the American Time Use Survey from BLS.
Goal is to replicate charts found here:
http://www.nytimes.com/interactive/2015/01/06/upshot/how-nonemployed-americans-spend-their-weekdays-men-vs-women.html
Data structure: The data is divided into four files.
In general, people in the survey are identified by (household, line_no) pairs,
where line_no separates people within a household.
The respondents file provides attributes of actual ATUS respondents,
and their line_nos are always 1.
The roster file provides attributes of people in the respondents' households. The activity file provides raw activity data for respondents, and the activity summary file summarizes it.

# First, grab the respondent and activity files:
http://www.bls.gov/tus/special.requests/atusresp_2014.zip
http://www.bls.gov/tus/special.requests/atusact_2014.zip.

# Next, load the data into pandas.

import pandas as pd

from getpass import getuser
dloadpath = "/users/"+getuser()+"/Downloads"

resp = pd.read_csv(dloadpath+"/atusresp_2014/atusresp_2014.dat")
act = pd.read_csv(dloadpath+"/atusact_2014/atusact_2014.dat")
"""

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
