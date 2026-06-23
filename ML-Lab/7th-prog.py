# program 7
# pip install pandas scikit-learn matplotlib
# Place BostonHousing.csv and auto-mpg.csv in the same directory before running.

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures


print("linear regression")
housing_df = pd.read_csv("BostonHousing.csv")

X = housing_df.drop("medv", axis=1)
y = housing_df["medv"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred = linear_model.predict(X_test)

plt.scatter(y_test, y_pred)
plt.title("Linear Regression Model")
plt.xlabel("actual")
plt.ylabel("predicted")
plt.show()

print("r2_score:", r2_score(y_test, y_pred))
print("mean_squared_error:", mean_squared_error(y_test, y_pred))


print("\npolynomial regression")
auto_df = pd.read_csv("auto-mpg.csv")

auto_df["horsepower"] = pd.to_numeric(auto_df["horsepower"], errors="coerce")
auto_df.dropna(inplace=True)

if "car name" in auto_df.columns:
    auto_df.drop("car name", axis=1, inplace=True)

X = auto_df.drop("mpg", axis=1)
y = auto_df["mpg"]

X_encoded = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.2,
    random_state=42,
)

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

polynomial_model = LinearRegression()
polynomial_model.fit(X_train_poly, y_train)
y_pred = polynomial_model.predict(X_test_poly)

plt.scatter(y_test, y_pred)
plt.title("Polynomial Regression")
plt.xlabel("actual")
plt.ylabel("predicted")
plt.show()

print("r2_score:", r2_score(y_test, y_pred))
print("mean_squared_error:", mean_squared_error(y_test, y_pred))
