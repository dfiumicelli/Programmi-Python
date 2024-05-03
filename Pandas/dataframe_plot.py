import matplotlib
import pandas as pd
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris.data',
                 names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Category"],
                 header=None)

# plottiamo il dataframe
pd.plotting.scatter_matrix(df, alpha=0.2, diagonal="kde")
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
sns.pairplot(df, hue="Category")
plt.show()