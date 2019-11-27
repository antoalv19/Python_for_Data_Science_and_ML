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
# SOLUTION: sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"]
jobt_joseph = sal["JobTitle"][sal["EmployeeName"] == "JOSEPH DRISCOLL"]

# How much does JOSEPH DRISCOLL make (including benefits)?
# SOLUTION: sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits]
tot_pay_jd = sal["TotalPayBenefits"][sal["EmployeeName"] == "JOSEPH DRISCOLL"]

# What is the name of highest paid person (including benefits)?
# ADV SOLUTION: sal.loc[sal["TotalPayBenefits"].idxmax()]
# .idxmax() restituisce il numero di indice
# .iloc() restituisce il dato presente a quell'indice
max_pay = sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()]["EmployeeName"]

# What is the name of lowest paid person (including benefits)?
# Do you notice something strange about how much he or she is paid? -> Amount is negative
# ADV SOLUTION: sal.loc[sal["TotalPayBenefits"].idxmin()]
min_pay = sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min()][["EmployeeName", "TotalPayBenefits"]]

# What was the average (mean) BasePay of all employees per year? (2011-2014)?
# mean_base_pay = sal[(2011 < sal["Year"]) & (sal["Year"] < 2014)]["BasePay"].mean()
mean_base_pay = sal[(2011 <= sal["Year"]) & (sal["Year"] <= 2014)].groupby("Year").mean()
mean_base_pay["BasePay"]

# How many unique job titles are there? - 2159
sal["JobTitle"].nunique()

# What are the top 5 most common jobs?
top_5_jobs = sal["JobTitle"].value_counts().head()

# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
# job_2013 = sal["JobTitle"][(sal["Year"] == 2013)].nunique()
job_2013 = sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)  # pretty tricky way to do this...

# How many people have the word Chief in their job title?
chief = sum(sal["JobTitle"][(sal["JobTitle"].str.contains("Chief") == True)].value_counts())

# Is there a correlation between length of the Job Title string and Salary?
# crea colonna title_len con lunghezza job title
sal["title_len"] = sal["JobTitle"].apply(len)

# controlla correlazione
corr_len = sal[["title_len", "TotalPayBenefits"]].corr()
