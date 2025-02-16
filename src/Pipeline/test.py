import pandas as pd

df = pd.read_csv("Data\\04_encoded_Data\\X_train.csv")

df_2 = pd.read_csv("Data\\02_CleanedData\\CleanedData.csv")

#print(df.isnull().sum())
print(df_2.isnull().sum())