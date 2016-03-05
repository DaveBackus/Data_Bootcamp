"""
PISA education data
International surveys of student performance

Sources
* https://en.wikipedia.org/wiki/Programme_for_International_Student_Assessment
* http://www.oecd.org/pisa/
* https://nces.ed.gov/surveys/pisa/
* http://www.oecd.org/pisa/keyfindings/pisa-2012-results-volume-I.pdf
* https://github.com/DaveBackus/Data_Bootcamp/blob/master/Code/Projects/PISA_SusanChen_Aug_15.ipynb

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp/

Written by Dave Backus, December 2015, based on earlier work by Susan Chen
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
Read xls file
Note:  skip notes at top/bottom, set double column labels
"""
import pandas as pd

pisa = pd.read_excel('http://dx.doi.org/10.1787/888932937035',
                     skiprows=18,
                     skipfooter=7,
                     index_col=0,
                     header=[0,1]
                     )

pisa = pisa.dropna()

print(pisa.index)
#print('\nPISA data \n', pisa)

#%%
"""
Plot
"""
# extract mean math score, sort top to bottom


