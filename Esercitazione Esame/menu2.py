import pandas as pd
import numpy as np


class Ordine:
    def __init__(self, menu, ordine):
        self.menu_df = pd.read_csv(menu)
        self.ordine_df = pd.read_csv(ordine)

    def costo_ordine(self):
        costo_tot = 0.0
        for index, rows in self.ordine_df.iterrows():
            id_prodotto = rows["id_prodotto_ordinato"]
            costo_corrente = self.menu_df[self.menu_df["id_prodotto"] == id_prodotto].costo.values[0]
            iva = (self.menu_df[self.menu_df["id_prodotto"] == id_prodotto].iva.values[0])/100
            costo_ivato = costo_corrente + costo_corrente * iva
            costo_tot += costo_ivato * rows["quantità"]
        print(costo_tot)

    def ricevuta(self):
        for index, rows in self.ordine_df.iterrows():
            id_prodotto = rows["id_prodotto_ordinato"]
            costo_corrente = self.menu_df[self.menu_df["id_prodotto"] == id_prodotto].costo.values[0]
            iva = (self.menu_df[self.menu_df["id_prodotto"] == id_prodotto].iva.values[0])/100
            costo_ivato = costo_corrente + costo_corrente * iva
            costo_totale_prodotto = costo_ivato * rows["quantità"]
            descrizione = self.menu_df[self.menu_df["id_prodotto"] == id_prodotto].descrzione.values[0]
            print("Descrizione: ", descrizione, ", quantità: ", rows["quantità"],
                  ", costo ivato: ", costo_ivato, ", iva: ", iva, ", costo totale: ", costo_totale_prodotto)

    def custom_func(self):
        print(self.ordine_df)
        array1 = self.ordine_df["id_prodotto_ordinato"].to_numpy()
        array2 = self.ordine_df["quantità"].to_numpy()
        mat1 = array1*np.identity(array1.shape[0])
        mat2 = array2*np.identity(array2.shape[0])
        mat1 = mat1@np.random.normal(size=(mat1.shape[1], 30), loc=1.0, scale=1.0)
        mat2 = mat2@np.random.normal(size=(mat2.shape[1], 30), loc=1.0, scale=1.0)
        return mat1@mat2.T


