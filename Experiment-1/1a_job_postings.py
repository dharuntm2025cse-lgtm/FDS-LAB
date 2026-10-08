import pandas as pd
import matplotlib.pyplot as plt
# Create the dataset
data = {
    'Year': list(range(2010, 2021)),
    'Job Postings': [150, 300, 450, 600, 800, 1200, 1600, 2100, 2700, 3400, 4200]
}
# Create DataFrame
df = pd.DataFrame(data)

# Display the data
print(df)

# Plot the trend
plt.plot(df['Year'], df['Job Postings'], marker='o')
plt.title('Trend of Data Science Job Postings')
plt.xlabel('Year')
plt.ylabel('Number of Job Postings')

plt.show()