# Journal
---

`10-05-2020`
### Data Analysis with Python and Pandas
#### set_index and reset_index methods
- bond = pd.read_csv("jamesbond.csv")
  bond.set_index(keys = "Films". implace = True) ~ index in bold/ replacs presious index dataframe
  Bond.reset_index(drop = False) ~ to reset 
- bond.reset_index(inplace = True)
  bond.set_index("Year", inplace = True) ~ these 2 store in reset 

#### Retrieve rows by index label with .loc[] accessor
- Get in the habbit of sorting, easier for pandas 
- bond = pd.read_csv("jamesbond.csv", index_col = "Film")
  bond.sort_index(inplace = True)
  bond.loc["Goldfinger"] ~ copies values in series
  bond.loc["a":"b":2] ~ copies values in between
-  Gives error if not in list, can check with "a" in bond.index (Gives False/True)

#### Retrieve rows by index label with iloc[] accessor
- bond.iloc[15, 20 ]

#### Second arguments to loc and iloc accesors
- bond.loc["Moonraker", "Actor"] ~ gives actor
- bond.loc["Moonraker"["Director", "Actor"]] ~ gives dataframe of director & Actor
- bond.iloc[14, 2:5]

#### Set new value for specific cell or cells in a row
- bond.loc["Dr.No", "Actor"] = "xxx" ~ changes actor name in row 
- bond.loc["Dr.No", ["a", "b","c"]] = ["x","y","z"]
- Integers are changed to floating point numbers

#### Set multiple values in dataframe
- Introduce boolean series to filter
- Act = bond["Actor"] == "Sean Connery"
  bond.loc[act, "Actor"] = "a" ~ not a copy a subset (.loc references rows)
  bond

#### Rename index labels or columns
- bond.rename(mapper = {"Goldeneye": "Golden Eye"}, axis = 0/"rows"/"index")
- bond.rename(index = {"Goldeneye": "Golden Eye"})
- Same works for columns 
- bond.columns = ["a","b"]
  bond

#### Delete rows or columns from dataframe
- bond.drop(["a","b"], inplace = True) ~ in rows
- bond.drop(labels = ["Box office", "b"], axis = "Columns") ~ in columns
- act = bond.pop("Actor") ~ removed permanantly
- del bond["Director"]

#### Create random sample
- bond.sample() ~ returns a single random row
- bond.sample(n = 5)
- bond.sample(frac = 0.25, axis ="index")

#### .nsmallest() and nlargest() method
- bond.nlargest(3, columns = "box office")
- bond.nlargest(n = 2, columns = "box office")
- bond["box office"].nlargest(8)

#### .where method
- bond.where(mask) ~ others null
- bond.where(bond[:box office]> 800)

#### .query method
- Doesn't work with spaces in columns
- [column_name.replace(" ","_") for column_name in bond.columns]
- bond.query('Actor == "Sean Connery"')
- != et and in etc are valid

#### .apply() method on single columns
- def convert(number):
      return str(number) + "millions"

  bond["Box Office"] = bond["Box Office"].apply(convert)
- columns = ["Box Office", "Budget"]
  for col in columns:
      bond[col] = bond[col].apply(convert)

#### .apply() method on rows
- def good_movie(row):
      actor = row[1]
      budget = row[4]

      if actor == "a"
         return "b"
      elif actor =="c" and budget > 40:
         return "d"
      else:
         return "e"
  bond.apply(good_movie, axis ="columns")

#### .copy method
- makes copy but saves it differently in memory
- bond["Directory"].copy()

#### Working with broken text data
- white spaces, multiple values etc.
- check .nuniques, make categories for lesser values by .astype 

#### Common string methods .lower(), .upper, .title, .len()
- chicago["Name"].str.lower()

#### .str.replace() method
- "xxx" replace("x", "!")
- chicago["Department"] = chicago["Deprtment"].str.replace("MGMNT","Management")
- chicago["Salary"].str.replaced("$", "").astype(float)

#### Filtering with string method
- .dropna(how = "all")
- chicago["a"].str.lower().str.contains("water")
- chicago["a"].str.lower().str.startswith("water")
- chicago["a"].str.lower().str.endswith("ist")

#### .strip(), .lstrip(), rstrip()
- removes spaces
- chicago["Name"].str.rstrip().str.lstrip()

#### String methods on Index and columns
- index_col = "Name"
- chicago.index = chicago.index.str.strip().str.title()
- chicago.columns = chicago.columns.str.upper()

#### .str.split() method
- chicago["Name"].str.split(",").str.get(0).str.title().value_counts() ~ gives list
- .get() gives back the first one before the comma in the list 
- can join many methods 
- expand and n parameters of .str.split() method
- chicago[["First Name", "Last Name"]] = chicago["Name"].str.split(",", expand = True)
- chicago["Name"].str.split(",", expand = True, n = 1)
 
---

`08-05-2020`
### Data Analysis with Python and Pandas
#### Filtering Data - Module's dataset and Memory optimization
`df = pd.read_csv("employees.csv, parse_dates = ["Start Date", "Last Login Time"])
df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")`

