"""
slides_indicators_fred.py
Global Economy course, handles the following:
  * Loads data from FRED (uses the fred python modul)
  * cross-correlation function and graph
  * business cycle scorecard (more graphs)

Written by: Trevor Barnett (tsb296@stern.nyu.edu)
Adapted from 'slides_indicators_FRED.R', written by Paul Backus and Espend Henriksen


USAGE: Just run the script. If 'DISPLAY' below is set to True, the script will display the graphs, rather than output them
to the current working directory. This uses the API key provided by Kim Ruhl in the original R script. Make sure you
have the scipy suite and pandas suite installed, as well as the 'fred' package (available in PyPy repository). 

"""



import fred
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date,datetime


FRED_API_KEY="055ba538c874e5974ee22d786f27fdda"
FRED_SERIES=["INDPRO", "PAYEMS", "HOUST", "RRSFS", "NAPM"]
FRED_START=date(1990,1,1)

#set to false to output graphs to a file, uses current working directory. All numerical analysis is printed to the console
DISPLAY=False


fred.key(FRED_API_KEY)

def get_fred_series(series):
	def filter(o):
		return {'date': datetime.strptime(o['date'],'%Y-%m-%d').date(),
			    series: o['value']}

	
	return pd.DataFrame(map(filter,fred.observations(series)['observations']),dtype='float64').set_index('date').dropna()



fred_data=get_fred_series(FRED_SERIES[0]) # Build an initial DataFrame
for s in FRED_SERIES[1:]:
	fred_data=fred_data.join(get_fred_series(s))

fred_data=np.log(fred_data).diff(12)[FRED_START:].dropna()

def make_ccf_chart(ax,x,y,title):
	ax.xcorr(fred_data[x],fred_data[y],maxlags=24)
	ax.set_ylim(-1,1)
	ax.set_xlim(-24,24)
	ax.set_xlabel("Lag k relative to IP",fontsize=8)
	ax.set_title(title,fontsize=12)
	ax.axvline(ymin=-1,ymax=1,color='r')

plt.close('all')
fig,((ax1,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2)
make_ccf_chart(ax1,'PAYEMS','INDPRO','Nonfarm Eployment')
make_ccf_chart(ax2,'HOUST','INDPRO','Housing Starts')
make_ccf_chart(ax3,'RRSFS','INDPRO','Retail Sales')
make_ccf_chart(ax4,'NAPM','INDPRO','Purchasing Managers Index')

plt.tight_layout()

if DISPLAY:
	plt.show()
else:
	plt.savefig('ccf.png')

mean= fred_data.mean()
std=fred_data.std()
corr=fred_data.corr()
print " == MEAN =="
print mean
print " == STD. DEV. =="
print std
print " == CORR =="
print corr


def make_bcs_chart(ax,n,title):
	ax.plot(fred_data.index,fred_data[n])
	ax.set_title(title)
	xlim,ylim=ax.get_xlim(),ax.get_ylim()
	
	
	ax.fill_between(xlim,mean[n]+std[n],mean[n]-std[n],facecolor='yellow',alpha=0.5)
	
	
plt.close('all')
fig,(ax1,ax2)=plt.subplots(nrows=2,ncols=1)
make_bcs_chart(ax1,'INDPRO','Industrial Production')
make_bcs_chart(ax2,'PAYEMS','Nonfarm Employment')

if DISPLAY:
	plt.show()
else:
	plt.savefig('bcs.png')
