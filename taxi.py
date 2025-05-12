# python -m pip install pandas pyarrow

# %%
import pandas as pd

df = pd.read_parquet('yellow_tripdata_2020-03.parquet')
# df short for DataFrame

# %%
df.columns

# %%
df.dtypes
# %% Column access (pd.Series)
df['VendorID']

# %%
df['VendorID'].unique()

# %%
df['trip_distance'].describe()
# %%
i = df['trip_distance'].idxmax()
df.iloc[i]

# %%
2**1000
# %%
n = df['VendorID'][1]  # 2
n**1000
# %%
