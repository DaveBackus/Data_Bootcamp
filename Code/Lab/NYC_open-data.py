"""
NYC open data experiments 

NYU Open Data 
https://nycopendata.socrata.com/

Directions:  search for dataset, click on export, right click on csv for url,
then kill everything after the question mark. 

Prepared for Data Bootcamp course at NYU  
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab 

Written by Dave Backus, February 2016 
Created with Python 3.5
"""
import pandas as pd

#%%
"""

"""
# restaurant inspections  
url = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv'
insp = pd.read_csv(url, nrows=10)

print('\nNYC restaurant inspections')
print('Dimensions:', insp.shape)
print('Variables:', list(insp))


#%%
"""
https://nycopendata.socrata.com/data?browseSearch=311+complaints
"""
url = 'https://data.cityofnewyork.us/api/views/erm2-nwe9/rows.csv'
df311 = pd.read_csv(url, nrows=10)

print('\n311 calls')
print('Dimensions:', df311.shape)
print('Variables:', list(df311))
