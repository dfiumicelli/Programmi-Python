import matplotlib
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')

months = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno"]

days_month = [31, 28, 31, 30, 31, 30]

s = pd.Series(days_month, index=months)
print(s.sum())
print(s.max())
print(s.min())

# oppure si può usare semplicemente la funzione describe

print(s.describe())


# possiamo applicare a una series una determinata funzione:


def my_func(x):
    print("Elemento della serie: ", x)
    return x ** 2


print(s.apply(my_func))


# possiamo passare più parametri alla funzione


def my_func(x, custom_param):
    print("Elemento della serie: ", x)
    return x ** 2 + custom_param


print(s.apply(my_func, args=(5,)))

# Possiamo convertire la serie di pandas in un ndarray di numpy tramite la funzione to_numpy, perdendo
# però gli indici. Si può plottare anche tramite pandas sfruttando matplotlib

s.plot()
plt.show()
