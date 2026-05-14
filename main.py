from encodings import cp1252

import pandas as pd


# load dataset
df = pd.read_csv("Data/retail_sales_clean.csv", encoding="cp1252")

# shows first five rows
print(df.head())

# info
print(df.info())

# check missing values
print(df.isnull().sum)

#remove a missing values
df = df.dropna()

# remove duplicates
df = df.drop_duplicates()

# Converted Data colum
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Create new feature

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Day'] = df['Order Date'].dt.day

# Clean columns name
print(df.columns)
df.columns = df.columns.str.lower().str.replace(' ','_')

# final check
print(df.info())
print(df.head())

df.rename(columns={"sub-category": "sub_category"},inplace=True)

df.to_csv("Final_cleaned_retail_data.csv", index=False)

print("Phase 1 is Completed Successfully")
