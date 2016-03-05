# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 21:33:04 2014

@author: sarahbeckett-hile
"""
import pandas as pd
from math import factorial, pow
import numpy as np
import scipy as sp
#%%
'''
 1. Let r be a binomial random variable. Compute Pr(r) for each of the following situations:
'''
# There are lots of good ways to do this
# Either make a couple of lists....
Ns = [10, 4, 16]
thetas = [.2, .4, .7]
Rs = [3, 2, 12]
questions = ['a', 'b', 'c']
#%%
#...and then write a while loop
i = 0
while i < len(questions):
    n = Ns[i] #name the different parts of the equation for easy reading
    theta = thetas[i]
    r = Rs[i]
    factorials = factorial(n) / (factorial(r)*factorial(n-r)) #this is the first chunk of the equation
    probability = factorials*pow(theta, r)*pow((1-theta), (n-r))
    rounded_prob = round(probability, 3)
    print('{}:'.format(questions[i]), rounded_prob)#
    i += 1 #add 1 to the value of i to make sure this loop ends. Doing while loops like this can be risky if you forget to add this part
#%%
###...or we could put it in dictionaries and make a DataFrame:
dict1 = {'n': Ns, 'theta': thetas, 'r': Rs} #create a dictionary from the lists
#%%
df = pd.DataFrame(data=dict1, index=questions) #create a DataFrame from the dictionary
#%%
# we'll have to use scipy.misc.factorial instead of math..factorial because math cannot work with a series, which is what we're using when applying functions to Pandas df columns
df['probability'] = (
    (sp.misc.factorial(df.n, exact = False)/
    (sp.misc.factorial(df.r, exact=False)*sp.misc.factorial(df.n-df.r, exact=False)))
    *np.power(df.theta, df.r)*np.power(1-df.theta, df.n-df.r)
    )
#%%
# or we could write a function:
def binomial_pdf(n, theta, r):
    factorials = factorial(n)/(factorial(r)*factorial(n-r))
    probability = factorials*pow(theta, r)*pow((1-theta), (n-r))
    return probability
#%%
binomial_pdf(10, .2, 3)
#%%
# finally, the simplest option - use a module that already does this:
# the module we'll use is scipy. List R first, then N and P (probability)
# http://docs.scipy.org/doc/scipy-0.13.0/reference/generated/scipy.stats.binom.html
sp.stats.distributions.binom.pmf(3, n = 10, p =.2)
#%%

'''
2. A chain of motels has adopted a policy of giving a 3% discount to customers who pay in cash
rather than by credit cards. Its experience is that 30% of all customers take the discount. Let Y =
number of discount takers among the next 20 customers.
    a. Do you think the binomial assumptions are reasonable in this situation?
'''
# YES!
#%%
'''
 b. Assuming that the binomial probabilities apply, find the probability that exactly 5 of
the next 20 customers take the discount.
'''
# we already have something for this!
print binomial_pdf(20, .3, 5)
#%%
'''
c. Find P(5 or fewer customers take the discount).
'''
r_list = range(0,6)
p_5_or_fewer = 0
for r in r_list:
    prob = binomial_pdf(20, .3, r)
    p_5_or_fewer =+ p_5_or_fewer + prob
print 'Probability that 5 or fewer customers will take the discount:', round(p_5_or_fewer, 3)
#%%
'''
d. What is the most probable number of discount takers in the next 20 customers?
'''
print .3*20
#%%
# or, to replicate the answers given in the assignment's answer key:
N = 20
theta = .3
binom_pdf_df = pd.DataFrame(index=range(0, N+1))
#%%
cumulative = 0
for index, i in binom_pdf_df.iterrows():
    probability = binomial_pdf(N, theta, index)
    binom_pdf_df.ix[index, 'P(X = x)'] = round(probability, 4)
    cumulative += probability
    binom_pdf_df.ix[index, 'P(X <= x)'] = round(cumulative, 4)
#%%
print 'Binomial with n = {} and p = {}'.format(N, theta)
binom_pdf_df
#%%
# this looks crazy messy, but all it's doing is asking for the value of the index where 'P(X = x)' is greatest
binom_pdf_df.index[binom_pdf_df['P(X = x)']==binom_pdf_df['P(X = x)'].max()].item()
#%%
# All of this can be turned into a new and fairly comprehensive function:
def binom_pdf(n, theta, R=None, Return=None):
    df = pd.DataFrame(index=range(0, n+1))
    cumulative = 0
    for index, i in df.iterrows():
        r = index
        factorials = factorial(n) / (factorial(r)*factorial(n-r)) # recreating the pdf function from  so it can standalone outside this script
        probability = factorials*pow(theta, r)*pow((1-theta), (n-r)) # need to use this and it can run independantly: from math import factorial, pow
        df.ix[index, 'P(X = x)'] = round(probability, 4)
        cumulative += probability
        df.ix[index, 'P(X <= x)'] = round(cumulative, 4)
        df.ix[index, 'P(X => x)'] = round(1-cumulative, 4)
    if R == None:
        return df
    if R != None:
        if Return == None:
            return df[df.index == R]
        #let's make some plain English options for specifying the value you're looking for with this function
        if Return == 'exactly':
            return df[df.index == R]['P(X = x)'].item()
        if Return == 'at_most' or Return == 'or_fewer' or Return == 'not_more_than' :
            return df[df.index == R]['P(X <= x)'].item()
        if Return == 'at_least' or Return == 'or_more':
            return df[df.index == R-1]['P(X => x)'].item()
        if Return == 'less_than' or Return == 'fewer_than':
            return df[df.index == R-1]['P(X <= x)'].item()
        if Return == 'greater_than' or Return == 'more_than':
            return df[df.index == R]['P(X => x)'].item()
        return df[df.index == R]
#%%
# since it's optional to submit a number for R, you can leave it out and get a table with all variables
binom_pdf(20, .3)
#%%
# or, if you are only interested in a particular value for R:
binom_pdf(20, .3, 5)
#%%
#or, if you want to get really specific:
binom_pdf(20, .3, 5, 'or_fewer')
#%%
'''
3. The admissions office of a small, selective liberal-arts college will only offer admission to
applicants who have a certain mix of accomplishments, including a combined SAT score of 1,400
or more. Based on past records, the head of admissions feels that the probability is 0.66 that an
admitted applicant will come to the college. If 500 applicants are admitted, what is the probability
that 340 or more will come? Note that “340 or more” means the set of values {340, 341, 342,
343, …, 499, 500}.
'''
# this is a great example for when we'd want to use the new binom_pdf function
# Instead of "R or fewer", we want "R or more"
# In other words, we want 'P(X => x)'
# luckily I already threw in this column!
#print binom_pdf(500, .66, 339)['P(X => x)'].item()
print binom_pdf(500, .66, 340, 'at_least')
# Bam, we're done!
#%%
'''
4. Suppose that a full-repair warranty is offered with each new Power-Up foodprocessor. If the
probability that any individual food processor will be returned forneeded warranty repairs within
one year is 0.11, and if a certain store sells 83 of these,find the probabilities that...

a. at most 10 food processors will be returned for warranty repairs;
'''
binom_pdf(83, .11, 10, 'at_most')

#%%
'''
b. at least 10 food processors will be returned for warranty repairs
'''
binom_pdf(83, .11, 10, 'at_least')
#%%
'''
c. exactly 10 food processors will be returned for warranty repairs;
'''
binom_pdf(83, .11, 10, 'exactly')
#%%
'''
d. not more than 15 food processors will be returned for warranty repairs.
'''
binom_pdf(83, .11, 15, 'not_more_than')
#%%
'''
5. The rate of home sales at a small real estate agency is 1.3 per day. We’ll assume that a Poisson
phenomenon can represent these home sales.

a. Find the probability that no homes will be sold on Monday.
'''
# First, let's write how how we'd do this if there was no existing module for Poisson probability
# we'll still cheat and use scipy to do exp()
# http://docs.scipy.org/doc/numpy/reference/routines.math.html
mean = 1.3
r = 0
poisson_probability = sp.exp(-mean) * (pow(mean,r)/factorial(r))
print poisson_probability
#%%
# fortunately, a fuction for Poisson probability does exists in scipy
# http://stackoverflow.com/questions/280797/calculate-poisson-probability-percentage
no_sales = sp.stats.distributions.poisson.pmf(0, 1.3)
print no_sales
#%%
'''
b. Find the probability that one home will be sold on Monday.
'''
one_sale = sp.stats.distributions.poisson.pmf(1, 1.3)
#%%
'''
c. Find the probability that two homes will be sold on Monday.
'''
sp.stats.distributions.poisson.pmf(2, 1.3)
#%%
'''
d. Find the probability that more than two homes will be sold on Monday
'''
no_sales = sp.stats.distributions.poisson.pmf(0, 1.3)
one_sale = sp.stats.distributions.poisson.pmf(1, 1.3)
two_sales = sp.stats.distributions.poisson.pmf(2, 1.3)
more_than_two_sales = 1 - no_sales - one_sale - two_sales
print more_than_two_sales
#%%
'''
(skip question 6 - all verbal answers)

7. It is maintained that, in a quiet equity market with no news, the daily number of shares trades
of EquiNimbus Corporation will be approximately normally distributed with mean 280,000 and
with standard deviation 32,000. Find the probability that the number of shares traded tomorrow
will be at most 325,000.
'''
# again, will try it first assuming that there's no existing function for this:
z_score = (325000 - 280000)/32000.00 # be sure to add ".00" to the end of the denominator. Otherwise you'll get an integer
