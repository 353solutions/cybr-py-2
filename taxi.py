# python -m pip install pandas pyarrow

# %%
import pandas as pd

df = pd.read_parquet('yellow_tripdata_2020-03.parquet')
# df short for DataFrame

# %%
df.columns

# %%
df.dtypes

# passenger_count is float64 since we have
# missing values
# Use pd.isnull to find out of a number is nan
# (None, NaT, ...)

# %%
2**1000
# %%
n = df['VendorID'][1]  # 2
n**1000

# %% Column access (pd.Series)
df['VendorID']

# %%
df['VendorID'].unique()

# %%
df['trip_distance'].describe()
# %%
i = df['trip_distance'].idxmax()
df.loc[i]  # Row access (slow-ish)
# %%
# deep=True means also memory allocated to strings
mem_usage = df.memory_usage(deep=True).sum()
mem_usage / 1_000_000
# %%
df[:5]  # first 5 row
# See also df.head, df.sample
# %%
df.sample(5)

# %%
df['tpep_pickup_datetime'].describe()

# GIGO: Garbage in, garbage out

# %% Exercise: How much money was collected?
# total_amount column
total = df['total_amount'].sum()
print(f'{total:,}')
# %% Get rows by condition: boolean indexing

s = pd.Series([1, 2, 3, 4, 5, 6, 7])
s > 3  # element-wise operation

# %%
mask = s > 3
s[mask]
# %%
s[s > 3]
# %%

# & = and
# | = or
# ~ = not

s[(s > 3) & (s < 6)]
# Python: s > 3 and s < 6
# %%
s[(s < 3) | (s > 5)]

# %%
s[~(s > 5)]  # s[s <= 5]
# %% Exercise: What is the total distance
# of rides with more than 1 passenger
mask = df['passenger_count'] > 1
df[mask]['trip_distance'].sum()

# %%

(
    df[df['passenger_count'] > 1][  # filter
        'trip_distance'
    ].sum()  # column access  # sum (aggregation)
)

# flow style

# %%
