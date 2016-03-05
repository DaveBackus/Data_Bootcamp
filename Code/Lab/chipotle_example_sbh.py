"""
Sarah's Chipotle code
"""
import pandas as pd
#import numpy as np
#import re

# first, define a pathway to tell python where this data can be found
path = 'https://raw.githubusercontent.com/TheUpshot/chipotle/master/orders.tsv'
# now import the data with pandas' read_table function
# read_table turns the data into a pandas DataFrame. Assign the dataframe the name df
df = pd.read_table(path)

# to take a quick look at the first few rows of the data, use the method .head()
# .head(10) returns the first 10 rows. If you don't specify a number, the default is 5
df.head(10)

# This data isn't well formatted for analysis for a few reasons:
#
# -  The item price has a $ symbol, so python will treat it like a string
#     - and we can't do math with strings
#
#
# -  The choice description isn't standardized
#     - everything is all clumped together
#     - so you can't do much to learn about the popularity of each item or its correlation with the main order
#
#
# - Sometimes the same choice_description isn't consistently written out
#      - for example, row 4 has "Tomatillo-Red Chili Salsa (Hot)"
#      - but row 7 has "Tomatillo Red Chili Salsa"
#      - these are the same menu item, but Python won't recognize that
# So now we have 3 main goals:
# 1. change the item_price  so that we can do math with it
# 2. separate the data in choice_description into different columns
# 3. standardize the names of the different items so they can be grouped more easily

# start by trying to sum up the vales in quanity:
df.quantity.sum()

# see? that was easy!
# now try to do the same with item_price
df.item_price.sum()

# that's a mess. it's because pandas saw the $ symbol and imported the data in the column as strings instead of numbers
# another way to diagnose this problem would be to check the datatype of one of the cells in the column
#type(df['item_price'][0])
df.dtypes

# to fix the price, we'll start by using the pandas method .replace()
# More on replace: http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.replace.html
# replace() is read as follows: look at column item_price, find the $, and replace it with nothing
df = df.replace(to_replace = {'item_price': {'\$': ''}}, regex=True)
# we used regex=True, otherwise Pandas would have looked for cells where $ was the only thing present
# problem is, $ is a symbol that has other operations in regular expression
# so we put a backslash in front of $ to tell regex "just treat $ as a normal character, not as an operator"
# this is a quirk of regex. If you want to learn more: https://docs.python.org/2/library/re.html

# now take a look
df.head()

# but we're still having problems with item_price
df.item_price.sum()

# this will create a new column 'price' that will turn the values in item_price into "floats"
df['price'] = df.item_price.astype('float')

# now this works!
df.price.sum()

# finally, let's just get rid of the old item_price column
del df['item_price']

# great! this is our new dataset with a nicely formatted price column
df.head()

# ## And now for something completely different...
# Now that we have the price column whipped into shape, let's take a closer look at the choice_description column:

df[['choice_description']].head(10)

# this is useless if we wanted to analyize the frequency of each of these sides
# first, let's get rid of the brackets using the same method we used to get rid of the $ symbol above
list_of_things_to_replace = ['\[', '\]'] # again, we'll need backslashes in front of the brackets to tell regex to treat them as normal characters
thing_we_want_to_replace_it_with = '' #t wo quotes with nothing in them means we'll just replace the brackets with nothing
df = df.replace(to_replace = list_of_things_to_replace , value = thing_we_want_to_replace_it_with, regex = True) #regex means it'll look for brackets anywhere, otherwise it would look for cells whose only value was [ or ]

df.head()

# Next, let's make a unique list of all the possible sides that appear in choice_description

choice_list = [] # start with an empty list
for i in range(len(df)): # basically for every row in the df
    if type(df['choice_description'][i]) == float: # if it's a number ignore it, this helps us with those NaN values
        pass
    else:
        order_list = df['choice_description'][i].split(", ") # use those commas as your deliminator
        for item in order_list: # now you have a little list of each item in choice_description in each row
            choice_list.append(item) # add that list to the master list
choice_df = pd.DataFrame(data=choice_list, columns=['Choices']) # turn this list into a little dataframe

# Now we can do some analysis. We'll start by counting how many times each side appears and ordering by most popular. We'll create a table that only takes the top 10 sides:

most_pop_choices = (pd.DataFrame(
                    choice_df.groupby('Choices')
                    .size(),
                    columns=['Count'])
                    .sort('Count',ascending=False)
                    .head(10)
                    .reset_index())
most_pop_choices

least_pop_choices = (pd.DataFrame(
                    choice_df.groupby('Choices')
                    .size(),
                    columns=['Count'])
                    .sort('Count',ascending=True)
                    .head(10)
                    .reset_index())
least_pop_choices

# some of these appear to be the same but with slightly different labels
# let's try to clean that up with some simple search-and-replace
# for instance, there are "vegetarian black beans" and "black beans", which should just be the same thing
# we can use regex for this!
# with method .replace(), you don't actually have to say "to_replace = " and "value = "
# Python will understand the first and second arguments to be these values
fix_beans = choice_df.replace('Vegetarian Black Beans',
                              'Black Beans', regex=True)

# let's do the same for salsas
# they recorded corn salsa 3 different ways: 'Roasted Chili Corn (Medium)', 'Roasted Chili Corn Salsa', and 'Roasted Chili Corn Salsa (Medium)'
# if we want our analysis to group these together, we can use regex again
# this time we'll use a list in the to_replace arguement
fix_salsas = fix_rice_beans.replace(['Roasted Chili Corn Salsa','Tomatillo Green Chili (Medium)'],
                                    'Roasted Chili Corn Salsa (Medium)')

# further discussion needed about using $, ^, *, ., etc


