# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 16:40:08 2014

@author: sarahbeckett-hile
"""
# documentation for pandas.plot:
# http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.plot.html
import pandas as pd
from pylab import savefig
#%%
# Import data into dataframe with read_csv:
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv')
#%%
# sanity check to make sure the import went through ok:
df.head()
#%%
# look at column names (.tolist() isn't necessary but easier to read)
df.columns.tolist()

#%%
# just as an experiment, see what a simple graph might look like before we wrangle the data:
df.plot()
#%%
#  disaster. specify the x and y axis, and limit it to the 1st 10 (the df is already sorted by top median income by najor)
df[:10].plot(x='Major', y='Total')
#%%
# still really bad.
# add rot to rotate the x-axis labels to make them easiery to read
df[:10].plot(x='Major', y='Total', rot=90)
#%%
# little better, but the default line graph is pretty meaningless. Make it a histogram:
df[:10].plot(x='Major', y='Total', kind='bar')
# notice that rot is gone - bar graphs will automatically rotate x labels to 90.
#%%
# add a title and a label for the y-axis:
ax = df[:10].plot(
    x='Major',
    y='Total',
    kind='bar',
    title='Popularity of the Top 10 Earning Majors'
    )
ax.set_ylabel('Frequency')

#%%
# Try to view women and men separately, and throw in a legend to distinguish the two:
ax1 = df[:10].plot(
    x='Major',
    y=['Women', 'Men'],
    kind='bar',
    title='Popularity of the Top 10 Earning Majors'
    )
ax1.set_ylabel('Frequency')
ax1.legend()
#%%
# rather than clustered, stack them
# also, use colormap to change up colors
# http://matplotlib.org/examples/color/colormaps_reference.html
# change kind='bar' to kind='barh' to make this a little easier to read
# since we're rotating this chart, change set_ylabel to set_xlabel
ax2 = df[:10].plot(
    x='Major',
    y=['Women', 'Men'],
    kind='barh',
    stacked=True,
    colormap= 'Paired',
    title='Popularity of the Top 10 Earning Majors'
    )
ax2.set_xlabel('Frequency')
ax2.legend()

#%%
# sanity check. When looking at total, mechanical was greater than chemical, and the totals were near 100k. Something it wrong.
# add a column that adds men & women columns. This should equal the "total" column
df['Men+Women'] = df.Men + df.Women
#%%
# now plot Total and Men+Women next to each other to see if anything is wrong. They should align perfectly for each Major
ax3 = df[:10].plot(
    x='Major',
    y=['Men+Women', 'Total'],
    kind='barh',
    colormap= 'Paired',
    title='Popularity of the Top 10 Earning Majors'
    )
ax3.set_xlabel('Frequency')
ax3.legend()
#%%
# the legend is in the way, move it over
# googled "legend outside plot pandas": http://stackoverflow.com/questions/23556153/how-to-put-legend-outside-the-plot-with-pandas
# also extend it to the top 20 majors to see if this issue is pervasive
ax4 = df[:20].plot(
    x='Major',
    y=['Men+Women', 'Total'],
    kind='barh',
    colormap = 'Paired',
    title='Popularity of the Top 10 Earning Majors',
    width=.9
    )
ax4.set_xlabel('Frequency')
ax4.legend(loc='lower right')
# problem with data is pretty clear from the graph. In 2 cases they mixed up the gender breakdowns, affecting 4 different majors
#%%

'''
New topic: let's look at the mean salary by major *group* instead of by each individual major.
'''
# group by major category
# http://pandas.pydata.org/pandas-docs/dev/groupby.html
group_df = df.groupby('Major_category').mean()
group_df
#%%
ax5 = group_df.plot(
    y = 'Median',
    kind='barh',
    colormap = 'Paired'
    )
ax5.set_xlabel('Mean of Median Salaries')
#%%
# importing seaborn makes graphs just a little more attractive. You don't have to do anything else after you import it - it just works
import seaborn as sns
#%%
ax6 = group_df.plot(
    y = 'Median',
    kind='barh',
    colormap='Paired'
    )
ax6.set_xlabel('Mean of Median Salaries')
#%%
# but, if you want to change more, you have lots of options with seaborn
# http://web.stanford.edu/~mwaskom/software/seaborn/tutorial/aesthetics.html
# use set_style('whitegrid') to change the background, but keep the gridlines
sns.set_style('whitegrid')
ax7 = group_df.plot(y = 'Median', kind='barh', colormap = 'Paired')
ax7.set_xlabel('Mean of Median Salaries')
#%%
# use grid(False) to get rid of the grid. Use despine() to get rid of the top and right spines
ax8 = group_df.plot(
    y = 'Median',
    kind='barh',
    colormap = 'Paired',
    linewidth = 0
    )
ax8.set_xlabel('Mean of Median Salaries')
ax8.grid(False)
sns.despine()
#%%
'''
New topic: The range of incomes for each major by major group
'''
#try to pick apart what's happening here...
quartile_df = group_df[['Median','P25th','P75th']].transpose()
quartile_df
#%%
# http://web.stanford.edu/~mwaskom/software/seaborn/generated/seaborn.boxplot.html?highlight=boxplot
# use seaborn's wrapper for boxplot matplotlib's boxplot
# seaborn lets you just pass a dataframe, whereas matplotlib would need you to pass an array
sns.set_style('whitegrid')
sns.boxplot(quartile_df,  vert=False)
sns.despine()
#%%
# instead of set_style, use set_context with set_contex for a different set of programmed looks
# set_context has the follow options (you can find this out by passing anything to set_context that it won't recognize)
# set_context ... paper, notebook, talk, poster
# make the line thicker with linewidth
sns.set_context('poster')
sns.boxplot(quartile_df,  vert=False, linewidth=3)
sns.despine()
path = '/Users/sarahbeckett-hile/Desktop/figure.png'
savefig(path)
#%%
# new df, look at just a partiicular major cateogry, segment by major
hdf = df[df.Major_category == 'Humanities & Liberal Arts'][['Major', 'Median', 'P25th', 'P75th']].set_index('Major').sort().transpose()
hdf
#%%
# try boxplot from the Pandas package instead of from seaborn to sea how different modules use matplotlib differently
#%%
hdf.boxplot(figsize=(4,5), grid=False, vert=False)
#%%
path = '/Users/sarahbeckett-hile/Desktop/figure.png'
savefig(path)

