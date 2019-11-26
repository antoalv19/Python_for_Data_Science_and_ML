import pandas as pd
import numpy as np

###### CONSTANTS ######
SALARIES_CSV = r"C:\Users\antonio.alvino\Desktop\Data Science\Py-DS-ML-Bootcamp-master\Refactored_Py_DS_ML_Bootcamp" \
               r"-master\04-Pandas-Exercises\Salaries.csv "

# Read Salaries.csv as a dataframe called sal.
sal = pd.read_csv(SALARIES_CSV)

# Check the head of the dataframe
sal.head()

# Check dataframe info (column, value count, data type)
# sal.info()

# What is the average Base Pay?
sal["BasePay"].mean()

# What is the highest amount of OvertimePay in the dataset ?
sal["OvertimePay"].max()

# What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't
# match up (there is also a lowercase Joseph Driscoll).

jobt_joseph = sal["JobTitle"][sal["EmployeeName"] == "JOSEPH DRISCOLL"]

# How much does JOSEPH DRISCOLL make (including benefits)?



