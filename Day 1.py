#Importing Libraries
import pandas as pd
import numpy as np
#Loading Dataset
df = pd.read_csv("data.csv")
df.head()
#Check Structure
df.info()
df.dtypes
df.isnull().sum()
numerical = df.select_dtypes(include=['int64','float64'])
categorical = df.select_dtypes(include=['object'])
for col in categorical.columns:
    print(col, df[col].unique())
df.shape
