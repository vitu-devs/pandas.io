# %% 
import pandas as pd
# %%
pathCSV = "datasets/Airbnb_Open_Data.csv"
df = pd.read_csv(pathCSV, sep=",")
# %%
df.head()
# %%
