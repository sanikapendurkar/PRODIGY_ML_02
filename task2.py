import pandas as pd
import math

df = pd.read_csv('mall.csv')

Income = df['AnnualIncome']
Spending = df['SpendingScore']

# Calculate distances for cluster 1
def cluster1_distance():
    distances1 = []
    for i in range(len(df)):  # Use len(df) to cover all rows
        distance = math.sqrt((Income[i] - 101)**2 + (Spending[i] - 24)**2)
        distances1.append(distance)
    return distances1

# Calculate distances for cluster 2
def cluster2_distance():
    distances2 = []
    for i in range(len(df)):  # Use len(df)
        distance = math.sqrt((Income[i] - 60)**2 + (Spending[i] - 50)**2)
        distances2.append(distance)
    return distances2

# Calculate distances for cluster 3
def cluster3_distance():
    distances3 = []
    for i in range(len(df)):  # Use len(df)
        distance = math.sqrt((Income[i] - 71)**2 + (Spending[i] - 75)**2)
        distances3.append(distance)
    return distances3

# Add distance columns to the DataFrame
df['distance1'] = cluster1_distance()
df['distance2'] = cluster2_distance()
df['distance3'] = cluster3_distance()

# Assign clusters based on distances
def assign_cluster(distance1, distance2, distance3):
    cluster_assigned = []
    for i in range(len(df)):  # Use len(df) to iterate over all rows
        if distance1[i] < distance2[i] and distance1[i] < distance3[i]:
            cluster_assigned.append(1)
        elif distance2[i] < distance1[i] and distance2[i] < distance3[i]:
            cluster_assigned.append(2)
        else:
            cluster_assigned.append(3)
    return cluster_assigned

# Add the assigned clusters to the DataFrame
df['ClusterAssigned'] = assign_cluster(df['distance1'], df['distance2'], df['distance3'])

# Save the updated DataFrame to a new CSV file
df.to_csv('mall_with_distances.csv', index=False)
