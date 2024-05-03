import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('TkAgg')

sns.set()

iris = sns.load_dataset('iris')
print(iris.head())
sns.pairplot(iris, hue='species', height=2.5)
plt.show()
