import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

class Superenalotto:

    def __init__(self, file_schedina, file_premi):
        self.schedine_df = pd.read_csv(file_schedina)
        self.premi_df = pd.read_csv(file_premi)

    def schedine_vincenti(self, numeri_vincenti, superstar):
        vincenti_np = np.array(numeri_vincenti)
        num1_6 = self.schedine_df[["num1", "num2", "num3", "num4", "num5", "num6"]]
        for index, rows in num1_6.iterrows():
            numeri_indovinati = np.intersect1d(rows.to_numpy(), vincenti_np)
            if numeri_indovinati.size > 0:
                if superstar == self.premi_df.iloc[index].superstar:
                    print("Vincente con superstar!")
                    print("Numeri indovinati: ", numeri_indovinati)
                    print("Superstar: ", superstar)
                    temp_df = self.premi_df[self.premi_df["numero_numeri_indovinati"] == numeri_indovinati.size]
                    temp_df = temp_df[temp_df["superstar_indovinato"] == 1]
                    premio = temp_df["premio"].values[0]
                    print("Premio: ", premio)
                else:
                    print("Vincente senza superstar!")
                    print("Numeri indovinati: ", numeri_indovinati)
                    temp_df = self.premi_df[self.premi_df["numero_numeri_indovinati"] == numeri_indovinati.size]
                    temp_df = temp_df[temp_df["superstar_indovinato"] == 0]
                    premio = temp_df["premio"].values[0]
                    print("Premio: ", premio)

    def guadagno(self, numeri_vincenti, superstar):
        vincenti_np = np.array(numeri_vincenti)
        premi_totali = 0.0
        costi_totali = 0.0
        num1_6 = self.schedine_df[["num1", "num2", "num3", "num4", "num5", "num6"]]
        for index, rows in num1_6.iterrows():
            numeri_indovinati = np.intersect1d(rows.to_numpy(), vincenti_np)
            if numeri_indovinati.size > 0:
                if superstar == self.premi_df.iloc[index].superstar:
                    temp_df = self.premi_df[self.premi_df["numero_numeri_indovinati"] == numeri_indovinati.size]
                    temp_df = temp_df[temp_df["superstar_indovinato"] == 1]
                    premio = temp_df["premio"].values[0]
                    premi_totali += premio
                else:
                    temp_df = self.premi_df[self.premi_df["numero_numeri_indovinati"] == numeri_indovinati.size]
                    temp_df = temp_df[temp_df["superstar_indovinato"] == 0]
                    premio = temp_df["premio"].values[0]
                    premi_totali += premio
            costi_totali += self.schedine_df.iloc[index].costo_schedina
        return costi_totali - premi_totali









sup = Superenalotto("schedina.csv", "premi.csv")
print(sup.schedine_df.head())
sup.schedine_vincenti([1, 2, 3, 4, 5, 6], 8)