"""
Basics with FRED data:  input, graphs, etc.

References
* Pandas: http://pandas.pydata.org/pandas-docs/stable/
* QE: http://quant-econ.net/pandas.html
* FRED input: http://pandas.pydata.org/pandas-docs/stable/remote_data.html#fred
* ALternative? https://github.com/zachwill/fred
* FRED: http://research.stlouisfed.org/fred2/
* acf: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.acorr
* ccf: http://matplotlib.org/examples/pylab_examples/xcorr_demo.html

Written by Dave Backus, NYU, August 2014
Created with Python 3.4
"""
import pandas as pd              # pandas handles data
import pandas.io.data as web     # this does internet input
import datetime as dt            # this handles dates
import matplotlib.pyplot as pl
import numpy as np

# set starting date and series, get from FRED
# default end date is most recent
start = dt.datetime(1950, 1, 1)
fred_series = ["GDPC1", "PCECTPI"]
data = web.DataReader(fred_series, "fred", start)

# what kind of thing do we have?
print(['data is type ', type(data)])

# some properties
data.info()
data.index

#%%
# compute growth rate and continue
g = data.pct_change()
g.columns = ['GDP Growth', 'Inflation']
moments = [g.mean(), g.std(), g.skew(), g.kurtosis()]
print(['Moments (mean, std, skew, kurt)', moments])
print(['Quantiles (0.25, 0.5, 0.75)', g.quantile(q=[0.25, 0.5, 0.75])])
print(['Correlations', g.corr()])

# try some graphs
g.plot()
#g.boxplot()
g.hist(bins=20)

#%%
# pyplot apps
gy = g.ix[1:,0]
gp = g.ix[1:,1]

#%%
#acf_gy = pl.acorr(gy, maxlags=48)
acf_gp = pl.acorr(gp, maxlags=60)
#pl.xcorr(gy, gp, maxlags=12)
#acf_gp = np.correlate(gp, gp, mode='same')
#acf = acf[12:]

phi = 0.991
acf_arma = 0.87*phi**abs(acf_gp[0])
pl.bar(acf_gp[0], acf_gp[1])
pl.plot(acf_gp[0], acf_arma, 'r*')
#pl.plot(acf_gp[0], 0.95**acf_gp[0], 'r*')


#%%
# Example
import matplotlib.pyplot as plt
import numpy as np

x,y = np.random.randn(2,100)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.grid(True)
ax1.axhline(0, color='black', lw=2)

ax2 = fig.add_subplot(212, sharex=ax1)
ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.grid(True)
ax2.axhline(0, color='black', lw=2)

plt.show()




