# Data Bootcamp:  Data sources & applications 

There's an enormous amount of public data available online:  data about countries, about markets, about individuals, and about companies.  Here are some of our favorites; we use most of them in class.  We link to a larger but less well organized list at the end.  


## Data about countries 

Go-to sources:   

* **FRED.**  [Large collection](https://research.stlouisfed.org/fred2/) of easy-to-use time series data from the St Louis Fed.  Comes with online graphing tools, Excel plug-in, etc.  We use the [Pandas tool](http://pandas.pydata.org/pandas-docs/stable/remote_data.html). One thing to keep in mind:  it's a mess if you mix data with different "frequencies" (monthly, quarterly, annual).  

* **World Bank.**  [Annual data](http://data.worldbank.org/) on the economic and social environments of a broad range of countries.  You can download the whole thing as a large csv or (our preference) use the [Pandas tool](http://pandas.pydata.org/pandas-docs/stable/remote_data.html).  The latter gives us doubly indexed dataframes, with observations indexed by year and country.  

Others we like:

* **WEO.**  The IMF's [World Economic Outlook](https://www.imf.org/external/ns/cs.aspx?id=28) comes out twice a year.  Annual macroeconomic data for most countries, 1980 to 5-10 years in the future.  We read the whole thing from their spreadsheet link. 

* **PWT.** The [Penn World Table](http://www.rug.nl/research/ggdc/data/pwt/?lang=en) is the best single source of basic macroeconomic data presented on a comparable basis (""PPP adjusted") for most countries.  Annual from 1950 to (roughly) 3-4 years ago.  We read the whole thing from their spreadsheet link.  

* **UN Population data.**  [Annual data](http://esa.un.org/unpd/wpp/Download/Standard/Population/) for most countries of the population by age.  Includes estimates from 1950 and projections to 2100.  We read the whole thing from their spreadsheet link. Also data on births (fertility) and deaths (mortality).    

## Data about financial markets 

* **Fama-French equity returns.**  The leading source of equity returns for investment research, courtesy of Gene Fama and Ken French.  Text files on [Ken French's website](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) are easily read into Excel.  The [Pandas tool](http://pandas.pydata.org/pandas-docs/stable/remote_data.html) is even better -- when it works. 

* **Yahoo and Google finance.**  Pandas also has [tools](http://pandas.pydata.org/pandas-docs/stable/remote_data.html) for accessing daily stock prices and other financial data.  

* **Quandl.**  A [nice aggregator](https://www.quandl.com/) of economic and financial information. Uses the Quandl package, which comes with Anaconda.  Much of it is free, but they also serve as an interface to paid data subscriptions.   


## Data about individuals 

There is lots of survey data online, which gives us individual outcomes (the employment status of people with specific characteristics, for example) as well as the usual average outcomes (the unemployment rate). That allows us to compare outcomes of various groups:  rich and poor, young and old, black and white, and so on.  Anthony Damico's [asdfree collection](http://www.asdfree.com/) includes an extensive list with descriptions.  Gianluca Violante's [guide to micro data](http://www.econ.nyu.edu/user/violante/NYUTeaching/QM/Fall15/Lectures/Lecture2_Data.pdf) is a a similar list focused on US sources.  It's aimed at PhD students, but you should get the idea.  These sources are not necessarily easy to use, but they're incredibly informative. Keep in mind that we have experts on hand to help with any that interest you.  

Here are some we have used:  

* **ACS.** The [American Community Survey](https://www.census.gov/programs-surveys/acs/) from the US Census covers demography (age, sex, ethnicity, location), economics (employment and income), education, and many other [subjects](https://www.census.gov/programs-surveys/acs/guidance/subjects.html). The [Public Use Microdata Sample](https://www.census.gov/programs-surveys/acs/technical-documentation/pums.html) (PUMS) contains individual responses. This [guide](https://source.opennews.org/en-US/learning/how-use-census-bureau-american-community-survey/) was written for journalists. Ari Lambstein has a [shorter guide](http://www.arilamstein.com/blog/2016/02/15/taking-next-step-census-data/) to navigating the universe of Census surveys.  The Minnesota Population Center has a nice [user interface](https://usa.ipums.org/usa/) for the ACS and other micro-data sources.  

* **CPS.** The [Current Population Survey](http://www.census.gov/programs-surveys/cps.html) collects information about employment status, income, and a broad range of demographic variables (age, education, ethnicity).  The [Minnesota interface](https://cps.ipums.org/cps/) is useful here, too.  

* **ATUS.**  The [American Time Use Survey](http://www.bls.gov/tus/) describes how people spend their time:  employed, doing housework, watching tv, etc.  This [article](http://scholar.princeton.edu/sites/default/files/annurev-economics-111809-125129_0.pdf) summarizes academic work done on similar surveys in many countries. [The Times](http://www.nytimes.com/interactive/2009/07/31/business/20080801-metrics-graphic.html) is unusually fond of this survey.

* **MEPS.**  The [Medical Expenditure Panel Survey](http://meps.ahrq.gov/mepsweb/) is the leading source of information about individual healthcare, including insurance status and expenditures.  


## Miscellaneous other sources 

Some that appeal to us, but please send suggestions:  

* **Kaggle datasets.**  Kaggle, the data competition outfit, has just opened a [datasets section](https://www.kaggle.com/datasets) that comes with data, documentation, coding enviroments, and forums.  More on [their blog](http://blog.kaggle.com/2016/01/19/introducing-kaggle-datasets/).

* **Airbnb.**  [Data](http://insideairbnb.com/get-the-data.html) on locations, rentals, and reviews. Chase loves this.  Good input for a map project?  

* **NYC Open Data.**  [Data](https://data.cityofnewyork.us/) collected by the City of New York. There's too much to summarize, but it includes taxis (every taxi ride in the city), restaurant inspections, and much much more.  [I Quant NY](http://iquantny.tumblr.com/) has some applications. [538](http://fivethirtyeight.com/tag/uber/) combined the taxi data with similar information about Uber, which they posted on their [repo](https://github.com/fivethirtyeight/uber-tlc-foil-response)

<!--
* **Pew Research Center.**  We haven't used it, but they do lots of surveys and post [the data](http://www.pewresearch.org/) on their website.   
-->	

## Data applications 

Data journalism:

* ESPN's **538 Blog**.  The high end of data journalism.  They often post their data as csv's in their [data repository](https://github.com/fivethirtyeight/data/blob/master/README.md).   

* NYT's **Upshot**.  Great graphics, including [these](http://www.nytimes.com/interactive/2015/12/15/upshot/the-best-places-for-better-cheaper-health-care-arent-what-experts-thought.html) [two](http://www.nytimes.com/interactive/2009/07/31/business/20080801-metrics-graphic.html) examples. They list sources, but don't typically post data.  

* Tim Taylor's **Conversable Economist** blog.  Tim's a former journalist, so a better writer than most economists.  He has a [daily post](http://conversableeconomist.blogspot.com/) about a topical economic issue, often with graphs we can use to track down data sources. If you don't recognize a source, ask us about it.  

Graphics:

* **Our World in Data.** A [website](http://ourworldindata.org/) devoted to data visualizations.  There's an economic development tenor, but they cover a broad range of topics:  population, energy, education, and much much more.    

* **Flowing Data.**  Nathan Yau's [daily graphic](http://flowingdata.com/). A good source of ideas and advice.  

* **VizWiz.** Andy Kriebel's ["visualization" blog](http://vizwiz.blogspot.com/).  A steady stream of examples and advice, including the invaluable Makeover Monday.  Tagline:  "Friends Don't Let Friends Use Pie Charts." 

* **Data is beautiful.**  On [Reddit](https://www.reddit.com/r/dataisbeautiful/). Relatively unfiltered, but a good source of ideas.  


## More

This is **not for the timid**, but we have a **[huge collection](https://docs.google.com/document/d/1L2ZDKFyyqfOrCGbNcCIE9mmgap4tjkTNuw32hK4c6BI/edit?usp=sharing)** of data sources and applications.  Get a cold drink and a comfy chair and see what strikes your fancy. Active investing?  Movie grosses? Sports? College Scorecard? Shooting deaths? All this and more.  Similar courage is called for if you go to **[Awesome Public Datasets](https://github.com/caesar0301/awesome-public-datasets#awesome-public-datasets)**.  There's way too much there, but one advantage is that it goes beyond economics and finance.  


