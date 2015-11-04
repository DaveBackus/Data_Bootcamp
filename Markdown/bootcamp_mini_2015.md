### Data Bootcamp Mini-Course, 2015 edition  

A brief overview of the tools and skills you'll learn in **[Data Bootcamp](https://github.com/DaveBackus/Data_Bootcamp#data-bootcamp)**, a course at NYU's Stern School of Business. Developed by Dave Backus, Chase Coleman, Spencer Lyon, and Glenn Okun.  With the help and support of Sarah Beckett-Hile, Hersh Iyer, Itamar Snir, and executives at Amazon.  

November 6 and 13, 2-4pm, Tisch UC 25
* Session 1:  Python fundamentals   
* Session 2:  data management (Pandas), graphics (Matplotlib), examples 

---
#### Announcements

We'll post announcements here.  

**Bring your computer to class.**  We'll put it to work.  

**Before the first session.** 
Please install the **Anaconda** distribution of **Python 3.4 or (now) 3.5** from the download page: <https://www.continuum.io/downloads>.  If you have trouble, read [this chapter](https://davebackus.gitbooks.io/test/content/installing-python.html), but keep in mind that the Anaconda download page has changed a little since it was written.  Or come 20 minutes early to the first session and we'll (try to) set you up.  

**Code used in class.**  [Class 1](https://github.com/DaveBackus/Data_Bootcamp/blob/master/Code/Python/bootcamp_fundamentals_1.py) | Class 2  
We recommend you download it before class:  Click on the link, then click on the Raw button in the upper right, then save in a directory where you can find it.  It's best if you add your initials to the end of the file name to indicate it's your version, which you can modify as you think best.  

---

#### Session 1 

Where we're headed 
* Think of a **picture** you'd like to produce -- a "visualization" 
* And about what **data** you'll need 
* And the **coding skills** to get there 
* Examples:  [Gapminder](http://www.gapminder.org/world/) | [cancer screening](http://www.vox.com/2015/10/28/9631500/does-mammography-work) 

Rules to live by 
* **Don't panic**.  The jargon and concepts will seem mysterious at first, but if you keep with it they'll start to make sense.  
* **Ask for help**.  Raise your hand if you don't follow what we're doing.  
* Develop your **Google fu**.  Learn to find answers to your questions with Google.   

**Skills** 

Why skills? 
* Businesses want people with skills (duh!) 

Why code? 
* One of the skills businesses value (not the only one) 
* Do things Excel can't do, and do them faster 

Why Python? 
* User-friendly 
* Broad range of applications  

**Getting set up**

Open browser 
* Google "nyu data bootcamp" 
* Find this page (look for link, or go to Markdown directory) 

Programming setups (and associated jargon)    
* Distribution (**Anaconda**)  
* Program (Python) 
* Environment:  **Spyder**, Jupyter, Pycharm, many others  

Spyder (start it up) 
* Editor 
* IPython console, object inspector    

**Programming basics** 

Our typical program 
* Input data 
* Manipulate data until it's in the form we want 
* Produce a compelling graphic 

Python basics 
* Calculations, assignments, comments, strings and quotes, lists, built-in functions (print, type), objects and methods, tab completion, getting help 

If you'd like to do more of this on your own:     
* Work your way through the [Codecademy](https://www.codecademy.com/tracks/python) course.  You can stop when you get to Advanced Topics.     
* Read the Python Fundamentals chapters of our [Data Bootcamp book](https://www.gitbook.com/book/davebackus/test/details).
* Read Mevan's [wonderful guide](https://medium.com/keep-learning-keep-growing/how-i-learned-to-stop-worrying-and-love-the-code-af1a809457c7) "to the misconceptions and anxieties that people like me -- people newly learning to code -- may have."  

---

#### Session 2 

**Review.**  Write down notes that help you explain each of the following to your neighbor:     
* `x = 107.3`
* `y = '3.14159'`
* `z = [x, y, 123]`
* `type(x)`
* `type?`
* method 
* object explorer 

**Data and graphics** 

Packages 
* Add new functionality to core language 
* Our favs:  Pandas (data), Matplotlib (graphics)
* The `import` command

Data basics 
* `import pandas as pd` 
* Reading spreadsheets and csv files 
* Dataframes:  column labels, 
* Examples:  test file, IMDb, ... 
* Internet sources with APIs:  FRED, World Bank 
 
Graphics basics 
* `import matplotlib`
* Approach 1:  `plot(x,y)`
* Approach 2:  apply methods to `fig, ax` 
* Parameters and styles 
* Approach 3:  apply `plot` method to dataframe 

**WORK IN PROGRESS FROM HERE ON**

Examples 
* Cancer:  http://www.vox.com/2015/10/28/9631500/does-mammography-work
* Gapminder:  http://www.gapminder.org/world/
* Uber:  http://fivethirtyeight.com/features/uber-is-serving-new-yorks-outer-boroughs-more-than-taxis-are/
* Indicators of US economic conditions 
* Emerging market indicators  
* Healthcare spending 

Following up:  


A product of the #nyuecon Python factory 
