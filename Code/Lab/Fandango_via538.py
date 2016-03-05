"""
Fandango and other movie ratings

Links
* http://fivethirtyeight.com/features/fandango-movies-ratings/
* https://github.com/fivethirtyeight/data/tree/master/fandango

Prepared for Data Bootcamp course at NYU
* https://github.com/DaveBackus/Data_Bootcamp
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, January 2016
Created with Python 3.5
"""
import pandas as pd
#import matplotlib.pyplot as plt

url1 = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/'
url2 = 'fandango/fandango_score_comparison.csv'
movie = pd.read_csv(url1+url2)

movie = movie.set_index('FILM')
#movie.describe().T

#%%
# plots
movie.plot.scatter(x='IMDB', y='Fandango_Ratingvalue')
movie.plot.scatter(x='Metacritic', y='Fandango_Ratingvalue')


