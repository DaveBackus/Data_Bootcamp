"""
CPS data entry experiments for Data Bootcamp course   

Goal is to reproduce 
http://esoltas.blogspot.com/2014/04/how-big-is-gender-pay-gap_10.html

Links and docs  
http://thedataweb.rm.census.gov/ftp/cps_ftp.html
http://thedataweb.rm.census.gov/pub/cps/basic/201501-/January_2015_Record_Layout.txt
http://thedataweb.rm.census.gov/pub/cps/march/asec2015early_pubuse.dd.txt
https://en.wikipedia.org/wiki/Current_population_survey_(US)

Data Bootcamp @ NYU Stern:  http://databootcamp.nyuecon.com/

Written by Dave Backus, December 2015  
Created with Python 3.5  
"""
"""
Check Python version 
"""
import pandas as pd               # the data package
import sys                        # system module (don't ask)

print('\nPython version:', sys.version)
print('Pandas version: ', pd.__version__)

#%%   
"""
CPS data entry from GNU zipped files 
"""
import pandas as pd

url_march = 'http://thedataweb.rm.census.gov/pub/cps/march/asec2015_pubuse.dat.gz' 

#codes = [('RECORD', 1, 1, '1=hh, 2=fam, 3=per'), 
#         ()]

march = pd.read_fwf(url_march, 
                    compression='gzip',
                    colspecs=[(0,1), (1,5), (5,7)],    
                    names=['HRECORD', 'SEQ', 'POS'],
                    nrows = 10, 
                    header=None) 
march

#%%
url_basic = 'http://thedataweb.rm.census.gov/pub/cps/basic/201501-/nov15pub.dat.gz' 
basic = pd.read_fwf(url_basic, 
                    compression='gzip',
                    colspecs=[(0,15), (17,21), (60,61), (90,91), (92,94)],     
                    names=['HRHHID', 'HRYEAR4', 'HRHTYPE', 'GEDIV', 'GESTFIPS'],
                    nrows = 200, 
                    header=None) 
print(basic)
