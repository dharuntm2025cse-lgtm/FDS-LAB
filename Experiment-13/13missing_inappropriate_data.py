import numpy as np
import pandas as pd

df = pd.read_csv("Hotel_Dataset.csv")

print(df.duplicated())

df['Hotel'] = df['Hotel'].replace(['Ibys'], 'Ibis')
df['FoodPreference'] = df['FoodPreference'].replace(['Vegetarian', 'veg'], 'Veg')
df['FoodPreference'] = df['FoodPreference'].replace(['non-Veg'], 'Non-Veg')

df['Bill'] = pd.to_numeric(df['Bill'], errors='coerce')

df.drop_duplicates(inplace=True)
df.drop(['Age_Group.1'], axis=1, inplace=True)

df.loc[df.CustomerID < 0, 'CustomerID'] = np.nan
df.loc[df.Bill < 0, 'Bill'] = np.nan
df.loc[df.EstimatedSalary < 0, 'EstimatedSalary'] = np.nan
df.loc[(df.NoOfPax < 1) | (df.NoOfPax > 20), 'NoOfPax'] = np.nan
df.loc[(df['Rating(1-5)'] < 1) | (df['Rating(1-5)'] > 5), 'Rating(1-5)'] = np.nan

df['EstimatedSalary'] = df['EstimatedSalary'].fillna(round(df['EstimatedSalary'].mean()))
df['Bill'] = df['Bill'].fillna(round(df['Bill'].mean()))
df['NoOfPax'] = df['NoOfPax'].fillna(round(df['NoOfPax'].median()))
df['Rating(1-5)'] = df['Rating(1-5)'].fillna(round(df['Rating(1-5)'].median()))

print("\nFinal Cleaned Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())
