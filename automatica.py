import numpy as np
import matplotlib.pyplot as plt
import control as ctrl


def bode_nyquist_plot(numeratore, denominatore):
    """
    Disegna i diagrammi di Bode e di Nyquist per una funzione di trasferimento.

    Parametri:
    numeratore (list): Coefficienti del numeratore.
    denominatore (list): Coefficienti del denominatore.
    """
    # Creazione della funzione di trasferimento
    sistema = ctrl.TransferFunction(numeratore, denominatore)

    # Disegno del diagramma di Bode
    plt.figure(figsize=(12, 6))
    ctrl.bode(sistema, dB=True, deg=True, omega_limits=(1e-2, 1e2), omega_num=500)
    plt.suptitle("Diagrammi di Bode")
    plt.tight_layout()

    # Disegno del diagramma di Nyquist
    plt.figure(figsize=(8, 8))
    ctrl.nyquist(sistema, omega=np.logspace(-2, 2, 500))
    plt.title("Diagramma di Nyquist")
    plt.grid(True)
    plt.xlabel("Reale")
    plt.ylabel("Immaginario")

    # Mostra i grafici
    plt.show()


# Esempio di utilizzo
if __name__ == "__main__":
    # Funzione di trasferimento: H(s) = 1 / (T1*s + 1)(T2*s + 1)
    numeratore = [1]
    denominatore = [1, 3, 2]  # Forma espansa con costanti di tempo

    bode_nyquist_plot(numeratore, denominatore)

