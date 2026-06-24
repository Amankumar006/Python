# ============================================================
# PROGRAM 4 QUESTION
# Develop a program to load the Iris dataset. Implement the
# k-Nearest Neighbors (k-NN) algorithm for classifying flowers based on their
# features. Split the dataset into training and testing sets and evaluate the
# model using metrics like accuracy and F1-score. Test it for different values
# of k (e.g., k=1,3,5) and evaluate the accuracy. Extend the k-NN algorithm to
# assign weights based on the distance of neighbors. Compare the performance of
# weighted k-NN and regular k-NN on a synthetic or real-world dataset.
# ============================================================
# pip install scikit-learn

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

X, y = load_iris(return_X_y=True)
X = StandardScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)

for k in [1, 3, 5]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)

    print(f"\nregular knn: k={k}")
    print("accuracy_score:", accuracy_score(y_test, pred))
    print("f1_score:", f1_score(y_test, pred, average="macro"))

    weighted_knn = KNeighborsClassifier(n_neighbors=k, weights="distance")
    weighted_knn.fit(X_train, y_train)
    pred_weighted = weighted_knn.predict(X_test)

    print(f"weighted knn: k={k}")
    print("accuracy_score:", accuracy_score(y_test, pred_weighted))
    print("f1_score:", f1_score(y_test, pred_weighted, average="macro"))
