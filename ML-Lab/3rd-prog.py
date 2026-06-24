# ============================================================
# PROGRAM 3 QUESTION
# Develop a program to implement Principal Component Analysis (PCA)
# for reducing the dimensionality of the Iris dataset from 4 features to 2.
# ============================================================
# pip install scikit-learn matplotlib

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data
y = iris.target

X_scaled = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=2).fit_transform(X_scaled)

print("original shape:", X.shape)
print("reduced shape:", X_pca.shape)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="viridis")
plt.title("PCA for Iris Dataset")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.colorbar(label="class")
plt.show()
