# %% 
import pandas as pd
# %%
pathCSV = "datasets/Airbnb_Open_Data.csv"
df = pd.read_csv(pathCSV, sep=",")
# %%
# df.head()
df = df.sort_values("id", ascending=True)
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
# Limpar dados Price
df["price"]
df["price"] = df["price"].str.replace('$','')
df["price"] = df["price"].str.replace(',','.')
df["price"] = df["price"].astype(float)
df["price"]
# %%
# Filtrando License para nulo
df["license"] = df["license"].fillna('')
# %%
df["service fee"] = df["service fee"].fillna("0")
df["service fee"] = df["service fee"].str.replace("$", "")
df["service fee"] = df["service fee"].str.replace(",", ".")
df["service fee"] = df["service fee"].astype(float)
df["service fee"]
# %%
# Filtrando nulo de host_identity_verified
df["host_identity_verified"] = df["host_identity_verified"].fillna("unconfirmed")

# %%
df["NAME"] = df["NAME"].fillna("")
df

# %%
df["price"].mean()
# %%
# Visualização em EXCEL
df.to_excel("dataframe_incompleto.xlsx", index=False)
# %%
# reconhemcimento de dados nulos
df.isnull()
# %%
df
# %%
df.to_excel("dataframe_incompleto.xlsx", index=False)
# %%
