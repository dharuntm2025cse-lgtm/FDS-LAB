import pandas as pd
df = pd.read_csv("Data - Data.csv")
print("Original Data:")
print(df)
print("\nDataset Information:")
df.info()

# Handle missing values
df['Country'] = df['Country'].fillna(df['Country'].mode()[0])
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(round(df['Salary'].mean()))

# Convert categorical data
updated_dataset = pd.concat(
    [pd.get_dummies(df['Country']), df.iloc[:, [1, 2, 3]]],
    axis=1
)
updated_dataset['Purchased'] = updated_dataset['Purchased'].replace(
    ['No', 'Yes'], [0, 1]
)

print("\nPreprocessed Data:")
print(updated_dataset)