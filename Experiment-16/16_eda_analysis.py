import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

print("First 5 rows:")
print(tips.head())

# Distribution plots
sns.displot(tips.total_bill, kde=True)
plt.show()

sns.displot(tips.total_bill, kde=False)
plt.show()

# Joint plots
sns.jointplot(x=tips.tip, y=tips.total_bill)
plt.show()

sns.jointplot(x=tips.tip, y=tips.total_bill, kind="reg")
plt.show()

sns.jointplot(x=tips.tip, y=tips.total_bill, kind="hex")
plt.show()

# Pair plots
sns.pairplot(tips)
plt.show()

print("\nTime Value Counts:")
print(tips.time.value_counts())

sns.pairplot(tips, hue='time')
plt.show()

sns.pairplot(tips, hue='day')
plt.show()

# Correlation
sns.heatmap(tips.corr(numeric_only=True), annot=True)
plt.show()

# Box plots
sns.boxplot(x=tips.total_bill)
plt.show()

sns.boxplot(x=tips.tip)
plt.show()

# Count plots
sns.countplot(x=tips.day)
plt.show()

sns.countplot(x=tips.sex)
plt.show()

# Pie chart
tips.sex.value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()

# Bar chart
tips.sex.value_counts().plot(kind='bar')
plt.show()

# Dinner day analysis
sns.countplot(x=tips[tips.time == 'Dinner']['day'])
plt.show()