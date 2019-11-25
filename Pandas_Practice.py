import numpy as np
import pandas as pd
from numpy.random import randn

# Creating a pandas series - You can convert a list,numpy array, or dictionary to a Series:
labels = ["a", "b", "c"]
my_list = [10, 20, 30]
arr = np.array(my_list)
d = {"a": 10, "b": 20, "c": 30}

# Using Lists
pd.Series(data=my_list)

# Using lists with an Index
pd.Series(data=my_list, index=labels)

# Numpy Arrays
pd.Series(arr)
pd.Series(arr, labels)

# Dictionary
pd.Series(d)

# Using an Index The key to using a Series is understanding its index. Pandas makes use of these index names or
# numbers by allowing for fast look ups of information (works like a hash table or dictionary).
ser1 = pd.Series([1, 2, 3, 4], index=["USA", "Germany", "USSR", "Japan"])
ser2 = pd.Series([1, 2, 5, 4], index=["USA", "Germany", "Italy", "Japan"])

# Operations are then also done based off of index:
operation = ser1 + ser2
# print(operation)

# Set pandas dataframe environment
np.random.seed(101)
df = pd.DataFrame(np.random.rand(5, 4), index=["A", "B", "C", "D", "E"], columns=["W", "X", "Y", "Z"])

# Selection and Indexing
df["W"]

# Pass a list of column names
df[["W", "Y"]]

# SQL syntax
df.W

# DF columns are series
type(df["W"])

# Creating a new column
df["New"] = df["W"] + df["Y"]

# Removing columns - Specify Inplace = True
df.drop("New", axis=1, inplace=True)

# Drop rows specifying index = 0
# df.drop("E", axis=0, inplace=True)

# Selecting Rows
df.loc["A"]

# Or select based off of position instead of label
df.iloc[2]

# Selecting subset of rows and columns
df.loc["B", "Y"]

df.loc[["A", "B"], ["W", "Y"]]

# Conditional Selection
df > 0

df[df > 0]

df[df["W"] > 0]

df[df["W"] > 0]["Y"]

df[df["W"] > 0][["Y", "X"]]

# For two conditions you can use | - OR and & - AND with parenthesis
# df[(df["W"] > 0) & (df[df["Y"] > 0])]

# More Index Details
# Let's discuss some more features of indexing, including resetting the index or setting it something else.
# Reset index to default
df.reset_index()

# New Index
newind = "CA NY WY OR CO".split()

# New column
df["States"] = newind

# Set new  index
df.set_index("States", inplace=True)

# Multi-Index and Index Hierarchy
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

# New dataframe

df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])

# Give name to indexes
df.index.names = ["Group", "Num"]

# Select using XS - da indice esterno a indice interno
df.xs(["G1", 1])

# Select using XS - da indice interno a esterno
df.xs(1, level="Num")
