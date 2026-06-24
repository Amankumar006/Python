# ============================================================
# PROGRAM 9 QUESTION
# Develop a program to implement the Naive Bayesian classifier
# considering Iris dataset for training. Compute the accuracy of the classifier,
# considering the test data.
# ============================================================
# pip install scikit-learn

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("accuracy:", accuracy_score(y_test, y_pred))
