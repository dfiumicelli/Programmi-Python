import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Superenalotto2:
    def __init__(self, schedina, premi):
        self.schedine_df = pd.read_csv(schedina)
        self.premi_df = pd.read_csv(premi)

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
                    print("Vincente senza superstar")
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
        custom_array = np.random.uniform(low=0.0, high=5.0, size=numeri_disp.shape)
        return numeri_disp @ custom_array


sup = Superenalotto2("schedina.csv", "premi.csv")
numeri_vincenti = []
count = 0
while count < 6:
    print("Numeri inseriti finora: ", len(numeri_vincenti))
    numero = int(input("Inserisci numero vincente: "))
    if numero < 1 or numero > 90 or numero in numeri_vincenti:
        print("Inserisci un numero compreso tra 1 e 90 che non sia già stato inserito")
    else:
        numeri_vincenti.append(numero)
        count += 1

superstar = None
while superstar is None:
    numero = int(input("Inserisci superstar: "))
    if numero < 1 or numero > 90 or numero in numeri_vincenti:
        print("Inserisci un numero compreso tra 1 e 90 che non sia già stato inserito")
    else:
        superstar = numero

sup.schedine_vincenti(numeri_vincenti, superstar)
print(sup.guadagno(numeri_vincenti, superstar))
sup.istogramma()
