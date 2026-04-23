import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')   # or 'tips'
df.head()
df.info()
df.describe()
df.isnull().sum()
df.hist(figsize=(10,8))
plt.show()

sns.boxplot(data=df)
plt.title("Boxplot")
plt.show()
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df)
plt.title("Scatter Plot")
plt.show()
corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
sns.pairplot(df, hue='species')
plt.show()