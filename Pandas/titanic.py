import matplotlib
import pandas as pd
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('titanic.csv')
print(df.head())
print(df.info())
print(df.describe())
sns.heatmap(df.isnull())
plt.show()
