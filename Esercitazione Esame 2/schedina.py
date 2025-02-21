import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy.ma.extras import intersect1d


class Schedina:
    def __init__(self):
        self.schedina = pd.read_csv('schedina.csv')
        self.premi = pd.read_csv('premi.csv')

    def vinto(self, vincenti, superstar):
        vincenti_np = np.array(vincenti)
        num1_6 = self.schedina[["num1","num2","num3","num4","num5","num6"]]
        for index, row in num1_6.iterrows():
            numeri_indovinati = intersect1d(row.to_numpy(), vincenti_np)
            if numeri_indovinati.size >= 0:
                if superstar == self.schedina.iloc[index].superstar:
                    print("Vincente con superstar!")
                    print("Numeri indovinati: ", numeri_indovinati)
                    print("Superstar: ", superstar)
                    a=self.premi[(self.premi["numero_numeri_indovinati"] == numeri_indovinati.size) & (self.premi["superstar_indovinato"] == 1)]
                    premio = a["premio"].values[0]
                    print("Premio: ", premio)
                else:
                    print("Vincente senza superstar!")
                    print("Numeri indovinati: ", numeri_indovinati)
                    temp = self.premi[self.premi["numero_numeri_indovinati"] == numeri_indovinati.size]
                    temp = temp[temp["superstar_indovinato"] == 0]
                    premio = temp["premio"].values[0]
                    print("Premio: ", premio)

    def guadagno(self, vincenti, superstar):
        costi_tot = 0.0
        premi_tot = 0.0
        vincenti_np = np.array(vincenti)
        num1_6 = self.schedina[["num1", "num2", "num3", "num4", "num5", "num6"]]
        for index, row in num1_6.iterrows():
            numeri_indovinati = intersect1d(row.to_numpy(), vincenti_np)
            if numeri_indovinati.size >= 0:
                if superstar == self.schedina.iloc[index].superstar:
                    temp = self.premi[(self.premi["numero_numeri_indovinati"] == numeri_indovinati.size) & (self.premi["superstar_indovinato"] == 1)]
                    premio = temp["premio"].values[0]
                    premi_tot += premio
                else:
                    temp = self.premi[(self.premi["numero_numeri_indovinati"] == numeri_indovinati.size) & (self.premi["superstar_indovinato"] == 0)]
                    premio = temp["premio"].values[0]
                    premi_tot += premio
            costi_tot += self.schedina.iloc[index]["costo_schedina"]
        return costi_tot - premi_tot

    def istogramma(self):
        num1_6 = self.schedina[["num1", "num2", "num3", "num4", "num5", "num6"]]
        numeri = num1_6.values.flatten()
        plt.hist(numeri, bins=90)
        plt.title("Istogramma dei numeri giocati")
        plt.show()

    def func(self):
        num = self.schedina[["num1", "num2", "num3", "num4", "num5", "num6"]].values.flatten()
        num = num[(num>30) & (num % 2 ==1)]
        print(num*np.random.uniform(size=num.shape, low=0.0, high=5.0))


s = Schedina()
#s.vinto([10,45,1,2,3,4], 11)
s.func()