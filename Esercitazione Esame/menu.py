import pandas as pd
import numpy as np


class Ordine:
    def __init__(self, menu, ordine):
        self.menu_df = pd.read_csv(menu)
        self.ordine_df = pd.read_csv(ordine)

    def costo_tot(self):
        costo = 0.0
        for index, row in self.ordine_df.iterrows():
            id_prodotto = row["id_prodotto_ordinato"]
            costo_corrente = self.menu_df[self.menu_df["id_prodotto"] == id_prodotto].costo.values[0]
            iva = (self.menu_df[self.menu_df["id_prodotto"] == id_prodotto].iva.values[0]) / 100
            costo_ivato = costo_corrente * (1 + iva)
            costo += costo_ivato * row["quantità"]
        print(costo)

    def ricevuta(self):
        ricevuta_df = pd.DataFrame(columns=["descrizione", "quantità", "costo unitario", "iva", "totale"])
        for index, row in self.ordine_df.iterrows():
            costo_corrente = self.menu_df[self.menu_df["id_prodotto"] == row["id_prodotto_ordinato"]].costo.values[0]
            iva = self.menu_df[self.menu_df["id_prodotto"] == row["id_prodotto_ordinato"]].iva.values[0] / 100
            costo_ivato = costo_corrente * (1 + iva)
            costo_totale_prodotto = costo_ivato * row["quantità"]
            descrizione = self.menu_df[self.menu_df["id_prodotto"] == row["id_prodotto_ordinato"]].descrizione.values[0]
            ricevuta_df = pd.concat(
                [ricevuta_df, pd.DataFrame([[descrizione, row["quantità"], costo_corrente, iva, costo_totale_prodotto]],
                                           columns=['descrizione', 'quantità', 'costo unitario', 'iva', 'totale'])])
        print(ricevuta_df)

    def custom_func(self):
        # a = self.ordine_df.id_prodotto_ordinato.to_numpy()
        # b = self.ordine_df["quantità"].to_numpy()
        # id = np.identity(n=a.size)
        # a_diag = a*id
        # b_diag = b*id
        # g1 = np.random.normal(size=a_diag.shape, scale=1.0, loc=1.0)
        # g2 = np.random.normal(size=b_diag.shape, scale=1.0, loc=1.0)
        # a_g1 = a_diag@g1
        # b_g2 = b_diag@g2
        # print(a_g1@b_g2.T)
        array1 = self.ordine_df["id_prodotto_ordinato"].to_numpy()
        array2 = self.ordine_df["quantità"].to_numpy()
        mat1 = array1 * np.identity(array1.shape[0])
        mat2 = array2 * np.identity(array2.shape[0])
        mat1 = mat1 @ np.random.normal(size=(mat1.shape[1], 30), loc=1.0, scale=1.0)
        mat2 = mat2 @ np.random.normal(size=(mat2.shape[1], 30), loc=1.0, scale=1.0)
        return mat1 @ mat2.T


ord = Ordine("menu.csv", "ordine.csv")
ord.costo_tot()
ord.ricevuta()
print(ord.custom_func())
array1 = np.array([[0, 1, 2, 3, 4], [1, 2, 3, 4, 5]])
print(array1.shape)
