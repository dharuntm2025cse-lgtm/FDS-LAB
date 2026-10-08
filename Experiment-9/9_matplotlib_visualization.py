import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = pd.read_csv('Iris_Dataset.csv')

# Display the dataset
print(data)

# Display information about the dataset
data.info()

# Display statistical summary
print(data.describe())

# Count each variety
print(data.value_counts('variety'))

# Count plot
sns.countplot(x='variety', data=data)
plt.show()

# Scatter plot - Sepal
sns.scatterplot(x='SepalLengthCm',
                y='SepalWidthCm',
                hue='variety',
                data=data)
plt.show()

# Scatter plot - Petal
sns.scatterplot(x='PetalLengthCm',
                y='PetalWidthCm',
                hue='variety',
                data=data)
plt.show()

# Pair plot
sns.pairplot(data, hue='variety')
plt.show()
# Histogram - Petal Length
sns.FacetGrid(data, hue='variety', height=5).map(
    sns.histplot, 'PetalLengthCm'
).add_legend()
plt.show()

# Histogram - Petal Width
sns.FacetGrid(data, hue='variety', height=5).map(
    sns.histplot, 'PetalWidthCm'
).add_legend()
plt.show()

# Histogram - Sepal Length
sns.FacetGrid(data, hue='variety', height=5).map(
    sns.histplot, 'SepalLengthCm'
).add_legend()
plt.show()

# Histogram - Sepal Width
sns.FacetGrid(data, hue='variety', height=5).map(
    sns.histplot, 'SepalWidthCm'
).add_legend()
plt.show()