import matplotlib
import pandas as pd
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data',
                 names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Category"],
                 header=None)
print(df.head())
print(df.index)
print(df.columns)
print(df.shape)
sepal_col = df["Sepal Length"]
print(sepal_col.head())

multiple_col = df[["Petal Length", "Petal Width"]]
print(multiple_col.head())

first_row = df.loc[0]
# in questo caso equivale alla funzione iloc[0]
# perché la posizione e l'index (generato automaticamente) sono uguali
# l'unica differenza è che l'iloc permette di fare slicing
print(first_row)
print(df.Category)
# posso accedere direttamente ai campi a patto che i nomi siano conformi alla nomenclatura di Py,
# per esempio niente spazi

