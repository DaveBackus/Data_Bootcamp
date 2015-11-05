### Data Bootcamp Mini-Course, 2015 edition  

This document:  https://github.com/DaveBackus/Data_Bootcamp/blob/master/Markdown/bootcamp_mini_2015.md

A brief overview of the tools and skills you'll learn in **[Data Bootcamp](https://github.com/DaveBackus/Data_Bootcamp#data-bootcamp)**, a course at NYU's Stern School of Business. Developed by Dave Backus, Chase Coleman, Spencer Lyon, and Glenn Okun.  With the help and support of Sarah Beckett-Hile, Hersh Iyer, Itamar Snir, and executives at Amazon.  

November 6 and 13, 2-4pm, Tisch UC 25
* Session 1:  Python fundamentals, examples    
* Session 2:  data management (Pandas), graphics (Matplotlib), examples 

---
#### Announcements

We'll post announcements here.  

**Bring your computer to class.**  We'll put it to work.  

**Before the first session.** 
Please install the **Anaconda** distribution of **Python 3.4 or (now) 3.5** from the download page: <https://www.continuum.io/downloads>.  If you have trouble, read [this chapter](https://davebackus.gitbooks.io/test/content/installing-python.html), but keep in mind that the Anaconda download page has changed a little since it was written.  Or come 20 minutes early to the first session and we'll (try to) set you up.  

**Code for class.**  [Class 1](https://github.com/DaveBackus/Data_Bootcamp/blob/master/Code/Python/bootcamp_fundamentals_1.py) | Class 2  (data | graphics | examples) 
We recommend you download it before class:  Click on the link, then click on the Raw button in the upper right, then save in a directory where you can find it.  It's best if you add your initials to the end of the file name to indicate it's your version, which you can modify as you think best.  

---

#### Session 1 

**Overview**

Where we're headed 
* Think of a **picture** you'd like to produce -- a "visualization" 
* And about what **data** you'll need 
* And the **coding skills** to get there 
* Examples:  [Gapminder](http://www.gapminder.org/world/) | [cancer screening](http://www.vox.com/2015/10/28/9631500/does-mammography-work) | [Uber in NYC](http://fivethirtyeight.com/features/uber-is-serving-new-yorks-outer-boroughs-more-than-taxis-are/) 

Philosophy  
* Target **coding novices**, no prior experience required or expected 
* Not a typical programming course:  cover only those aspects of Python relevant to data work 

Rules to live by 
* **Don't panic**.  The jargon and concepts will seem mysterious at first, but if you keep with it they'll start to make sense.  
* **Ask for help**.  Raise your hand if you don't follow what we're doing.  
* Develop your **Google fu**.  Learn to find answers to your questions with Google.   

<!-- 
**Skills** 

Why skills? 
* Businesses want people with skills (duh!) 

Why code? 
* One of the skills businesses value (not the only one) 
* Do things Excel can't do, and do them faster 

Why Python? 
* User-friendly 
* Broad range of applications  

-->

**Prelaunch checklist**

Install Anaconda 
* Google "anaconda download"
* Download installer for **Python 3.5** 
* Run installer 

Locate this file in a browser 
* Google "nyu data bootcamp" and follow links 
* Or:  type in url at the top 

Save today's code file in a handy place 
* Create directory/folder `Data_Bootcamp` 
* Click on code link above, then Raw button 
* Save file in `Data_Bootcamp` directory 

Launch 
* Look for **Launcher** in your programs
* Start it up (takes a minute) 
* Click on **Spyder** (another minute) 

**Programming basics** 

Our typical program 
* Input data 
* Manipulate data until it's in the form we want 
* Produce a compelling graphic 

Spyder basics  
* Editor 
* IPython console, object inspector    

Python basics 
* Calculations, assignments, comments, strings and quotes, lists, built-in functions (print, type), objects and methods, tab completion, getting help 

If you'd like to do more of this on your own:     
* Work your way through the [Codecademy](https://www.codecademy.com/tracks/python) course.  You can stop when you get to Advanced Topics.     
* Read the Python Fundamentals chapters of our [Data Bootcamp book](https://www.gitbook.com/book/davebackus/test/details).
* Read Mevan's [wonderful guide](https://medium.com/keep-learning-keep-growing/how-i-learned-to-stop-worrying-and-love-the-code-af1a809457c7) "to the misconceptions and anxieties that people like me -- people newly learning to code -- may have."  

**Next Wednesday or Thursday:**  Work through the review below.

---

#### Session 2 

**Review.**  Sketch out notes to explain each to your neighbor:     
* `x = 107.3`
* `y = '3.14159'`
* `z = [3, 2, 7, 2]`
* `type(x)`
* `type?`
* `w = z.count(2)` (This one's harder; the idea is to use the available help to find out what it does. Or just try it.) 


**WORK IN PROGRESS FROM HERE ON**

**Data and graphics** 

Packages 
* Packages/libraries/modules = plug-ins that add new tools to Python 
* There are lots of them
* Our favs:  Pandas (data), Matplotlib (graphics)
* The `import` command

Data basics 
* `import pandas as pd` 
* Reading spreadsheets and csv files 
* Dataframes:  column labels, row labels  
* Examples:  ... 
* Internet sources with APIs:  FRED, World Bank 
 
Graphics basics 
* `import matplotlib`
* Approach 1:  `plot(x,y)`
* Approach 2:  apply methods to `fig, ax` 
* Parameters and styles 
* Approach 3:  apply `plot` method to dataframe 

Examples 
* Cancer:  http://www.vox.com/2015/10/28/9631500/does-mammography-work
* Gapminder:  http://www.gapminder.org/world/
* Uber:  http://fivethirtyeight.com/features/uber-is-serving-new-yorks-outer-boroughs-more-than-taxis-are/
* Indicators of US economic conditions 
* Emerging market indicators  
* Healthcare spending 

Following up:  


A product of the #nyuecon Python factory 
