import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load the dataset
df = pd.read_csv('data/cleveland_heart_disease', header=None)
df.info()
# Assign column-names(headers)
df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 
              'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# Handle missing values or non-numeric data, if any
df = df.replace('?', np.nan) # Replace '?' with NaN

# Convert columns to numeric (if not already)
df = df.apply(pd.to_numeric, errors='coerce')

# Replace missing values with the median of each column
df.fillna(df.median(), inplace=True)

# Basic statistics
print(df.describe())

# Correlation matrix
correlation_matrix = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Heart Disease Features')
plt.show()

# Prepare data for clustering
X = df.drop(['target', 'age', 'sex'], axis=1)  # We'll cluster based on features, not the target

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine optimal number of clusters using the elbow method
inertias = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(k_range, inertias, 'bx-')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('The Elbow Method showing the optimal k')
plt.show()

# Perform K-means clustering
optimal_k = 4  # This should be determined from the elbow plot
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)

# Add cluster labels to the original dataframe
df['Cluster'] = cluster_labels

# Visualize clusters using PCA for dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=cluster_labels, cmap='viridis')
plt.title('Clusters of Heart Disease Patients')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.colorbar(scatter)
plt.show()

# Analyze clusters
for i in range(optimal_k):
    cluster_data = df[df['Cluster'] == i]
    print(f"\nCluster {i} Statistics:")
    print(cluster_data.describe())
    
    plt.figure(figsize=(12, 6))
    cluster_data.drop(['Cluster', 'target'], axis=1).mean().plot(kind='bar')
    plt.title(f'Average Feature Values for Cluster {i}')
    plt.ylabel('Scaled Average Value')
    plt.show()

# Analyze the relationship between clusters and the target variable
cluster_target_cross = pd.crosstab(df['Cluster'], df['target'])
print("\nCluster vs Target Variable:")
print(cluster_target_cross)

plt.figure(figsize=(10, 6))
cluster_target_cross.div(cluster_target_cross.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Proportion of Heart Disease Cases in Each Cluster')
plt.xlabel('Cluster')
plt.ylabel('Proportion')
plt.legend(title='Heart Disease', loc='upper right')
plt.show()