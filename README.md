# Journal

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
- s = pandas.Series(x)
- s.(tab??)
- s.values (no brackets needed)
- s.index
- s.dtype

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


