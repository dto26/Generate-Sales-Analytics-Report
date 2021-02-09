# python libraries
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import calendar
# local files
# from helper import Mode, load_relevant_data

#Task 1: Read in data
data = pd.read_csv('./data/clean_data/cleaned_data.csv')

# Question 1: What was the best month for sales? How much was earned that month?
''' bar chart of total monthly sales '''
def plot_monthly_sales():
    months = range(1, 13)
    plt.bar(months, data.groupby(['Month']).sum()['Sales'])
    plt.xticks(months)
    plt.ylabel('Sales USD($)')
    plt.xlabel('Month Number')
    plt.savefig('./resources/monthly_sales_plot.png', dpi=500)
    plt.show()

# Question 2: Which countries were sold in the most?
''' bar chart with total sales per country
    note: does not look good with the mock data (249 countries)
'''
def plot_country_sales():
    keys = [country for country, df in data.groupby(['Country'])]
    plt.bar(keys, data.groupby(['Country']).sum()['Sales'])
    plt.xticks(keys, rotation='vertical', size=8)
    plt.ylabel('Sales USD($)')
    plt.xlabel('Month number')
    plt.savefig('./resources/country_sales.png', dpi=500)
    plt.show()

# Question 3: Which products sold the most?
def plot_product_sales():
    prod_group = data.groupby('Product')
    quantity_ordered = prod_group.sum()['QuantityOrdered']
    keys = [pair for pair, df in prod_group]
    plt.bar(keys, quantity_ordered)
    plt.xticks(keys, rotation='vertical', size=8)
    plt.savefig('./resources/product_sales.png', dpi=500)
    plt.show()

# Question 4: What is the correlation between sale price and quantity ordered?
def plot_orders_vs_price():
    prod_group = data.groupby('Product')
    prices = data.groupby('Product').mean()['Price']
    quantity_ordered = prod_group.sum()['QuantityOrdered']
    keys = [pair for pair, df in prod_group]

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.bar(keys, quantity_ordered, color='b')
    ax2.plot(keys, prices, color='g')

    ax1.set_xlabel('Product')
    ax1.set_xticklabels(keys, rotation='vertical', size=8)
    ax1.set_ylabel('Quantity Ordered', color='b')
    ax2.set_ylabel('Price USD($)', color='g')

    plt.savefig('./resources/orders_vs_price.png', dpi=500)
    fig.show()

# Question 5: Orders per country on world map?
def plot_world_sales():
    filename = 'world_sales.png'
    dates = list(data.columns)
    # Get quantity ordered by country
    df = data.groupby('Country')[dates].agg('sum')
    df = df.drop(columns=['OrderID', 'Price', 'Sales', 'Month', 'Day', 'Year'])
    # print(df)
    create_global_figure(df)

def create_global_figure(df):
    year = data.Year[1]
    df['QuantityOrdered'] = pd.to_numeric(df['QuantityOrdered'])
    df['Country'] = df.index

    fig = px.choropleth(
        df,
        locations='Country',
        locationmode="country names",
        scope="world",
        color="QuantityOrdered",
        hover_name="Country",
        color_continuous_scale='Viridis',
        title=f"Global Sales {year}",
        width=1000,
    )
    fig.update_layout(margin=dict(l=0, r=0, t=70, b=20), title={"font": {"size": 20}, "x":0.5},)
    fig.write_image('./resources/world_sales.png', engine='kaleido')

# uncomment for testing
# plot_monthly_sales()
# plot_country_sales()
# plot_product_sales()
# plot_orders_vs_price()
# plot_world_sales()
