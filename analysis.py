# python libraries
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from datetime import datetime, timedelta
import calendar

# local files
# from helper import Mode, load_relevant_data

#Task 1: Read in data
data = pd.read_csv('./data/clean_data/cleaned_data.csv')

# Question 1: What was the best month for sales? How much was earned that month?
''' bar chart of total monthly sales '''
def bar_plot_monthly_sales():
    months = range(1, 13)
    plt.bar(months, data.groupby(['Month']).sum()['Sales'])
    plt.xticks(months)
    plt.ylabel('Sales USD($)')
    plt.xlabel('Month Number')
    plt.savefig('./resources/monthly_sales_plot.png', dpi=500)
    plt.show()

# line chart of total sales $ per month
def line_plot_monthly_sales():
    months = np.array(range(1, 13))
    # months_smooth = np.linspace(months.min(), months.max(), 200)
    df = data.groupby(['Month']).sum()['Sales']
    # y = df.to_numpy()
    # spl = make_interp_spline(months, y, k=5)
    # y_smooth = spl(months_smooth)
    # plt.plot(months_smooth, y_smooth)

    markers_on = np.round_(df.to_numpy(), decimals=2)
    # print(markers_on)
    plt.plot(months, df.to_numpy(), '-o')
    plt.xticks(months)
    plt.ylabel('Sales USD($)')
    plt.xlabel('Month Number')
    plt.savefig('./resources/monthly_sales_line_plot.png', dpi=500)
    plt.show()

# Question 2: Which countries were sold in the most?
''' bar chart with total sales per country
    note: does not look good with the mock data (249 countries)
'''
def bar_plot_country_sales():
    keys = [country for country, df in data.groupby(['Country'])]
    plt.bar(keys, data.groupby(['Country']).sum()['Sales'])
    plt.xticks(keys, rotation='vertical', size=8)
    plt.ylabel('Sales USD($)')
    plt.xlabel('Month number')
    plt.savefig('./resources/country_sales.png', dpi=500)
    plt.show()

# Question 3: Which products sold the most?
def bar_plot_product_sales():
    prod_group = data.groupby('Product')
    quantity_ordered = prod_group.sum()['QuantityOrdered']
    keys = [pair for pair, df in prod_group]
    plt.bar(keys, quantity_ordered)
    plt.xticks(keys, rotation='vertical', size=8)
    plt.savefig('./resources/product_sales.png', dpi=500)
    plt.show()

# Question 4: What is the correlation between sale price and quantity ordered?
def bar_plot_orders_vs_price():
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
def map_plot_world_sales():
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

# Question 6: Percentage of orders by product (pie chart)
def pie_plot_products_orders_percentage():
    df = data.groupby(['Product']).sum()['QuantityOrdered']
    quantity = []
    labels = []
    for items in df.iteritems():
        labels.append(items[0])
        quantity.append(items[1])
    fig, ax = plt.subplots()
    
    size = 0.3
    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(len(labels)))

    ax.pie(quantity, labels=labels, colors=outer_colors, autopct='%1.1f%%', wedgeprops=dict(width=size, edgecolor='w'))

    ax.set(aspect="equal", title='Percentage of orders by product')
    plt.savefig('./resources/pie_products_orders.png', dpi=500)
    plt.show()

# uncomment for testing
# bar_plot_monthly_sales()
# line_plot_monthly_sales()
# bar_plot_country_sales()
# bar_plot_product_sales()
# bar_plot_orders_vs_price()
# map_plot_world_sales()
pie_plot_products_orders_percentage()
