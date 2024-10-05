import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the updated CSV file
df = pd.read_csv('mall_with_distances.csv')

# Set plot style
sns.set(style="whitegrid")

# Create a scatter plot to visualize the clusters
plt.figure(figsize=(10, 6))

# Plot each cluster with a different color
sns.scatterplot(
    x='AnnualIncome',
    y='SpendingScore',
    hue='ClusterAssigned',
    data=df,
    palette='viridis',  # You can also use 'Set1', 'coolwarm', etc.
    legend='full',
    s=100  # Marker size
)

# Add plot labels and title
plt.title('Customer Segmentation Based on Annual Income and Spending Score', fontsize=15)
plt.xlabel('Annual Income (k$)', fontsize=12)
plt.ylabel('Spending Score (1-100)', fontsize=12)

# Display the plot
plt.show()
