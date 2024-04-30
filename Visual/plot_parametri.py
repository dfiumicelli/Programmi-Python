import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-whitegrid")
x = np.linspace(0, 10, 100)
plt.plot(x, np.cos(x), color="r", label="Cosine")
plt.plot(x, np.tan(x), color="g", label="Tangente")
plt.title("Cosine vs Tangente")
plt.xlabel("X")
plt.ylabel("cos(x) e tan(x)")
plt.legend()
plt.show()
