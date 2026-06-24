# ============================================================
# PROGRAM 8 QUESTION
# Develop a program to load the Titanic dataset. Split the data into
# training and test sets. Train a decision tree classifier. Visualize the tree
# structure. Evaluate accuracy, precision, recall, and F1-score.
# ============================================================
# pip install pandas scikit-learn matplotlib
# Place titanic_train.csv in the same directory before running.

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

df = pd.read_csv("titanic_train.csv")
print(df.head(3))

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Age"] = df["Age"].fillna(df["Age"].mean())

X = df[["Age", "Sex", "Pclass"]]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("accuracy:", accuracy_score(y_test, y_pred))
print("f1_score:", f1_score(y_test, y_pred))
print("recall:", recall_score(y_test, y_pred))
print("precision:", precision_score(y_test, y_pred))

plot_tree(model, feature_names=X.columns, filled=True)
plt.title("Decision Tree Classifier")
plt.show()
