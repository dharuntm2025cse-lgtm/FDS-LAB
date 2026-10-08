import matplotlib.pyplot as plt
# Sample data
roles = ['Data Analyst', 'Data Engineer', 'Data Scientist','ML Engineer', 'Business Analyst']
counts = [300, 500, 450, 200, 150]
# Plot the distribution
plt.bar(roles, counts)
plt.title('Distribution of Data Science Roles')
plt.xlabel('Role')
plt.ylabel('Count')
plt.show()