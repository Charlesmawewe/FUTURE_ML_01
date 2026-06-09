# FUTURE_ML_01
Ml task 1
# Superstore Sales Analytics Dashboard

## Overview

This project is an end-to-end data analytics solution built using Python, Streamlit, Plotly, and Scikit-learn. The dashboard provides interactive insights into sales performance, profitability, customer activity, regional trends, and future sales forecasts using historical Superstore data.

The goal of the project is to demonstrate data cleaning, exploratory data analysis (EDA), dashboard development, and basic machine learning forecasting in a business context.


## Features

### KPI Dashboard

* Total Sales
* Total Profit
* Total Orders
* Total Customers

### Interactive Analysis

* Monthly Sales Trend
* Profit by Category
* Sales by Region
* Sales by Segment
* Top 10 Products by Sales
* Profit vs Sales Analysis

### Forecasting

* 6-Month Sales Forecast
* Linear Regression model using Scikit-learn

### Filtering

Users can filter dashboard results by:

* Region
* Category
* Segment


## Technologies Used

* Python
* Pandas
* NumPy
* Streamlit
* Plotly
* Scikit-learn
* Git
* GitHub


## Machine Learning Component

A Linear Regression model was implemented using Scikit-learn to forecast future sales based on historical monthly sales data.

The model:

1. Aggregates sales by month
2. Learns historical sales trends
3. Predicts sales for the next six months
4. Displays predictions directly in the dashboard


## Business Value

The dashboard helps businesses understand:

* Sales performance over time
* Most profitable product categories
* Regional sales distribution
* Customer segment performance
* Product demand concentration
* Future revenue trends

Potential business applications include:

* Inventory planning
* Budget forecasting
* Marketing strategy
* Revenue forecasting
* Business performance monitoring


## Project Structure

```text
FUTURE_ML_01/
│
├── data/
│   └── Sample - Superstore.csv
│
├── dashboard.py
├── analysis.py
├── superstore_clean.csv
├── README.md
│
└── notebooks/
```


## Installation

Clone the repository:

```bash
git clone <repository-url>
cd FUTURE_ML_01
```

Install dependencies:

```bash
pip install pandas numpy plotly streamlit scikit-learn
```

Run the dashboard:

```bash
streamlit run dashboard.py
```



## Author

Charles Mawewe

Data Science Student | Aspiring Data Engineer

This project was developed as part of my data analytics and machine learning portfolio to demonstrate practical skills in data processing, visualization, dashboard development, and predictive analytics.

