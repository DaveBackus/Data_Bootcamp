"""
FiveThirtyEight College Major Data
Data pulled from American Community Survey 2010-2012 as used in this article:
'http://fivethirtyeight.com/features/the-economic-guide-to-picking-a-college-major/'
Written by Matt Davis, NYU, February 2015
Created in Python 3.4
"""
# PRELIMINARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

# IMPORTING DATA
# All students
url_all = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/all-ages.csv'
df_all = pd.read_csv(url_all)
# Recent graduates, a subset of all students consisting of <28 year olds with an undergraduate degree
url_recent = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv'
df_recent = pd.read_csv(url_recent)
# Graduate students, a subset of all students consisting of >25 year olds enrolled in graduate school
url_grad = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/grad-students.csv'
df_grad = pd.read_csv(url_grad)
# Recent STEM students, a subset of recent graduates
url_stem = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/women-stem.csv'
df_stem = pd.read_csv(url_stem)

#FUNCTIONS

"""
Parameters
----------
df : the dataframe being considered. Choose from:
        df_recent: sample <28 years old with a bachelor's degree
        df_grad: sample >25 years old enrolled in graduate school
        df_all: all subjects contained in the two above
        df_stem: sample <28 years old majoring in a STEM subject

category : the measure being used
Choose one out of the following, wrapped in single quotation marks

    For df_recent

        Rank	:                 Rank by median earnings relative to other members in their dataframe
        Total:                Total number of people with major
        Sample_size	      Sample size (unweighted) of full-time, year-round ONLY (used for earnings)
        Men	                  Male graduates
        Women	            Female graduates
        ShareWomen	            Women as share of total
        Employed	            Number employed (ESR == 1 or 2)
        Full_time	            Employed 35 hours or more
        Part_time	            Employed less than 35 hours
        Full_time_year_round	Employed at least 50 weeks (WKW == 1) and at least 35 hours (WKHP >= 35)
        Unemployed	            Number unemployed (ESR == 3)
        Unemployment_rate	Unemployed / (Unemployed + Employed)
        Median	            Median earnings of full-time, year-round workers
        P25th	            25th percentile of earnigns
        P75th	            75th percentile of earnings
        College_jobs	      Number with job requiring a college degree
        Non_college_jobs	      Number with job not requiring a college degree
        Low_wage_jobs	      Number in low-wage service jobs

    For df_grad

        Grad_total
        Grad_employed
        sample_size
        Grad_employed
        Grad_full_time_year_round
        Grad_unemployed
        Grad_unemployment_rate
        Grad_median
        Grad_P25
        Grad_P75
        Nongrad_total
        Nongrad_employed
        Nongrad_full_time_year_round
        Nongrad_unemployed
        Nongrad_unemployment_rate
        Nongrad_median
        Nongrad_P25
        Nongrad_P75
        Grad_share
        Grad_premium

    For df_stem

        Total
        Men
        Women
        ShareWomen
        Median

    For df_all

        Total
        Employed
        Employed_full_time_year_round
        Unemployed
        Unemployment_rate
        Median
        P25th
        P75th

majcat: Choose one of the following major categories:

        Agriculture & Natural Resources
        Biology & Life Science
        Engineering
        Humanities & Liberal Arts
        Communications & Journalism
        Computers & Mathematics
        Industrial Arts & Consumer Services
        Education
        Law & Public Policy
        Health
        Interdisciplinary
        Physical Sciences
        Psychology & Social Work
        Arts
        Business
"""

def sort(df, category, order, n):
    """
    Ranks the top-n or bottom-n majors by a given category

    Parameters
    ----------
    order: ascending or descending
        0 means descending by chosen category
        1 means ascending by chosen category
        2 means descending by median salary

    n: truncates the number of majors in the list to n
        n = 0 gives an untruncated list (i.e. all 173 majors)

    """
    catlist = list(zip(df.Major, df[category]))

    if order == 0:
        catlist = sorted(catlist, key=itemgetter(1), reverse=True)

    if order == 1:
        catlist = sorted(catlist, key=itemgetter(1))

    if order == 2:
        catlist = catlist

    if n > 0:
        catlist = catlist[:n]

    return pd.DataFrame(catlist)

