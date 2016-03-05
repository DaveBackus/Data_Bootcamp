# -*- coding: utf-8 -*-
"""
Fama/French Data
@author: wmadavis
"""

# Preliminaries
import pandas as pd
import pandas.io.data as web
import numpy as np

# URLS of additional data
url_folios = 'https://www.quandl.com/api/v1/datasets/KFRENCH/P_ME_AFS_M.csv'
url_momentum = 'https://www.quandl.com/api/v1/datasets/KFRENCH/MOMENTUM_M.csv'
url_industry = 'https://www.quandl.com/api/v1/datasets/KFRENCH/5_IND_PORTF_M.csv'

# Importing additional data and indexing by date
df_folios = pd.read_csv(url_folios, index_col = 0).iloc[::-1]
df_momentum = pd.read_csv(url_momentum,index_col = 0).iloc[::-1]
df_industry = pd.read_csv(url_industry, index_col = 0).iloc[::-1]
# Aligning datetime indices
joint_1 = df_folios.join(df_momentum).join(df_industry)


'''
Note: df_folios has data for every month since July 1964, while df_industry and
df_momentum have some periods of missing data. For these periods, we have NaNs
'''

# Reindexing the Fama-French Research Data Factors to datetime format
ff = web.DataReader('F-F_Research_Data_Factors', 'famafrench')[0]
rng = pd.date_range('1926-07-01', periods=len(ff), freq='MS')
ff = pd.DataFrame(ff.values, index=rng, columns = ff.columns)

'''
Note: We have (arbitrarily) assigned the monthly data to the first day of each
month. We want the monthly indices to be aligned with the other dataframes so
we re-index it appropriately. However, (as of March 22, 2015), ff has data for
Feb 2015, but df_folios does not. We will append a new row of data to joint_1
so that we can re-index ff by the dates used in joint_1.
'''

joint_1 = joint_1.append(pd.DataFrame(np.zeros((1,0))))
# Let us call this last February period February 28 in keeping with the pattern
# of end-of-month observations
joint_1 = joint_1.rename(index={0: '2015-02-28'})
# Now let us re-index the ff data by this new index
ff = pd.DataFrame(ff.values, index=joint_1.index, columns = ff.columns)
# Now let us join joint_1 and ff and replace missing data with 'NaN'
df_ff = ff.join(joint_1).replace('-99.99', 'NaN')
'''
Now we have a single DataFrame 'df_ff' of dimensions 1064x29, with the
following as columns corresponding to the datasets

    Column number   Dataset                     Column title
    -------------   -------                     ------------
    0               FF Research Data Factors    1 b'Mkt-RF'
    1                                           2 b'SMB'
    2                                           3 b'HML'
    3                                           4 b'RF'
    4               Portfolios Formed on ME     <= 0
    5                                           Lo 30
    6                                           Med 40
    7                                           Hi 30
    8                                           Lo 20
    9                                           Qnt 2
    10                                          Qnt 3
    11                                          Qnt 4
    12                                          Hi 20
    13                                          Lo 10
    14                                          Dec 2
    15                                          Dec 3
    16                                          Dec 4
    17                                          Dec 5
    18                                          Dec 6
    19                                          Dec 7
    20                                          Dec 8
    21                                          Dec 9
    22                                          Hi 10
    23              Momentum Factor             Momentum
    24              Five-Industry Portfolios    Consumer
    25                                          Manufacturing
    26                                          Technology
    27                                          Healthcare
    28                                          Other

Additional Notes provided by the authors:

    Missing data are indicated by -99.99 or -999."

    On the Portfolios Formed on ME dataset:

        "It contains value- and equal-weighted returns for size portfolios.
        Each record contains returns for:
            Negative (not used)
            30%
            40%
            30%
            5 Quintiles
            10 Deciles
        The portfolios are constructed at the end of Jun.

    On the Momentum Factor dataset:

        "It contains a momentum factor, constructed from six value-weight
        portfolios formed using independent sorts on size and prior return of
        NYSE, AMEX, and NASDAQ stocks.

        Momentum is the average of the returns on two (big and small) high
        prior return portfolios  minus the average of the returns on two low
        prior return portfolios.

        The portfolios are constructed monthly. Big means a firm is above the
        median market cap on the NYSE at the end of the previous month; small
        firms are below the median NYSE market cap. Prior return is measured
        from month -12 to - 2.  Firms in the low prior return portfolio are
        below the 30th NYSE percentile.  Those in the high portfolio are above
        the 70th NYSE percentile.

    On the Five-Industry Portfolios:

        It contains value- and equal-weighted returns for  5 industry
        portfolios. The portfolios are constructed at the end of June.
'''
