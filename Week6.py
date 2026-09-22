import pandas as pd
from sklearn.datasets import load_iris


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)


print("First 5 rows of dataset:")
print(df.head())


print("\nMean values:")
print(df.mean())

print("\nMedian values:")
print(df.median())

print("\nMode values:")
print(df.mode().iloc[0])

print("\nRange values:")
print(df.max() - df.min())

print("\nVariance values:")
print(df.var())

print("\nStandard Deviation values:")
print(df.std())

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

print("\nInterquartile Range (IQR):")
print(IQR)