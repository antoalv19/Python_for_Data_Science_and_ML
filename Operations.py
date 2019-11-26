import pandas as pd
import numpy as np

# create DataFrame
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
df.head()

# Extract array of Unique Values - .unique()
df["col2"].unique()

# Count how many unique values are present - .nunique()
df["col2"].nunique()

# Get array of values and frequency
df["col2"].value_counts()

# Selecting data using criteria from multiple columns
newdf = df[(df["col1"] > 2) & (df["col2"] == 444)]


# Applying Functions to each column entry using .apply()
def times2(x):
    return x * 2


# apply times 2 function
df["col1"].apply(times2)

# get length of each item
df["col3"].apply(len)

# Sum the entries of column 1
df["col1"].sum()

# PERMANENTLY remove a column
del df["col1"]

# Get column and index names
df.columns

# get index info, start, stop and step size
df.index

# Sorting and ordering a dataframe
df.sort_values(by="col2")  # inplace=False by default

# find and check for null values
df.isnull()

# drop rows with NaN values
df.dropna()

# fill NaN values with something else
df.fillna("Value")

########## PIVOT TABLE ###########
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)

print(df.pivot_table(values="D", index=["A", "B"], columns="C").fillna("0"))
