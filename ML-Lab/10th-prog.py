# ============================================================
# PROGRAM 10 QUESTION
# Develop a program to implement k-means clustering using Wisconsin
# Breast Cancer data set and visualize the clustering result.
# ============================================================
# pip install scikit-learn matplotlib

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X = data.data

X = StandardScaler().fit_transform(X)
labels = KMeans(n_clusters=2, random_state=42).fit_predict(X)
X_pca = PCA(n_components=2).fit_transform(X)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels)
plt.title("K-Means Clustering")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
