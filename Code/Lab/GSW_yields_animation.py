
# coding: utf-8

# In[1]:

"""
US Yield Curve Dynamics

Repository of materials (not including this file):
* https://github.com/DaveBackus/Data_Bootcamp

Written by David Cai, June 2015, txc202@nyu.edu
Created with Python 3.4.3

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# input yield data from csv
file = '/Users/davidcai/YieldsAssignment/GSW_nominal_yields.csv' # file location
df = pd.read_csv(file, index_col=0) # read in csv file and treat first column as row labels
dates = df.index # create list of dates
maturity = list(range(1,122))

def animate(nframe):
    plt.cla() # clear window
    plt.plot(maturity, df.iloc[nframe], label='%s'%dates[nframe]) # graph yield vs maturity, label graph with date
    plt.xlim(0,120) # Set x-axis range from 0 to 120 months
    plt.xlabel('Maturity (months)') # add x-axis label
    plt.ylim(-5,20) # Set y-axis range from -5 to 20 percent
    plt.ylabel('Yield (percentage)') # add y-axis label
    plt.title('US Treasury Yields') # add title
    plt.legend(loc='upper center', borderpad=0.25) # move legend to upper center, increase legend whitespace

fig = plt.figure(figsize=(5,5)) # set window size to 5 x 5 inches
anim = animation.FuncAnimation(fig, animate, frames=len(df))
# create new graph for each observation date using animate function
anim.save('bond_yields.gif', writer='imagemagick', fps=6); # save to gif file, requires external program ImageMagick
# animation has six frames per second

