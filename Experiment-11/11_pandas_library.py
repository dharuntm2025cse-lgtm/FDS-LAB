import numpy as np
import pandas as pd

# Create a list
list1 = [[1, 'Smith', 50000],
         [2, 'Jones', 60000]]

# Create DataFrame
df = pd.DataFrame(list1)

# Assign column names
df.columns = ['Empd', 'Name', 'Salary']

# Display DataFrame
print("EMPLOYEE DATAFRAME")
print(df)

# Display information
print("\nDATAFRAME INFORMATION")
df.info()

# Read 50 Startups dataset
df = pd.read_csv('50_Startups.csv')

# Display information of 50 Startups dataset
print("\n50 STARTUPS DATASET INFORMATION")
df.info()

# Display the complete dataset
print("\n50 STARTUPS DATASET")
print(df)

# Display first five rows
print("\nFIRST FIVE ROWS")
print(df.head())

# Display last five rows
print("\nLAST FIVE ROWS")
print(df.tail())