- Date type imported as strings, problem when we want to do date time operations. Should tell pandas that we have a date time to do date time operations.
- df["Start Date"] = pd.to_datetime(df["Start Date"]) ~ 1993-08-06
- df["Last Login Time"] = pd.to_datetime(["Last Login Time"]) ~ 2020-04-23 12:42:00
- df["Senior Management"] = df["Senior Management"].astype("bool") ~ to store boolean values
- Big data and small catagories of values, we can store catagorical instead of string values ~ to reduce size of files
- df["Gender"] = df["Gender"].astype("caregory") ~ reduces size

#### Filtering based on a condition
- df["Gender"] == "Male" ~ gives series of boolean
- df[df["Gender"] == "Male"] ~ gives new dataframe with Male
- df[df["Salary"] > 1100000]
- df[df["Start Date"] >= "1985-01-01"]

#### Filtering based on more than one operator
- mask1 = df["Gender"] == "Male" ~ AND
  mask2 = df["Team"] == "Marketing"
  df[mask1 & mask2] 

- mask1 = df["Senior Management"] ~ OR
  mask2 = df["Start Date"] < "1990-01-01"
  df[mask1 | mask2]   

- df[mask1 & mask2 | mask3] ~ evaluated left to right

#### .isin method
- mask = df["Team"].isin(["Legal", "Sales", "Product"]) 
  df[mask]
-For a lot of OR needs, multiple values for single series

#### .isnull() and .notnull
- Boolean series to filter later
- mask = df["Team"].sinull()
  df[mask] 

#### .between() method
- df[df["Salary"].between(60000,70000)]
- df[df["Last Login Time"].between("0.8:30AM", "12:00PM")]

#### .duplicated() method
- df.sort_values("First Name", inplace = True)
- df[df["First Name"].duplicated(keep = False)]  
- ~df[df["First Name"].duplicated(keep = False)] ~ only reperesented once

#### .drop_duplicates() method
- df.sort_values("First Name", inplace = True)
- len(df)
- df.drop_duplicates() ~ removes rows when all values are identical
- df.drop_duplicates(subset = ["First Name"], Keep = "first") ~ keeps first 
- df.drop_duplicates(subset = ["First Name"], Keep = False) ~ removes all duplicates
- df.drop_duplicates(subset = ["First Name", "Teams"])

#### .unique() and .nunique() methods
- df["Gender"].unique() ~array with the unique values
- len(df["Gender"].unique())
- df["Gender"].nunique() ~ gives number of unique values excluding null values
- df["Gender"].nunique(dropna = False)

---

`07-05-2020`
### Data Analysis with Python and Pandas

#### What is inplace()?

#### Broadcasting operations
- Like .apply(), to apply commands on the values of series not the whole series
- X.["a"].add(5) or X.["a"] + 5
- Will work with null values
- Same for all math operators
- X.["a"].mul(5) or X.["aa"] = X.["a"] * 5

#### Review .value_counts() method
- X["a"].value_counts(): frequency of a

#### Drop rows and null values
- Deal with NaN values
- X.dropna() ~ removes rows with any NaN values
- X.dropna(how = "all") ~ removes rows with all NaN values
- X.dropna(how = "all", inplace = "True")
- X.dropna(axis = 1) or X.dropna(axis = "columns") ~ removes columns with NaN
- X.dropna(subset = ["a", "b"]) ~ removes specific rows with NaN

#### .fillna() method
- X.fillna() ~ replace every NaN value
- Works better with similar data types
- X["X"].fillna(0, inplace = True) ~ replaces NaN at specific data type
- inplace() is important

#### .astype() method
- convert data types into each other
- Important to not have NaN values
- nba = pd.read_csv("nba.csv").dropna(how = "all")
  nba["Salary"].fillna(0, inplace = True)
  nba["College"].fillna("None"), inplace = True)
  nba.head(6)
  nba.dtypes (or nba.info() which is better)
  nba["Salary"] = nba["Salary"].astype("int")
  nba["Number"].astype("int")

~ Catagory (unique to pandas) ~ for duplicate values to decrease load
  nba["Position"].nunique().astype("category") ~ saves memory

#### .sort_values() method for dataframes
  - X.sort_values("a", ascending =True) ~ sorts value by a
  - X.sort_values("a", ascending =True, inplace = True) ~ overwrites the original dataframe
  - Puts NaN in the end
  - nba.sort_values("Salary", naposition = "first") ~ puts NaN first
  - nba.sort_values(["Team", "Name"]) ~ sorts for 2 columns
  - nba.sort_values(["Team", "Name"], ascending =[True, False], inplace = True) ~ ascention of columns to sort
  
#### .sort_index() method
- nba.sort_index(ascending = True) ~ sorting by index

#### .rank() method
- nba = pd.read_csv("nba.csv").dropna(how ="all")
- nba["Salary"] = nba["Salary"].fillna(0).astype("int")
- nba["Salary Rank"] = nba["Salary"].rank(ascending = True).astype("int") ~ gives a rank for the Salary values
- nba.sort_values(by = "Salary", ascending = False) ~ same as rank

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


