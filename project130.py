import pandas as pd 
import csv 

df = pd.read_csv("final.csv")
del df["Luminosity"]

print(df.shape)
print(list(df))
df.to_csv("final_data.csv")

f1 = pd.read_csv("final_data.csv")
del df["Unnamed: 0"]
del df["Unnamed: 9"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
df.to_csv("final_data1.csv")
