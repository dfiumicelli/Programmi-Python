import pandas as pd
import numpy as np
months = ["gennaio", "febbraio", "marzo"]
days = [31, 28, 31]
s = pd.Series(days, index=months)
print(s["gennaio": "marzo"])

index = range(50)
num = np.random.normal(size=(50,))
p = pd.Series(num, index=index)
print(p)