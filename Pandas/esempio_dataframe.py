import pandas as pd

data = {
    "Jobs": pd.Series(["Engineer", "Doctor"], index=["first", "second"]),
    "Cities": pd.Series(["Rome", "Paris"], index=["second", "third"])
}

df = pd.DataFrame(data)
print("Shape of df: ", df.shape)
print("Columns of df: ", df.columns)
print("Index of df: ", df.index)
print("df: \n", df)

# possiamo creare dataframe anche senza creare direttamente le series
# ma le colonne devono avere lo stesso numero di elementi

data = {
    "Colonna1": [3, 34, 4, 2, 2],
    "Colonna2": [3, 37, 8, 1, 5]
}

df = pd.DataFrame(data)
print("Shape of df: ", df.shape)
print("Columns of df: ", df.columns)
print("Index of df: ", df.index)
print("df: \n", df)