# %% 
import pandas as pd
# %%
pathCSV = "datasets/Airbnb_Open_Data.csv"
df = pd.read_csv(pathCSV, sep=",")
# %%
df.head()
# %% 
# transformando colunas em listas
df.columns # colunas
columns_datasets = df.columns.tolist()
print(columns_datasets)
# %%
df.dtypes
# %%
df.sample(5)
# %%
# Limpar dados
df["price"]
df["price"] = df["price"].str.replace('$','')
df["price"] = df["price"].str.replace(',','.')
df["price"] = df["price"].astype(float)
df["price"]

# %%
df["price"].mean()
# %%
