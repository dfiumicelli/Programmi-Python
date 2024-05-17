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
                if superstar == self.schedine_df.iloc[index].superstar:
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
                if superstar == self.schedine_df.iloc[index].superstar:
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

    def istogramma(self):
        num1_6 = self.schedine_df[["num1", "num2", "num3", "num4", "num5", "num6"]]
        numeri = num1_6.values.flatten()
        plt.hist(numeri, bins=90)
        plt.title("Istogramma dei numeri giocati")
        plt.show()

    def custom_func(self):
        num1_6 = self.schedine_df[["num1", "num2", "num3", "num4", "num5", "num6"]]
        numeri = num1_6.values.flatten()
        numeri = numeri[numeri > 30]
        numeri_disp = numeri[numeri % 2 == 1]
        a = np.random.uniform(low=0.0, high=5.0, size=numeri_disp.shape)
        print(a * numeri_disp)


count = 0
numeri_vincenti = []
while count < 6:
    print("Numeri inseriti fin'ora: ", len(numeri_vincenti))
    numero = int(input("Inserire il numero vincente: \n"))
    if numero > 90 or numero < 1 or numero in numeri_vincenti:
        print("Inserire un numero tra 1 e 90 e che non sia già stato inserito")
    else:
        numeri_vincenti.append(numero)
        count = count + 1
superstar = None
while not superstar:
    numero = int(input("Inserire il numero superstar: \n"))
    if numero > 90 or numero < 1 or numero in numeri_vincenti:
        print("Inserire un numero tra 1 e 90 e che non sia già stato inserito")
    else:
        superstar = numero
sup = Superenalotto("schedina.csv", "premi.csv")
print(sup.schedine_df.head())
sup.schedine_vincenti(numeri_vincenti, superstar)
sup.istogramma()
sup.custom_func()
