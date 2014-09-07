"""
Runs peaktrough.py, which generates Cooley-Rupert figures for specified
series from FRED.

Execute peaktrough.py first, then run this program.

Written by Dave Backus under the watchful eye of Chase Coleman and Spencer Lyon
Date:  July 10, 2014
"""
# import functions from peaktrough.py. * means all of them 
# generates the msg "UMD has deleted: peaktrough" which means it reloads
from peaktrough import *

# do plots one at a time
manhandle_freddata("GDPC1", saveshow="show")
print("aaaa")

# do plots all at once with map
fred_series = ["GDPC1", "PCECC96", "GPDIC96", "OPHNFB"]

# uses default saveshow parameter
gdpc1, pcecc96, gpdic96, ophnfb = map(manhandle_freddata, fred_series)

print("xxxx")
# lets us change saveshow parameter
gdpc1, pcecc96, gpdic96, ophnfb = map(lambda s:
    manhandle_freddata(s, saveshow="save"), fred_series)

print("yyyy")
# skip lhs (this doesn't seem to work, not sure why)
map(lambda s:
    manhandle_freddata(s, saveshow="show"), fred_series)
    
print("zzzz")


