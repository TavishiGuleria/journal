# Journal
---

`05-05-2020`
### Data Analysis with Python and Pandas
#### Intro to Dataframe
 - 2D data structure, with rows and columns (like a table)
 - Don't care about rows/columns. Number of reference points to extract a value. 2D because of 2 points of reference
 - 3D when we have 2 tables and need a data point from one of them
 - NaN: Not a number  
 - If column has NaN anywhere. Pnadas converts to floating point (in order to support NaN values)

#### Methods and sttributes shared between series and dataframes
- Attribute is a piece of data that belongs to an object. Objects internal state. What ot comprises of
- Method is a command/message to send to an object, ask object to do.
- Methods - .head(), .tail()
- Attribute - .index, .values, .shape, .dtype, .dtype.value_count() (method .value_counts on attribute .dtype)
- Most important (object, attributes, methods)
- Exclusive attributs/methods for dataframes: .columns, .axes, .info (big picture summary)

#### Differences between shared methods
- Think about approach a problem. How's the object and how different methods apply
- If we want to sum horizontally and not vertically: x.sum(axes = 1) or x.sum(axes = "columns")
- Some work the same as for series some have slight differences

#### Select one column from Dataframe
- x.(column name case sensitive) ~ for easy column names but doesn't work all the time
- Bracket syntax to get columns from a dataframe
- x["Column name"]
- Single column extracted from dataframe becomes a series

#### Select 2 or more colums from Dataframe
- X[["a","b"]]
- When we extract 2 or more columns we always get new dataframe
- We can switch columns X[["b","a"]]

#### Add neew column to Dataframe
- X ["a"] = "b" (b is new column) (all values in column are same)
- X.insert(3, column = "a", value = "b")

#### Broadcasting operations



--- 

`29-04-2020`
### Data Analysis with Python and Pandas
#### Series
- One D labelled array
- pd.(tab???) this is dot notation
- pd.Series(xxx) ~this gives the panda series
- Object means string
- webster = {"x" : "y",
             "x" : "y"}
  pd.Series(webster)

#### Attributes
- Summarise details of a list
- s = pandas.Series(x)
- s.(tab??)
- s.values (no brackets needed)
- s.index
- s.dtype
- pokemon.is_unique (returns true/false)
- pokemon.ndim
- pokemon.shape (rows, column(more than 1D))
- pokemon.size (gives values, counts null values)
- pokemon.name (can reasign name)

#### Methods
- Does something to the object
- s.sum()

#### Parameters and arguments
- eg. Difficulty (parameter) = easy(argument), medium, hard
- pd.Series(Shift + Tab??????)
- pd.Series(data = xxx, index = yyy)

#### Import series with .read_csv()
-pd.read_csv()
-pd.read_csv("pokemon.csv") ~imports dataframes
pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)

#### .head() and .tail() method
-pokemon.head(number?) ~ makes copy and can store again

#### Python built-in functions
- len(xxx)
- type(xxx)
- dir(xxx) ~ gives attributes and methods
- sorted(xxx)
- list(xxx)
- double click grey area to condense
- dict(xxx)
- max(xxx)
- min(xxx)

#### .sort_values()
- pokemon.sort_values() ~ alphabetically, brand new series created 
- pokemon.sort_values().head ~ method chaining
- pokemon.sort_values(ascending = False).tail 
- google.sort_values(ascending = False).head(1) ~ googles highest stock price

#### Pythons 'in' keyword
- permanently modify the objec the method is called on
- x in [x, y, z]
- Problem; looks at index for in keyword 
- x in x.values

#### Extract series value by index position
- pokemon [100, 200, 300]  ~ brand new series from these index
- pokemon [50:100:2] ~ all from 50 to 99, sets of 2
- pokemon [-30:]

#### Extract series value by index label
- pokemon.read_csv("pokemon,csv", index_col = "pokemon", squeeze = True)
- pokemon.reindex(index = ["x","y"])

#### .get() method
- pokemon.read_csv("pokemon,csv", index_col = "pokemon", squeeze = True)
- pokemon.sort_index(inplace = True)
- pokemon.head(3)
- pokemon.get(3)
- pokemon.get("xxx")
- pokemon.get([0, 5])
- pokemon.get(["xxx", "yyy"])
- Wrong index will give nothing, then
- pokemon.get(key = "zzz", default = "Not in list") ~ even if 1 woption is wrong gives, default 

