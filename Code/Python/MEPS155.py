"""
MEPS data 

Variables and columns 
* DUPERSID 9-16         (combined dwelling and person id)
* DOBYY 205-208         (year of birth) 
* SEX 209-209           (sex) 
* EDUYRDEG 249-250      (education)
* TTLP12X 1502-1507     (person's income)
* FAMINC12 1508-1513    (family income)
* TOTEXP12 2677-2682    (total medical expenditures)
* PERWT12F 5303-5314    (some kind of weight)

Links 
http://meps.ahrq.gov/mepsweb/
http://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-155

Written by Dave Backus, NYU, November 2015 
Thanks to Martin Hackmann for the suggestion and advice 
"""
"""
copy file to hard drive
"""
import urllib              # handles internet files 
import os 
import zipfile             # handles zip files 
import pandas as pd 

url = 'http://meps.ahrq.gov/mepsweb/data_files/pufs/h155dat.zip'
zfname = '../' + 'Temp/' + os.path.basename(url)

# copy url to file 
urllib.request.urlretrieve(url, zfname)

#%%
"""
create zipfile object zf and extract file from it 
"""
zf = zipfile.ZipFile(zfname, 'r')
print('Contents:', zf.namelist()) 

# grab first filename and extract it
inzip = zf.namelist()[0]
dir  = '../Temp/'
extract = zf.extract(inzip, path=dir) 

#%%
"""
read file
"""
import pandas as pd 

meps = pd.read_fwf(extract, 
                    colspecs=[(8,16), (204,208)],     
                    names=['DUPERSID', 'DOBYY'],
                    header=None) 

meps.shape

#%%
