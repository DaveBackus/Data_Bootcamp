"""
NYC restaurant inspections and ratings

NYU Open Data
https://nycopendata.socrata.com/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59

Variable names
CAMIS      unique identifier for the entity (restaurant)
DBA        business name (doing business as)
BORO       1 = MANHATTAN, 2 = BRONX, 3 = BROOKLYN, 4 = QUEENS, 5 = STATEN IS
BUILDING   building number
STREET	  street name
ZIPCODE
PHONE
CUISINE
INSPECTION DATE
ACTION	  No violations, re-opened, re-closed, closed, missing = no action
VIOLATION CODE
VIOLATION DESCRIPTION
CRITICAL FLAG
SCORE
GRADE	  A, B, C, Z = Grade Pending, P=Grade Pending on re-opening
GRADE DATE
RECORD DATE  Date data was extracted
From:  https://nycopendata.socrata.com/api/views/xx67-kt59/files/cWGKTm3caip6-I-6ZXJ6GeXSw9A_VieTzbBJhE41Mpc?download=true&filename=Restaurant%20Inspection%20Open%20Data%20Dictionary%20082214.xlsx

Repository of materials (including this file):
* https://github.com/DaveBackus/Data_Bootcamp

Written by Dave Backus, January 2016
Created with Python 3.5
"""
import pandas as pd

# read data from file
file = 'nyc_restaurant_inspections.csv'
dir  = '../csv/'

df = pd.read_csv(dir+file)
df.shape

#%%
# read data from NYC repo
url = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv'
dfweb = pd.read_csv(url, nrows=20)

dfweb.shape

#%%
