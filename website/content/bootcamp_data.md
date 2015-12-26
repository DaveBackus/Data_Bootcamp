# Data Bootcamp:  Data sources 

**UNDER CONSTRUCTION**

There's an enormous amount of public data available online.  Here are some highlights:      

## Data about countries 

Go-to sources:   

* **FRED.**  [Large collection](https://research.stlouisfed.org/fred2/) of easy-to-use time series data from the St Louis Fed.  Comes with online graphing tools, Excel plug-in, etc.  We use the [Pandas tool](http://pandas.pydata.org/pandas-docs/stable/remote_data.html). 

* **World Bank.**  [Annual data](http://data.worldbank.org/) related to the economic and social environments of a broad range of countries.  You can download the whole thing as a large csv or (our preference) use the [Pandas tool](http://pandas.pydata.org/pandas-docs/stable/remote_data.html).  The latter gives us a doubly indexed dataframe, with observations indexed by year and country.  

Others:

* **WEO.**  The IMF's [World Economic Outlook](https://www.imf.org/external/ns/cs.aspx?id=28) comes out twice a year.  Basic macroeconomic data for most countries, from 1980 to 5-10 years in the future.  We provide code in class to read in the whole thing.  

* **PWT.** The Penn World Table is the best single source of basic macroeconomic data presented on a comparable basis (""PPP adjusted") for most countries.  Annual from 1950 to (roughly) 3-4 years ago.  We prefer to read in the whole thing from a spreadsheet.  

* **UN Population data.**  [Annual data](http://esa.un.org/unpd/wpp/Download/Standard/Population/) for most countries of the population by age.  Includes estimates from 1950 and projections to 2100.  We read the whole thing from a spreadsheet.  


## Financial data 


* **Fama-French equity returns.**  The leading source of equity data for investment research, courtesy of Gene Fama and Ken French.  Text files are [Ken French's website](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) are easily read into Excel.  The [Pandas tool](http://pandas.pydata.org/pandas-docs/stable/remote_data.html) is even better, but it's currently broken.

* **Yahoo and Google finance.**  


## Survey data

There is lots of survey data online, which allows us to see not only average outcomes (the unemployment rate) but individual outcomes (whether people with specific characteristics are employed).  Anthony Damico's [asdfree collection](http://www.asdfree.com/) includes an extensive list with descriptions.  

Here are some we have used:  

* **ACS.** The American Community Survey from the US Census...  Examples...  Guide...  

* **ATUS.**  The American Time Use Survey 

* **MEPS.**  


## Miscellaneous other sources 


* **Airbnb.**  [Data](http://insideairbnb.com/get-the-data.html) on locations, rentals, and reviews. 


* **NYC Open Data.**  

https://data.cityofnewyork.us/
Taxi data, restaurant inspections, and much much more.  


[538](http://fivethirtyeight.com/features/uber-is-serving-new-yorks-outer-boroughs-more-than-taxis-are/); their Uber data comes from another source, but they posted all of it on their [repo]()

[I Quant NY](http://iquantny.tumblr.com/) is a blog devoted to NYC Open data.   
