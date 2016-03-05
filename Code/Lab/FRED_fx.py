"""
Daily Foreign Exchange Data
@author: W. Matthew Davis

Data retrieved from FRED, Federal Reserve Bank of St. Louis
https://research.stlouisfed.org/fred2/series/DEXUSEU/, March 18, 2015.

"""

# PRELIMINARIES
import pandas as pd
import pandas.io.data as web

def import_fx(rel_curr, base_curr, lower=None, upper=None):
    """
    Pulls FRED exchange-rate data to create any desired exchange rate from the
    given options

    Parameters
    ----------
    rel_curr: the relative currency
    base_curr: the base currency

        e.g. if we say the US-EU exchange rate is $1.07 per Euro, the dollar is
        the relative currency and the euro is the base currency

        Choose from the following, wrapping the currency code in single
        quotation marks, e.g. create_fx('EU', 'NO')

        currency code       currency

        US                  US Dollars
        EU                  Euros
        UK                  British Pounds
        NZ                  New Zealand Dollars
        JP                  Japanese Yen
        CH                  Chinese Yuan
        CA                  Canadian Dollars
        BZ                  Brazilian Reals
        MX                  Mexican Pesos
        SZ                  Swiss Francs
        KO                  Korean Won
        IN                  Indian Rupees
        TH                  Thai Baht
        TA                  Taiwanese Dollars
        SF                  South African Rand
        VZ                  Venezuelan Bolivares
        MA                  Malaysian Ringgit
        SI                  Singaporean Dollars
        NO                  Norwegian Kroner
        HK                  Hong Kong Dollars
        SD                  Swedish Kroner
        DN                  Danish Kroner
        SL                  Sri Lankan Rupees

        Make sure to wrap in single quotations.


    lower: lower bound for dates of interest
    upper: upper bound for dates of interest

            wrap in single quotations and use YYYY-MM-DD format
            default is to use first available date for lower and latest data
            for upper

        e.g. import_fx('EU', 'US', '2010-03-01', '2013-03-01')

    Returns
    -------
    df : pd.DataFrame
        A DataFrame of the desired exchange rate indexed by the desired date
        range
    """

    if rel_curr in ('EU', 'UK', 'NZ'):
        fxcode = 'DEXUS'+rel_curr
        rel_raw = web.DataReader(fxcode, 'fred') # Imports data from FRED
        rel_conv = rel_raw.convert_objects(convert_numeric=True) # Converts dataframe into numeric dataframe
        relative = rel_conv.truncate(before=lower, after=upper)**-1

    elif rel_curr == 'US':
        if base_curr in ('EU', 'UK', 'NZ'):
            fxcode = 'DEXUS'+base_curr
            rel_raw = web.DataReader(fxcode, 'fred') # Imports data from FRED
            rel_conv = rel_raw.convert_objects(convert_numeric=True) # Converts dataframe into numeric dataframe
            relative = pd.DataFrame(rel_conv.values/rel_conv.values, index=rel_conv.index).truncate(before=lower, after=upper)
        elif base_curr == 'US':
            rel_raw = web.DataReader('DEXUSEU', 'fred')
            rel_conv = rel_raw.convert_objects(convert_numeric=True)
            return pd.DataFrame(rel_conv.values/rel_conv.values, index=rel_conv.index, columns = ['DEXUSUS'])
            exit()
        else:
            fxcode = 'DEX'+base_curr+'US'
            rel_raw = web.DataReader(fxcode, 'fred') # Imports data from FRED
            rel_conv = rel_raw.convert_objects(convert_numeric=True) # Converts dataframe into numeric dataframe
            relative = pd.DataFrame(rel_conv.values/rel_conv.values, index=rel_conv.index).truncate(before=lower, after=upper)

    else:
        fxcode = 'DEX'+rel_curr+'US'
        rel_raw = web.DataReader(fxcode, 'fred') # Imports data from FRED
        rel_conv = rel_raw.convert_objects(convert_numeric=True) # Converts dataframe into numeric dataframe
        relative = rel_conv.truncate(before=lower, after=upper)

    if base_curr in ('EU', 'UK', 'NZ'):
        fxcode2 = 'DEXUS'+base_curr
        base_raw = web.DataReader(fxcode2, 'fred')
        base_conv = base_raw.convert_objects(convert_numeric=True)
        base = base_conv.truncate(before=lower, after=upper)

    elif base_curr == 'US':
        if rel_curr in ('EU', 'UK', 'NZ'):
            return pd.DataFrame(relative.values, index=relative.index, columns = ['DEX'+rel_curr+'US'])**-1
            exit()
        else:
            return pd.DataFrame(relative.values, index=relative.index, columns = ['DEX'+rel_curr+'US'])
            exit()
    else:
        fxcode2 = 'DEX'+base_curr+'US'
        base_raw = web.DataReader(fxcode2, 'fred')
        base_conv = base_raw.convert_objects(convert_numeric=True)
        base = base_conv.truncate(before=lower, after=upper)**-1

    new_label = 'DEX'+rel_curr+base_curr
    new_rate = pd.DataFrame(relative.values*base.values, index=relative.index, columns = [new_label])
    return new_rate

def joint_plot(base, rel_1, rel_2=None, rel_3=None, lower=None, upper=None):
    """
    Plots the value of a "base" currency in terms of 1-3 "relative" currencies
    in a given time interval

    Parameters
    ----------
    base: the base currency
    rel1, rel2, rel3: the relative currencies

        Choose from the following, wrapping the currency code in single
        quotation marks, e.g. jointplot('EU', rel1='NO')

        currency code       currency

            US                  US Dollars
            EU                  Euros
            UK                  British Pounds
            NZ                  New Zealand Dollars
            JP                  Japanese Yen
            CH                  Chinese Yuan
            CA                  Canadian Dollars
            BZ                  Brazilian Reals
            MX                  Mexican Pesos
            SZ                  Swiss Francs
            KO                  Korean Won
            IN                  Indian Rupees
            TH                  Thai Baht
            TA                  Taiwanese Dollars
            SF                  South African Rand
            VZ                  Venezuelan Bolivares
            MA                  Malaysian Ringgit
            SI                  Singaporean Dollars
            NO                  Norwegian Kroner
            HK                  Hong Kong Dollars
            SD                  Swedish Kroner
            DN                  Danish Kroner
            SL                  Sri Lankan Rupees

        Make sure to wrap in single quotations.


    lower: lower bound for dates of interest
    upper: upper bound for dates of interest

            wrap in single quotations and use YYYY-MM-DD format
            default is to use first available date for lower and latest data
            for upper

        e.g. joint_plot('US', 'MA', rel_2='UK', rel_3='SI', lower='2010-03-01')
        concurrently plots the exchange rate of the US dollar in terms of the
        Malaysian Ringgit, the British Pound, and the Singaporean Dollar since
        March 1, 2010.

    """
    joint = import_fx(rel_1, base, lower, upper)
    if rel_2 != None:
        joint = joint.join(import_fx(rel_2,base, lower, upper))
    if rel_3 != None:
        joint = joint.join(import_fx(rel_3,base, lower, upper))
    joint.interpolate().plot(subplots = True)

# The Swiss franc since Jan. 2011 in US Dollars, Euros, and British Pounds
joint_plot('SZ', 'US', rel_2='EU', rel_3='UK', lower = '2011-01-01')
