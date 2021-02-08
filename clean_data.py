import pandas as pd
import os
import numpy
import pycountry
import random
import datetime
import calendar

#Task 1: Read in data
data = pd.read_csv('./data/all_mock_data.csv')

# Task 2: Get rid of any Nan
nan_df = data[data.isna().any(axis=1)]
data = data.dropna(how='all')

# Task 3: Correct column types
data['QuantityOrdered'] = pd.to_numeric(data['QuantityOrdered'])
data['Price'] = pd.to_numeric(data['Price'])

# Task 4: Add sales column
data['Sales'] = data['QuantityOrdered'] * data['Price']

# Task 5: Add month, day, and year columns
data['Month'] = data['OrderDate'].str[5:7]
data['Day'] = data['OrderDate'].str[8:10]
data['Year'] = data['OrderDate'].str[0:4]

data['Month'] = data['Month'].astype('int32')
data['Day'] = data['Day'].astype('int32')
data['Year'] = data['Year'].astype('int32')

# Task 4: Sort by date
data['OrderDate'] = pd.to_datetime(data['OrderDate'])
data = data.sort_values(by='OrderDate', ascending=True)
data.reset_index(inplace=False)

# Task 6: Export clean data as csv
data.to_csv('./data/clean_data/cleaned_data.csv', index=False)
print("clean_data.csv saved to ./data/clean_data/")
