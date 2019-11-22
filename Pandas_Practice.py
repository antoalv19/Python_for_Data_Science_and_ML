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
df

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



