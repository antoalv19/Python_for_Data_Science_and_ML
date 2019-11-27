import numpy as np
import pandas as pd

# Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom.
ecom = pd.read_csv(r"C:\Users\antonio.alvino\Desktop\Data "
                   r"Science\Py-DS-ML-Bootcamp-master\Refactored_Py_DS_ML_Bootcamp-master\04-Pandas-Exercises"
                   r"\Ecommerce Purchases.csv")

# Check the head of the DataFrame.
ecom.head()

# How many rows and columns are there?
# ecom.info()

# What is the average Purchase Price?
ecom["Purchase Price"].mean()

# What were the highest and lowest purchase prices?
ecom["Purchase Price"].min()
ecom["Purchase Price"].max()

# How many people have English 'en' as their Language of choice on the website?
# SOLUTION: ecom[ecom["Language"] == "en"].count()
ecom[ecom["Language"] == "en"]["Language"].value_counts()

# How many people have the job title of "Lawyer" ?
ecom[ecom["Job"] == "Lawyer"]["Job"].value_counts()

# How many people made the purchase during the AM and how many people made the purchase during PM ?
ecom["AM or PM"].value_counts()

# What are the 5 most common Job Titles?
ecom["Job"].value_counts().head(5)

# Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
ecom[ecom["Lot"] == "90 WT"]["Purchase Price"]

# What is the email of the person with the following Credit Card Number: 4926535242672853
ecom[ecom["Credit Card"] == 4926535242672853]["Email"]

# How many people have American Express as their Credit Card Provider and made a purchase above $95
# SOLUTION: ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()
ecom[(ecom["CC Provider"] == "American Express") & (ecom["Purchase Price"] > 95)]["CC Provider"].value_counts()

# Hard: How many people have a credit card that expires in 2025?
# SOLUTION: sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')
sum(ecom[ecom["CC Exp Date"].astype(str).str[3:5] == "25"]["CC Exp Date"].value_counts())

# Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
# SOLUTION: ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)
ecom["Email"].str.split("@", n=1, expand=True)[1].value_counts().head()
