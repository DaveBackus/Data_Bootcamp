-------------
Python basics
-------------

We're going to run through some of the basics of Python.
In our experience, once you have the basics down, 
you can fill in missing pieces yourself.  

By the end of the first week, we'll be running some basic programs, 
entering and manipulating data, and producing basic graphics. 
We'll do more complex data manipulations and graphics next week.  

The code is (will be!) posted at 
`GitHub <https://github.com/DaveBackus/Data_Bootcamp/tree/master/Code/Python/bootcamp_basics.py>`_.
Here and throughout the code is Python 3.4. 
That won't matter for most things, but it does for some.  

The references at the end direct you to useful online sources with more
information about the same topics.  


Coding environment
------------------

Our coding environment is Spyder.
Start it up as we described in ??
On the left we have an editor where we enter Python commands.
Various 'buttons' at the top allow us to run some or all of them.  
On the lower right, we have an IPython console
where results appear when we execute them.  
The results are reported with numbers in square brackets:  [1], [2], etc.  
We can also type commands directly in the console,
which we use to experiment.  

The combination of an editor and an IPython console is a classic coding environment.
We think it's the obvious choice and will use it throughout.  
Some of colleagues prefer to use other editors -- Sublime text, Emacs, VIM --
but Spyder strikes us as the obvious choice for noexperts.  

Python 2 or 3?
--------------

We'll be using Python 3.  The differences from Python
are minor, but there enough of them that you don't want to mix them up.
If you installed Python 2.7 (say), please stop and install Python 3.4 or later.  


Comments, code cells, and printing 
----------------------------------

*Comments.* We think programs should have lots of comments.  
Imagine your code as an explanation for others of what you've done, and why.  
The device in Python is the hashtag #.  
Anything in a line after # is a comment.  
For example::

	# comment
	x = 7	# another comment: this line assigns the value 7 to the variable x 

We also use block comments.  Anything between triple quotes is a comment.
By convention we use double quotes for this:: 

	"""
	Comments about the program.
	Program written for Data Bootcamp, NYU Stern, 2014.
	Section 1 is about comments.
	"""

*Code cells.*    
In Spyder we can use '#%%' to divide a program into blocks of code called code cells. 
We can run code cells separately, which is easier when we're debugging
than running the whole program.  

*Printing.*  We'll use the print command.  If we type print(x) in the IPython console, 
the command and its result look like this:: 

	In [1]: print(x) 
	Out[1]: 7 

In the IPython console, we can also just type the variable name x with the same effect::

	In [2]: x 
	Out[2]: 7 


Calculations and assignments 
----------------------------

As we just saw, we can assign calculations (and other things) to variables.
For example::

	x = 2*3 
	y = 2**3 
	z = 2/3 
	#%% 

The first one multiplies 2 times 3 (6), the second takes 2 to the power 3 (8), 
and the third divides 2 by 3 (a floating point approximation of two-thirds).  
If we type this into Spyder's editor, we create a code cell.
If we then click on one of the small green triangles at the top
-- the one that says 'Run current cell' --
the commands are echoed in the console but nothing else happens.  
We could print the results,  
but it's easier to look in the Variable explorer (check the tabs at the right).

Our last example ::  

	w = log(x)

generates the error :: 

	File "<ipython-input-xyzzy>", line 17, in <module>  
	w = log(x)
	NameError: name 'log' is not defined

This reminds us that basic Python doesn't include functions like log.
If we want them, we need to add them, 
which is easy to do, but something for later.  


*Practice.* 
(i) Set u equal to the square root of 5. 
(ii) Compute the third power of u.  


Strings
-------

mmm

  first = 'Dave'
  last  = 'Backus'
  full  = first + ' ' + last

Practice.  Construct your name in the form:  Last, First. 


Slicing
-------



Lists
-----



Two commands:  type and len
---------------------------



Objects and methods
-------------------

tab completion
object explorer 


Practice.  Start with your name in the form (last, first) and decomposite it into
separate first and last names. 


Control flow language 
---------------------


Conditionals (booleans) 
-----------------------

Code::

  >>> x == 7



While loops 
-----------


If statements etc 
-----------------


For loops 
---------

Also range 


List comprehensions 
-------------------

Obscure terminology, but useful...  


Functions 
---------

indentation, return


References 
----------

Spyder.  

`Python tutorial <https://docs.python.org/3.4/tutorial/introduction.html>`_.  
This is very good.  

Google style guide.  How to write understandable code.

Quant Econ.  Intro...

Python 2 or 3?