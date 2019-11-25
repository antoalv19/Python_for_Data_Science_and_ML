import numpy as np
import pandas as pd

# Create dataframe
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

# crea dataframe
df = pd.DataFrame(data)

# Now you can use the .groupby() method to group rows together based off of a column name. For instance let's group
# based off of Company. This will create a DataFrameGroupBy object
df.groupby("Company")

# salva oggetto come nuova variabile
by_comp = df.groupby("Company")

# ora si possono chiamare i metodi di calcolo sull'ogetto aggreato
# media
by_comp.mean()

# standard deviation
by_comp.std()

# MIN e MAX - funzionano anche sulle stringhe sortando per ordine alfabetico
by_comp.min()
by_comp.max()

# count
by_comp.count()

# describe and transpose
by_comp.describe()
by_comp.describe().transpose()["GOOG"]




