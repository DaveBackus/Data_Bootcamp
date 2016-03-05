"""
Fama/French Data
@author: wmadavis
"""

## Preliminaries
import pandas as pd
import pandas.io.data as web

## IMPORTING DATA

# Research Data Factors
df_research = web.DataReader('F-F_Research_Data_factors', 'famafrench')[0]

#%%
# Portfolios Formed on Size
url_folios = 'https://www.quandl.com/api/v1/datasets/KFRENCH/P_ME_AFS_M.csv'
df_folios = pd.read_csv(url_folios, index_col = 0).iloc[::-1]
index = df_folios.index
df_folios.index = df_research.index

# Momentum Factor
df_momentum = web.DataReader('F-F_Momentum_Factor', 'famafrench')[1]

# 5-Industry Portfolios
'''
This dataset is organized strangely. Using the DataReader produces a dict
object with keys 4, 6, 8, 10, 12, 14, 16 corresponding to the following:

    4:      Average Value Weighted Returns (Monthly)
    6:      Average Equal Weighted Returns (Monthly)
    8:      Average Value Weighted Returns (Annual)
    10:     Average Equal Weighted Returns (Annual)
    12:     Number of Firms in Portfolios (Monthly)
    14:     Average Firm Size (Monthly)
    16:     Sum of BE/Sum of ME (Annual)
    18:     Value-Weighted Average of BE/ME (Annual)

We will import the monthly data separately. We need to relabel the columns
since they are identical between these eight datasets.
'''
ind = web.DataReader('5_Industry_Portfolios', 'famafrench')

# Average Value Weighted Returns
df_ind_val = ind[4]
df_ind_val.columns = ['Cons_val', 'Manuf_val', 'HiTec_val', 'Hlth_val', 'Other_val']

# Average Equal Weighted Returns
df_ind_eq = ind[6]
df_ind_eq.columns = ['Cons_eq', 'Manuf_eq', 'HiTec_eq', 'Hlth_eq', 'Other_eq']

# Number of Firms in Portfolios
df_ind_firms = ind[12]
df_ind_firms.columns = ['Cons_firms', 'Manuf_firms', 'HiTec_firms', 'Hlth_firms', 'Other_firms']

# Average Firm Size
df_ind_size = ind[14]
df_ind_size.columns = ['Cons_size', 'Manuf_size', 'HiTec_size', 'Hlth_size', 'Other_size']

# Merging all ind data
df_ind = df_ind_val.join(df_ind_eq).join(df_ind_firms).join(df_ind_size)

'''
Now we will merge the four DataFrames we have: df_research, df_momentum,
df_folios, and df_ind. These three are all indexed YYYYMM, but we will then
re-index them by the dates provided by the more specific YYYY-MM-DD dates
from the Quandl data.
'''

# MERGING ALL DATA
df_ff = df_research.join(df_folios).join(df_momentum).join(df_ind)
df_ff.index = index # Re-indexing
df_ff = df_ff.replace('-99.99', 'NaN') # Replace missing data with 'NaN'

# Looking at df_ff.columns, we find we can still clean up some column titles
# for ease of navigation.
df_ff = df_ff.rename(columns={"1 b'Mkt-RF'":'Mkt_RF', "2 b'SMB'":'SMB', "3 b'HML'":'HML', "4 b'RF'":'RF', "<= 0":'Negative', "1 b'Mom'":'Momentum'})

'''
Now we have a single DataFrame 'df_ff' of dimensions 1064x44, with the
following as columns corresponding to the datasets

    Column #   Dataset                           Column title
    --------   -------                           ------------
    0          FF RESEARCH DATA FACTORS          Mkt-RF
    1                                            SMB
    2                                            HML
    3                                            RF
    4          PORTFOLIOS FORMED ON SIZE         Negative
    5                                            Lo 30
    6                                            Med 40
    7                                            Hi 30
    8                                            Lo 20
    9                                            Qnt 2
    10                                           Qnt 3
    11                                           Qnt 4
    12                                           Hi 20
    13                                           Lo 10
    14                                           Dec 2
    15                                           Dec 3
    16                                           Dec 4
    17                                           Dec 5
    18                                           Dec 6
    19                                           Dec 7
    20                                           Dec 8
    21                                           Dec 9
    22                                           Hi 10
    23          MOMENTUM FACTORS                 Momentum
    24          FIVE-INDUSTRY PORTFOLIOS         Cons_val
    25                                           Manuf_val
    26                                           HiTec_val
    27                                           Hlth_val
    28                                           Other_val
    29                                           Cons_eq
    30                                           Manuf_eq
    31                                           HiTec_eq
    32                                           Hlth_eq
    33                                           Other_eq
    34                                           Cons_firms
    35                                           Manuf_firms
    36                                           HiTec_firms
    37                                           Hlth_firms
    38                                           Other_firms
    39                                           Cons_size
    40                                           Manuf_size
    41                                           HiTec_size
    42                                           Hlth_size
    43                                           Other_size

        For the Portfolios Formed On Size,
            Qnt refers to quintiles
            Dec refers to deciles
        For the Five-Industry Portfolios,
            Cons refers to Consumer
            Manuf refers to Manufacturing
            HiTec refers to High Technology
            Hlth refers to Healthcare
            Other refers to all other industries
            _val refers to Average Value Weighted Returns
            _eq refers to Average Equal Weighted Returns
            _firms refers to the Number of Firms in Portfolios
            _size refers to the Average Firm Size

    For example, we may call
        df_ff['Hi 10'] or df_ff.HiTec_firms

Additional Notes provided by the authors:

    On the Portfolios Formed on Size dataset:

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

    On the Five-Industry Portfolio dataset:

        It contains value- and equal-weighted returns for 5 industry
        portfolios. The portfolios are constructed at the end of June.
'''
