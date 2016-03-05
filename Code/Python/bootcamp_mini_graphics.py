"""
For Class #2 of an informal mini-course at NYU Stern, Fall 2014.

Topic:  reminders, matplotlib graphics

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp

Written by Dave Backus, Sarah Beckett-Hile, and Glenn Okun
Created with Python 3.4
"""

"""
Reminders 0:  editor, IPython console, Object inspector

Reminders 1:  calculations, strings, slicing
"""
x, y, z = 2*3, 2**3, 2/3    # yes, three at once!
a, b = 'some', 'thing'      # strings
c = a + b

numbers = [x, y, z]
strings = [a, b, c]
both = numbers + strings
print([type(both), both[:3], both[3:]])

#%%
"""
Reminders 2:  reading csv's (the exercise from last class)
"""
import pandas as pd
url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/'
url2 = 'college-majors/recent-grads.csv'
df = pd.read_csv(url1+url2)

#%%
# print various properties of df one at a time
properties = [type(df), df.columns, df.index, df.shape, df.head()]
for prop in properties:
    print(prop, end='\n\n')

#%%
"""
Graphics 1:  Pyplot's simple (Matlab-like) interface
diff bar colors:  http://stackoverflow.com/questions/2581400/matplotlib-changing-rect-colours-on-the-fly
"""
import matplotlib.pyplot as plt             # import pyplot module

# data
# this is FRED series GDPCA, billions of 2009 USD, accessed November 2014
gdp  = [13271.1, 13773.5, 14234.2, 14613.8, 14873.7, 14830.4, 14418.7,
        14783.8, 15020.6, 15369.2, 15710.3]
# FRED series DPCERX1A020NBEA
pce  = [8867.6, 9208.2, 9531.8, 9821.7, 10041.6, 10007.2, 9847.0, 10036.3,
        10263.5, 10449.7, 10699.7]
year = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]

#%%
# line plot
plt.plot(year, gdp, color='#ffcc00', linewidth=2,
         marker='o', alpha=0.8)
plt.plot(year, pce, color='magenta', linewidth=2, alpha=0.5)
#%%
# dress up the figure
plt.title('US Real GDP and Consumption')
plt.ylabel('Billions of 2009 USD')
plt.legend(('GDP', 'Consumption'), loc=0)   # legend
plt.text(2010, 14000, 'GDP')                # add label at specific location
plt.text(2010, 9200, 'Consumption')         # another one
plt.ylim((0, 16000))                        # change y axis limits
plt.tick_params(length=6, width=2, colors='red')
plt.savefig('bootcamp_test.pdf')
plt.show()                                  # this closes the plot

#%%
# bar charts

# Example 1
plt.bar(year, gdp)
#%%                       # bar(x,y)
# prettier version
plt.bar(year, gdp, width=0.8, color='blue', align='center', alpha=1)
plt.show()

#%%
# Example 2
# See:  http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html
codes     = ['USA', 'FRA', 'JPN', 'CHN', 'IND', 'BRA', 'MEX']
countries = ['United States', 'France', 'Japan', 'China', 'India',
             'Brazil', 'Mexico']
# World Bank data, thousands of 2013 USD, PPP adjusted
gdppc     = [53.1, 36.9, 36.3, 11.9, 5.4, 15.0, 16.5]
other_axis = range(len(gdppc))

plt.bar(other_axis, gdppc, align='center')

# prettify it
plt.xticks(other_axis, codes, fontsize=12)
plt.xlim((-0.75, 6.75))
plt.ylabel('GDP Per Capita (thousands of USD)')
plt.title('GDP Per Capita', fontsize=16, loc='left')
plt.show()

#%%
# Example 2':  horizontal bars
plt.barh(other_axis, gdppc, align='center', edgecolor='red',
         linewidth=2, alpha=0.2)
plt.ylim((-0.6, 6.6))
plt.yticks(other_axis, countries, fontsize=14)
plt.show()

#%%
"""
Graphics 2:  Object-oriented graphics
"""
import matplotlib.pyplot as plt             # redundant if already done
gdp  = [13271.1, 13773.5, 14234.2, 14613.8, 14873.7, 14830.4, 14418.7,
        14783.8, 15020.6, 15369.2, 15710.3]
pce  = [8867.6, 9208.2, 9531.8, 9821.7, 10041.6, 10007.2, 9847.0, 10036.3,
        10263.5, 10449.7, 10699.7]
year = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]

# set up a plot
fig, ax = plt.subplots()                    # sets up single plot
print([type(fig), type(ax)])                # see what we have

# add content to the object ax
ax.plot(year, gdp, color='blue', linewidth=2, alpha=0.8)

#%%
# multiple plots

# plylab version
# ??

# object oriented version
fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)

# first figure
ax[0].plot(year, gdp, color='blue', linewidth=2, alpha=0.8)
ax[0].text(2010, 14000, 'GDP')

# second figure
ax[1].plot(year, pce, color='magenta', linewidth=2, alpha=0.8)
ax[1].text(2010, 9200, 'Consumption')

plt.show()

