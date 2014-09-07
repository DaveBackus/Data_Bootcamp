"""
Cooley-Rupert-style business cycle figures for Backus-Ferriere-Zin paper, 
"Risk and ambiguity in models of business cycles,"  Carnegie-Rochester-NYU 
conference paper, April 2014.

FRED codes:  ["GDPC1", "PCECC96", "GPDIC96", "OPHNFB"]
(gdp, consumption, investment, labor productivity)

Cooley-Rupert link:  http://econsnapshot.com/
Paper link:  http://pages.stern.nyu.edu/~dbackus/BFZ/ms/BFZ_CRN_latest.pdf

Authors: Chase Coleman and Spencer Lyon
Date: 06/24/2014

TODO: Add labels to the plots
    Increase thickness of current recession
    Smaller fonts in legend 
    Identify FRED code?
"""
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.data import DataReader

# legend control, subject to change 
# http://stackoverflow.com/questions/7125009/how-to-change-legend-size-with-matplotlib-pyplot
params = {'legend.fontsize': 10,
          'legend.linewidth': 0.5}  # this one doesn't seem to do anything 
plt.rcParams.update(params)


def chopseries(data, indices, periods=40):
    """
    Takes a series and chops it into pieces starting with cyclical peaks.
    Formally, it turns it into a data frame starting at each peak index date
    and running for the number of periods specified (default is 40)

    Parameters
    ----------
    data : pd.Series
        The Series that should be chopped. Index should be a
        DatetimeIndex

    indices : pd.DatetimeIndex
        A pandas DatetimeIndex where each item represents the beginning
        of a cycle

    periods : int, optional(default=40)
        An integer specifying the maximum number of periods to retain
        in each cycle. In other words, the function will attempt to keep
        `periods` items, starting at each date in indices

    Returns
    -------
    new_data : pd.DataFrame
        A pd.DataFrame with columns named for the year the cycle
        started. The data is a subset of the original series passed into
        the function
    """
    # Number or series to plot
    n = len(indices)
    c_names = ["%d cycle" % x.year for x in indices]

    new_data = pd.DataFrame(np.empty((periods, n)), columns=c_names)

    for num, date in enumerate(indices):
        date_loc = data.index.get_loc(date)
        try:
            new_data[c_names[num]] = data.ix[date_loc:date_loc+periods].values
        except:
            the_values = data.ix[date_loc:].values
            length = the_values.size
            stupiddata = np.concatenate([the_values.squeeze(),
                                        np.nan*np.ones(periods-length)])
            new_data[c_names[num]] = stupiddata

    return new_data


def peak_begin_dates(start="01/01/1972", end=datetime.now()):
    """
    Use the fred dataset `USRECQ` to determine the beginning of the
    peaks before all recessions between dates start and end

    Parameters
    ----------
    start : string or datetime.datetime, optional(default='01/01/1972')
        A string or other acceptable pandas date identifier that marks
        the beginning of the window for which we will search for starts
        of peaks

    end : string or datetime.datetime, optional(default=datetime.now())
        The ending date of the search window

    Returns
    -------
    rec_startind : pd.DatetimeIndex
        A pandas DatetimeIndex representing the starting points of each
        "peak" from start to end
    """
    # Get quarterly recession dates from FRED
    rec_dates = DataReader("USRECQ", "fred", start=start)
    one_vals = np.where(rec_dates == 1)[0]
    rec_start = [one_vals[0]]

    # Find the beginning of the recession dates (Don't include ones that
    # begin within three years of a previous one -- hence the `+12`)
    for d in one_vals:
        if d > max(rec_start) + 12:
            rec_start.append(d)

    rec_startind = rec_dates.index[rec_start]

    return rec_startind


def manhandle_freddata(fred_series, nperiods=40,
                       changetype="log", start="01/01/1972",
                       saveshow="show", **plot_kwargs):
    """
    This function takes a string that corresponds to a data series from
    FRED and creates a DataFrame that takes this series and creates a
    new series that shows the percent change of the series starting at
    the beginning of every business cycle and ending `nperiods` quarters
    later using either log differences or percent change.

    By default it will start at the beginning of 1972 and additionally
    data should be quarterly

    If you would like to use multiple series, use python's map function:

        map(manhandle_freddata, [list of fred_series])  

    Parameters
    ----------
    fred_series : string
        A string representing the fred dataset identifier.

    nperiods : int, optional(default=40)
        The number of periods each cycle should represent. This is
        passed directly to the `chopseries` function

    changetype : string
        A string identifying how the percentage change should be
        computed. Acceptable values are `percent` or `log`

    start : string or datetime.datetime, optional(default='01/01/1972')
        A string or other acceptable pandas date identifier that marks
        the beginning of the window for which we will search for starts
        of peaks. This is passed directly to `pd.io.data.DataReader` to
        obtain the data set and to `peak_begin_dates` to determine
        starting periods for business cycle peaks

    plot_kwargs : other
        Other keyword arguments that will be passed directly to the
        `pd.DataFrame.plot` method when generating the plot. See pandas
        plotting documentation for an explanation of acceptable values

    Returns
    -------
    pct_change : pd.DataFrame
        The pandas DataFrame representing representing the percent
        change from the beginning of each peak, extended out `nperiods`

    Examples
    --------
    >>> rgdp = manhandle_freddata('GDPC1')  # produces real GDP plot 

    For more examples see the `examples.ipynb` notebook in this
    directory.
    """
    # Get data
    fred_data = DataReader(fred_series, "fred", start=start)

    # Get dates for start of peak
    peak_dates = peak_begin_dates(start=start)

    # Break the time-series into chunks for each recession
    chopped_data = chopseries(fred_data, peak_dates, periods=nperiods)

    # Compute percent changes.
    if changetype.lower() == "percent":
        pct_change = ((chopped_data / chopped_data.iloc[0] - 1)*100)
    elif changetype.lower() == "log":
        logged = np.log(chopped_data)
        pct_change = (logged - logged.iloc[0]) * 100.0

    # plot data 
    fig, (ax) = plt.subplots(1, 1)
    ax.set_ylabel("Percent change from previous peak")
    pct_change.index.name = "Quarters since previous peak"  # becomes x_label
    pct_change.plot(ax=ax, **plot_kwargs)
    ax.legend_.set_title("FRED: " + fred_series)  # set title on legend

    # add line for x-axis and show the plot.
    ax.axhline(y=0, xmin=0, xmax=nperiods, color='k', linewidth=1.5)
    
    # if saveshow="save" save plot as pdf file with name = FRED code 
    if saveshow=="save":
        fn =  "BFZ_" + fred_series + ".pdf"
        plt.savefig(fn)
    else:
        plt.show()

    return pct_change


if __name__ == '__main__':
    # Get Real GDP, Real Personal Consumption, Nonresidential Investment,
    # and Output per Hour from FRED
    fred_names = ["GDPC1", "PCECC96", "GPDIC96", "OPHNFB"]

    # gdpdiff, pceccdiff, gpdicdiff, ophnfbdiff = map(manhandle_freddata,
    #                                                   fred_names)

"""
Examples 
manhandle_freddata("GDPC1", saveshow="show")
manhandle_freddata("GDPC1", saveshow="save")
"""