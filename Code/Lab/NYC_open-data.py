"""
NYC open data experiments

NYU Open Data
https://nycopendata.socrata.com/
https://dev.socrata.com/docs/endpoints.html

Directions:  search for dataset, click on export, right click on csv for url,
then kill everything after the question mark.

Prepared for Data Bootcamp course at NYU
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, February 2016
Created with Python 3.5
"""
import pandas as pd
import time

#%%
"""
restaurant inspections
takes 7-8 minutes with an ethernet connection, delivers 476k observations
"""
start = time.process_time()
print('\nLocal time at start:', time.localtime())
url = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv'
insp = pd.read_csv(url, low_memory=False)

print('\nNYC restaurant inspections')
print('Dimensions:', insp.shape)
print('Variables and types:\n', insp.dtypes, sep='')

print('\nLocal time at finish:', time.localtime())
print('\nTiming for restaraunt input', time.process_time()-start)

#%%
"""
311 complaints
"""
url = 'https://data.cityofnewyork.us/api/views/erm2-nwe9/rows.csv'
df311 = pd.read_csv(url, nrows=10)

print('\n311 calls')
print('Dimensions:', df311.shape)
print('Variables:', list(df311))

#%%
"""
Itamar's 311 code
50k observations takes 7 minutes with ethernet connection
Paul's explanation:
The data server runs a program that tells it how to deliver the data.
The inputs to this program are passed to the server in the url after the ?.
The format is described in the SODA Query docs, which we access from the
wrench at the top of the NYC open data page:
https://nycopendata.socrata.com/
https://dev.socrata.com/docs/queries/
"""
print('\nLocal time at start:', time.localtime())

size=1000
start=0
base_url='https://data.cityofnewyork.us/resource/erm2-nwe9.json'
df_final=pd.DataFrame()
for i in range(50):
    url = base_url+'?$limit=%s&$offset=%d'%(size,start)
    df=pd.read_json(url)
    df_final = df_final.append(df)
    start+=size

print('\n311 calls')
print('Dimensions:', df_final.shape)
print('Variables and types:\n', df_final.dtypes, sep='')

print('\nLocal time at finish:', time.localtime())


