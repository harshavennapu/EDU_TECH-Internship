import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Titanic-Data.csv")
print(df.head())
print(df.isnull().sum())
sns.heatmap(df.isnull(), cbar=False)
plt.show()
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
sns.boxplot(df['Age'])
plt.show()
print(df.isnull().sum())
df.to_csv("cleaned_Titanic-Data.csv", index=False)
print(df.isnull().sum())
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(['Cabin'], axis=1, inplace=True)
print(df.isnull().sum())
df.to_csv("cleaned_titanic.csv", index=False)