def cutoff(df, category, cut, direction, order, n):
    """
    Retrieve a list of majors that obey a given cutoff criterion customizable by category and order

    Parameters
    ----------
    cut : the numerical cutoff point within the category

    direction: filtering to include only those majors below, above, or exactly the cutoff point
        'above' or 'below' or 'exact'

    order: ascending or descending
        0 means descending by chosen category
        1 means ascending by chosen category
        2 means descending by median salary

    n: truncates the list to the top (or bottom) n majors
        n = 0 gives an untruncated list (i.e. all 173 majors)
    """

    if direction == 'below':
        filt = list(zip(df[df[category] <= cut].Major, df[df[category] <= cut][category]))

    if direction == 'above':
        filt = list(zip(df[df[category] >= cut].Major, df[df[category] >= cut][category]))

    if direction == 'exact':
        filt = list(zip(df[df[category] == cut].Major, df[df[category] == cut][category]))

    if order == 0:
        filt = sorted(filt, key=itemgetter(1), reverse=True)

    if order == 1:
        filt = sorted(filt, key=itemgetter(1))

    if n > 0:
        filt = filt[:n]

    return pd.DataFrame(filt)

def stackedbars(df, majcat, n):
    """
    Produces a series of n bar graphs depicting interquartile salary between majors within a given major category
    Due to length of majors, major codes were used as a proxy on the x axis. These can be easily cross-referenced with the appropriate data frame.

    Parameters
    ----------
    majcat: Enter a string representing the major category of interest

    n: truncates the majors of interest to the top n majors within the major category
        n = 0 gives an untruncated list
    """
    N =  len(df[df.Major_category == majcat])
    width = 0.35
    newdata = df[df.Major_category == majcat]

    if n >= 1:
        newdata = newdata[:n]
        N = n

        Q1s = np.array(newdata.P25th.values.T)   # vector of first quartile values
        Meds = np.array(newdata.Median.values.T) # vector of median values
        Q3s = np.array(newdata.P75th.values.T)   # vector of third quartile values
        p1 = plt.bar(np.arange(N), Q1s, width, color = 'r')
        p2 = plt.bar(np.arange(N), Meds-Q1s, width, color = 'y', bottom = Q1s)
        p3 = plt.bar(np.arange(N), Q3s-Meds, width, color = 'g', bottom = Meds)

    if n == 0:
        Q1s = np.array(newdata.P25th.values.T)   # vector of first quartile values
        Meds = np.array(newdata.Median.values.T) # vector of median values
        Q3s = np.array(newdata.P75th.values.T)   # vector of third quartile values
        p1 = plt.bar(np.arange(N), Q1s, width, color = 'r')
        p2 = plt.bar(np.arange(N), Meds-Q1s, width, color = 'y', bottom = Q1s)
        p3 = plt.bar(np.arange(N), Q3s-Meds, width, color = 'g', bottom = Meds)

    plt.ylabel('Salary')
    plt.xlabel('Major code')
    plt.title('Interquartile salary range of graduates in ' + str(majcat))
    plt.xticks(np.arange(N)+width/2., newdata.Major_code.values.T)
    plt.legend((p1[0], p2[0], p3[0]),('First quartile', 'Median', 'Third quartile'), loc=3)

#Examples

# The graduate-school majors with the five lowest unemployment
sort(df_grad, 'Grad_unemployment_rate', 1, 5)

# The undergradate majors with fewer than 500 women enrolled sorted in ascending order by number of women enrolled
cutoff(df_recent, 'Women', 500, 'below', 1, 0)

# Interquartile bargraphs of the five majors within business with the highest median salaries for recent graduates
stackedbars(df_recent, 'Business', 5)
