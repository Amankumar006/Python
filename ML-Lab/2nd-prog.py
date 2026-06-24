# ============================================================
# PROGRAM 2 QUESTION
# Develop a program to load a dataset with at least two numerical
# columns (e.g., Iris, Titanic). Plot a scatter plot of two variables and
# calculate their Pearson correlation coefficient. Write a program to compute
# the covariance and correlation matrix for a dataset. Visualize the correlation
# matrix using a heatmap to know which variables have strong positive/negative
# correlations.
# ============================================================
# pip install pandas matplotlib seaborn
# Place titanic_train.csv in the same directory before running.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic_train.csv")
print(df.head(3))

num_df = df[["Age", "Fare", "SibSp", "Parch", "Pclass"]]
num_df = num_df.dropna()

# scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(num_df["Age"], num_df["Fare"])
plt.title("scatter plot of Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

# pearson correlation
corr = num_df["Age"].corr(num_df["Fare"])
print("corr:")
print(corr)

# covariance matrix
cov_matrix = num_df.cov()
print("cov_matrix:")
print(cov_matrix)

# correlation matrix
corr_matrix = num_df.corr()
print("corr_matrix")
print(corr_matrix)

# heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("heatmap")
plt.show()
