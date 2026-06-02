import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./data/Sample - Superstore.csv")

print(df.head())

import pandas as pd

df = pd.read_csv("data/Sample - Superstore.csv")

print("\nColumns:")
print(df.columns)

print("\nDataset Shape:")
print(df.shape)

print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

import pandas as pd

# Load dataset
df = pd.read_csv("data/Sample - Superstore.csv")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Create new useful columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

print(df.head())

print("\nTOTAL SALES")
print(round(df["Sales"].sum(), 2))

print("\nTOTAL PROFIT")
print(round(df["Profit"].sum(), 2))

print("\nTOTAL ORDERS")
print(df["Order ID"].nunique())

print("\nTOTAL CUSTOMERS")
print(df["Customer ID"].nunique())

sales_by_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY CATEGORY")
print(sales_by_category)
profit_by_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nPROFIT BY CATEGORY")
print(profit_by_category)
sales_by_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY REGION")
print(sales_by_region)
top_states = (
    df.groupby("State")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 STATES BY PROFIT")
print(top_states)

sales_by_category.plot(kind="bar")

plt.title("Sales by Category")
plt.ylabel("Sales")
plt.xlabel("Category")

plt.tight_layout()
plt.show()

profit_by_category.plot(kind="bar")

plt.title("Profit by Category")
plt.ylabel("Profit")
plt.xlabel("Category")

plt.tight_layout()
plt.show()
sales_by_region.plot(kind="bar")

plt.title("Sales by Region")
plt.ylabel("Sales")
plt.xlabel("Region")

plt.tight_layout()
plt.show()
monthly_sales = (
    df.groupby(
        df["Order Date"].dt.to_period("M")
    )["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)
monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
df.to_csv("superstore_clean.csv", index=False)

print("\nClean dataset exported successfully!")