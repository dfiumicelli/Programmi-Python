import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

matplotlib.use('TkAgg')

sns.set()

df = pd.read_csv('iris.data', names=["sepal_length", "sepal_width", "petal_length", "petal_width", "category"])
print(df.head())
iris_versicolor = df[df['category'] == 'Iris-versicolor']
sns.pairplot(iris_versicolor)
plt.show()
