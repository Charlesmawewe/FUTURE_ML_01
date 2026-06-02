import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.linear_model import LinearRegression

# PAGE SETUP 
st.set_page_config(page_title="Superstore Dashboard", layout="wide")

# LOAD DATA 
df = pd.read_csv("superstore_clean.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])

# SIDEBAR FILTERS 
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

segment = st.sidebar.multiselect(
    "Segment",
    df["Segment"].unique(),
    default=df["Segment"].unique()
)

df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Segment"].isin(segment))
]

#  KPI CALCULATIONS 
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

# Header
st.title(" Superstore Sales Dashboard")

# KPI ROW 
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Orders", total_orders)
col4.metric("Customers", total_customers)

st.divider()

# ROW 1: TREND + CATEGORY 
col1, col2 = st.columns(2)

with col1:
    st.subheader("Monthly Sales Trend")

    monthly = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
    monthly["Order Date"] = monthly["Order Date"].astype(str)

    fig = px.line(monthly, x="Order Date", y="Sales")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Profit by Category")

    cat = df.groupby("Category")["Profit"].sum().reset_index()

    fig = px.bar(cat, x="Category", y="Profit")
    st.plotly_chart(fig, use_container_width=True)

# ROW 2: REGION + SEGMENT
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Region")

    reg = df.groupby("Region")["Sales"].sum().reset_index()

    fig = px.pie(reg, names="Region", values="Sales", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Sales by Segment")

    seg = df.groupby("Segment")["Sales"].sum().reset_index()

    fig = px.pie(seg, names="Segment", values="Sales", hole=0.5)
    st.plotly_chart(fig, use_container_width=True)

# ROW 3: TOP PRODUCTS + SCATTER 
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Products")

    top = df.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()

    fig = px.bar(top, x="Sales", y="Product Name", orientation="h")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Profit vs Sales")

    fig = px.scatter(df, x="Sales", y="Profit", color="Category")
    st.plotly_chart(fig, use_container_width=True)

# FORECASTING 
st.divider()
st.subheader("Sales Forecast (Next 6 Months)")

monthly = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
monthly["Order Date"] = monthly["Order Date"].astype(str)
monthly["Time"] = np.arange(len(monthly))

X = monthly[["Time"]]
y = monthly["Sales"]

model = LinearRegression()
model.fit(X, y)

future = 6
future_time = np.arange(len(monthly), len(monthly) + future).reshape(-1, 1)
future_pred = model.predict(future_time)

future_dates = pd.date_range(
    start=pd.to_datetime(monthly["Order Date"]).max(),
    periods=future + 1,
    freq="ME"
)[1:]

forecast_df = pd.DataFrame({
    "Order Date": future_dates,
    "Sales": future_pred
})

fig = px.line(monthly, x="Order Date", y="Sales")
fig.add_scatter(x=forecast_df["Order Date"], y=forecast_df["Sales"], mode="lines", name="Forecast")

st.plotly_chart(fig, use_container_width=True)

# BUSINESS INSIGHT
st.subheader("Business Insight")

st.write("""
This dashboard helps a business understand:
- Sales performance over time
- Most profitable categories
- Regional and segment performance
- Product demand concentration
- Future sales forecast (next 6 months)

This can be used for:
- Inventory planning
- Budget planning
- Marketing strategy
- Revenue forecasting
""")