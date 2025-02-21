import pandas as pd

df = pd.read_csv("iris.data", header=None, names=["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width", "Category"])
print(df.shape)
print(df["Sepal Lenght"][df.Category == "Iris-virginica"].head())
print(df[["Sepal Lenght", "Petal Lenght"]][df["Petal Width"] >= 2.0].head())