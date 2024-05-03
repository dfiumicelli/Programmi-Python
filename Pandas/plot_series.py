import matplotlib
import pandas as pd
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


index = range(50)
values = np.random.normal(size=(50, ))
s = pd.Series(values, index=index)
s.plot(kind="box")
s.plot.hist()

plt.show()
