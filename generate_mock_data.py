import pandas as pd
import numpy
import pycountry
import random
import datetime
import calendar

products = {
    # Product: [Price, Weight]
    'notebook': [4.99, 30],
    'pen': [1.25, 15],
    'pencil': [0.99, 30],
    'eraser': [0.49, 20],
    'ruler': [3.99, 10],
    'charging cable': [11.95, 40],
    'headphones': [99.99, 35],
    'laptop': [900, 65],
    'AA batteries (4-pack)': [3.99, 20],
    'wireless mouse': [25.99, 55],
    'mouse pad': [5.99, 50]
}

countries_list = list(pycountry.countries)[1:249]

def generate_random_dates(month):
    # generate a date in the yyyy-mm-dd format
    day_range = calendar.monthrange(2020, month)[1]
    random_day = random.randint(1, day_range)
    date = datetime.datetime(2020, month, random_day)

    return date.strftime("%y-%m-%d")

def generate_random_countries():
    # generate random country names or codes
    rand_val = random.randint(1, 249)
    try:
        rand_val = random.randint(1, 249)
        country = countries_list[rand_val].name # .alpha_2 for code
        return country
    except IndexError:
        pass

columns = ['Order ID', 'Order Date', 'Country', 'Product', 'Price']


order_id = 1551086

product_list = [product for product in products]
weights = [products[product][1] for product in products]

for month_val in range(1, 13):
    if month_val <=10:
        orders = int(numpy.random.normal(loc=1200, scale=400))
    if month_val == 11:
        orders = int(numpy.random.normal(loc=2000, scale=300))
    if month_val == 12:
        orders = int(numpy.random.normal(loc=2500, scale=300))

    df = pd.DataFrame(columns=columns)
    for i in range(orders):
        date = generate_random_dates(month_val)
        country = generate_random_countries()
        product = random.choices(product_list, weights=weights)[0]
        price = products[product]
        df.loc[i] = [order_id, date, country, product, price[0]]

        order_id += 1

    month_name = calendar.month_name[month_val]
    print(month_name + ' finished...')
    df.to_csv(f'data/{month_name}_test_data.csv')

