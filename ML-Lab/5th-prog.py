# program 5
# pip install scikit-learn seaborn matplotlib

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)

model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("accuracy_score:", accuracy_score(y_test, y_pred))
print("classification_report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

cm = confusion_matrix(y_test, y_pred)
print("confusion_matrix:")
print(cm)

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names,
)
plt.title("Naive Bayes Confusion Matrix")
plt.xlabel("predicted")
plt.ylabel("actual")
plt.show()
