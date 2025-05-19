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
t = df['tpep_pickup_datetime'][0]
t
# %%

# df['tpep_pickup_datetime'].year  # error
df['tpep_pickup_datetime'].dt.year

# Speical types:
# dt: Timestamp
# str: str (lower, upper, ...)
# cat: categorial
# sparse: ...
# %%

orig_df = df  # keep it around
mask = (df['tpep_pickup_datetime'].dt.year == 2020) & (
    df['tpep_pickup_datetime'].dt.month == 3
)

# df now is a "view" on the orignal df
df = df[mask]
print(len(orig_df), '->', len(df))

# %%
# df = df.dropna()
# print(len(df))

# %%
# Cleaning data:
# - drop invalid/missing
# - fill with some value

# Fill missing passenger count with 1

mask = pd.isnull(df['passenger_count'])
# df[mask]['passenger_count'] = 1 # BUG: Changing a view
df.loc[mask, 'passenger_count'] = 1

# %% Calculate the average speed in mph
duration = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
duration.describe()
# %%
mask = df['tpep_dropoff_datetime'] < df['tpep_pickup_datetime']
mask.sum()  # See how many rows are bad
df = df[~mask]
# %%

duration = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
duration.describe()
# %% Duration outliers
duration[duration > duration.quantile(0.99)]
# %% Clean rides above 2 hours
mask = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']) < pd.Timedelta('2h')
(~mask).sum()

# %%
df = df[mask]
duration = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
duration.describe()
# %%
# df['trip_distance'] / duration # error
duration_hours = duration / pd.Timedelta('1h')
speed_mph = df['trip_distance'] / duration_hours
speed_mph.mean()

# %%

mask = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']) > pd.Timedelta('1min')
(~mask).sum()
df = df[mask]
# %%

duration = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
duration_hours = duration / pd.Timedelta('1h')
speed_mph = df['trip_distance'] / duration_hours
speed_mph.mean()
# %% Exercise: What is the median tip percent
# for rides above 1 mile?
