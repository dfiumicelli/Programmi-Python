# Imports
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import re


pd.set_option('display.expand_frame_repr', False)
# Import data
df_train = pd.read_csv('titanic.csv')

print(df_train.head())
print(df_train.info())
print(df_train.describe())

print(df_train.isnull)

sns.heatmap(df_train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

sns.catplot(x='Survived',col='Gender',kind='count',data=df_train)
plt.show()

sns.countplot(x='Survived',hue='Pclass',data=df_train)
plt.show()

sns.countplot(x='SibSp',data=df_train)
plt.show()

sns.histplot(df_train['Age'].dropna(),kde=False,color='darkred')
plt.show()

plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass',y='Age',data=df_train,palette='winter')

def impute(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 38
        elif Pclass == 2:
            return 29
        else:
            return 24

    else:
        return Age

df_train['Age']=df_train[['Age','Pclass']].apply(impute,axis=1)

# Store target variable of training data in a safe place
survived_train = df_train.Survived

print(df_train.columns)

plt.show()

# Concatenate training and test sets
data = df_train.drop(['Survived'], axis=1)

# View head
print(data.info())

print(data.Name.tail())

data['Title'] = data.Name.apply(lambda x: re.search(' ([A-Z][a-z]+)\.', x).group(1))
sns.countplot(x='Title', data=data)
plt.xticks(rotation=45)
plt.show()


data['Title'] = data['Title'].replace({'Mlle':'Miss', 'Mme':'Mrs', 'Ms':'Miss'})
data['Title'] = data['Title'].replace(['Don', 'Dona', 'Rev', 'Dr',
                                            'Major', 'Lady', 'Sir', 'Col', 'Capt', 'Countess', 'Jonkheer'],'Special')
sns.countplot(x='Title', data=data)
plt.xticks(rotation=45)
plt.show()

print(data.tail())

# Did they have a Cabin?
data['Has_Cabin'] = ~data.Cabin.isnull()

# View head of data
print(data.head())

data.drop(['Cabin', 'Name', 'PassengerId', 'Ticket'], axis=1, inplace=True)
print(data.head())

print(data.info())

sns.heatmap(data.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

# Impute missing values for Age, Fare, Embarked
data['Age'] = data.Age.fillna(data.Age.median())
data['Embarked'] = data['Embarked'].fillna('S')
print(data.info())

print(data.head())

# Binning numerical columns
data['CatAge'] = pd.qcut(data.Age, q=4, labels=False )
data['CatFare']= pd.qcut(data.Fare, q=4, labels=False)
print(data.head())

data = data.drop(['Age', 'Fare'], axis=1)
print(data.head())

# Transform into binary variables
data_dum = pd.get_dummies(data, drop_first=True)
print(data_dum.head())
corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.show()

print(data.head())