#### Math method on series object
- pokemon.count ~ it excludes null values (different from pokemon.len)
- x.std()
- x.min()
- x.max()
- x.median()
- x.mode()
- x.described() ~ stastical summary
- many other stastical, math and economics methods (on general page)

#### .idmax and .idmin methods
- index labels with largest and smallest value in series
- x[x.idmin()]

#### .value_count() method
- pokemon.value_count() ~ number of times an item occurs
- pokemon.value_count().sum  
- pokemon.value_count(ascending = True)

#### .apply() method
- Calls a function on every single value in the series
- def classify_performance(number):
      if number < 300:
      return "Ok"
      elif number >= 300:
      return "satisfactory"
      else:
      return "excellent"
- x.apply(classify_performance)
- x.apply(lambda stock_price : stock_price + 1) ~ simpler operation than a function

#### .map() method
- maps values of series to other collection of data
- x.map(y) ~ x looks for same values in index of y and returns corrosponding value from other series
- When there are 2 different data types 

---

#### Dictionary
- xxx = {"key": yyy,
          "Key2": yyy
        }
- extract xxx("key2")

#### Operators
- 1 == 1 (gives true/false)
- 1 != 2 (gives true/false)
- etc...

#### Function
- Reusable chunk of code
- def convert_to_F(CTemp): 
      product = CTemp * 1.8
      final = product + 32
      return = final 
- To execute convert_to_F(xx)

---

`27-04-2020`
### Data Analysis with Python and Pandas
#### Jupyter notebook interface
- Keyboard shortcuts at insert
- To make it minimilistic - Toggle and remove numbers
- Insert let's you insert etc. cells
- Cell menu - various helper run options
- Kernel - when notebook is not responsive - use to restart and run
- Edit - to edit cell 

#### Cell types and modes
- Code dropdown options
- Markdown! (formatting using symbols)
- Edit mode 
- Command mode (esc key - keyboard shortcuts y and m to edit the notebook)

#### Keyboard shortcuts
- Command mode using esc key - blue outline
- H key - help for all shortcuts
- B key - create cells below
- A key - create cells above
- DD key - delete's cell
- X key - cut cell

#### Import libraries to notebook
- Pandas is an example of a solution built by developers to solve common problems. Such packages are also there for other applications
- In the server we installed the libraries, doesn't mean that its available (to conserve memory) - so explicitly specify
- import pandas as pd 
- import numpy as np
- Example pd.__version__

#### Data types and variables
- comments (using '#')
- integers, floating point, strings("xxx"), bollean (true/false)
- type (xxx) gives the type
- variable are place holders
- '=' right side analysed first 

#### Lists (array)
- Data container that can store multiple values 
- [x,x,x] (data types don't need to be consistant, but is prefered)
- len (xxx) gives length of list
- xxx[4] gives index valus. Index starts counting at 0, final is n-1

---

`24-04-2020`
### Data Analysis with Python and Pandas
#### Starting up
- Open Anaconda prompt from the search menu
- To check for all environments present: conda info --envs
- To create new environemnt: conda create --name xxx (in the course - pandas_udemy playground)
- To activate environment: conda activate pandas_udemyplayground
- Now Install packages: conda install pandas jupyter bottleneck numexpr matplotlib
- In future to update libraries: conda update xxx or to update all libraries: conda update --all
- To deactivate current environment: conda deactivate
- After deactivating, to ever remove an environemnt: conda remove --name xxx --all (for all packages)

#### Lauching each time
- Open Anaconda
- Activate course: conda activate pandas_udemyplayground
- To run jupyter notebook: jupyter notebook (this launches a web browser)
- Role of server? provides an easy to run way quick aproach. Without server we will have to save notebook and run again in cmd prompt). But, should be shut down later.
- Create notebook in udemy (pandas) folder/ open existing notebook from here
- Click New - Python 3
- Shift + Enter to execute cell
- Ctrl + Enter - remains in the same cell
- Last things the cell executes is printed

#### Shutting each down
- Save and checkpoint from floppy disk file icon (also ctrl + s)
- Close tab (doesn't mean we've closed server)/ file - close and halt?
- See all files tab. Green icon means notebook is still running
- Go to runnings tab and 'shutdown' notebook
- Close chrome browser
- Turn server off in cmd prompt window - ctrl c twice
- Close cmd prompt


