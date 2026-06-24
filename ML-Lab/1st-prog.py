# ============================================================
# PROGRAM 1 QUESTION
# Develop a program to load a dataset and select one numerical column.
# Compute mean, median, mode, standard deviation, variance, and range for a
# given numerical column in a dataset. Generate a histogram and boxplot to
# understand the distribution of the data. Identify any outliers in the data
# using IQR. Select a categorical variable from a dataset. Compute the frequency
# of each category and display it as a bar chart or pie chart.
# ============================================================
# pip install pandas matplotlib
# Place student_dataset.csv in the same directory before running.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_dataset.csv")
marks = df["Marks"]

print("mean:", marks.mean())
print("median:", marks.median())
print("mode:", marks.mode())
print("standard_deviation:", marks.std())
print("variance:", marks.var())
print("range:", marks.max() - marks.min())

# histogram
plt.hist(marks, bins=5)
plt.title("histogram of marks")
plt.xlabel("marks")
plt.ylabel("frequency")
plt.show()

# boxplot
plt.boxplot(marks)
plt.title("boxplot of marks")
plt.show()

# outlier detection
Q1 = marks.quantile(0.25)
Q3 = marks.quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = marks[(marks < lower) | (marks > upper)]
print("outliers:")
print(outliers)

# categorical column
gender = df["Gender"]

# frequency count
freq = gender.value_counts()
print("freq:")
print(freq)

print(df.head(3))

# bar chart
freq.plot(kind="bar")
plt.title("bar chart")
plt.xlabel("gender")
plt.ylabel("count")
plt.show()

# pie chart
freq.plot(kind="pie", autopct="%1.1f%%")
plt.title("pie chart")
plt.show()
