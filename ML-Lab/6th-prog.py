# ============================================================
# PROGRAM 6 QUESTION
# Implement the non-parametric Locally Weighted Regression algorithm
# in order to fit data points. Select appropriate data set for your experiment
# and draw graphs.
# ============================================================
# pip install pandas numpy matplotlib
# Place BostonHousing.csv in the same directory before running.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("BostonHousing.csv")

X = df["rm"].values
y = df["medv"].values


def locally_weighted_regression(x0, tau=0.5):
    X_bias = np.c_[np.ones(len(X)), X]
    weights = np.exp(-((X - x0) ** 2) / (2 * tau**2))
    W = np.diag(weights)

    theta = np.linalg.pinv(X_bias.T @ W @ X_bias) @ X_bias.T @ W @ y
    return np.array([1, x0]) @ theta


X_test = np.linspace(min(X), max(X), 200)
y_pred = [locally_weighted_regression(x) for x in X_test]

plt.scatter(X, y, label="Data")
plt.plot(X_test, y_pred, "r", label="LWR Curve")
plt.xlabel("RM")
plt.ylabel("MEDV")
plt.title("Locally Weighted Regression")
plt.legend()
plt.show()
