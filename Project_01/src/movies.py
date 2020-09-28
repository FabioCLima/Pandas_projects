import pandas as pd 
import numpy as np
import os
import matplotlib.pyplot as plt
pd.options.display.max_columns = 30
pd.options.display.float_format = '{:.2f}'.format

script_address = os.path.join(os.path.abspath("."), 'src')
script_address = os.path.dirname(os.path.abspath(__file__))
project_address = os.path.dirname(script_address)
dados_address = os.path.join(project_address, 'data')
filepath_csv = os.path.join(dados_address, 'movies_complete.csv')
#df = pd.read_csv(filepath_csv, parse_dates=['release_date'])

df = (pd.read_csv("Project_01/data/movies_complete.csv", 
                  parse_dates=['release_date']))
print(df.info())
print(df.shape)
print(f'\nO nome das features do dataset:\n{df.columns}')

print(df.isnull().sum())

#  The  and the worst movies
#
print('\nFilter the dataset and find the best/worst n movies with')
print('Highest Revenue')
df_revenue = df['revenue_musd']
print(df_revenue.describe())
max_revenue = df_revenue.max()
min_revenue = df_revenue.min()

highest_revenue_movie = df[df['revenue_musd'] == max_revenue]['title']
print(f'\nHighest Revenue is {highest_revenue_movie}')

# Highest Budget
#
max_budget_movie = df['budget_musd'].max()
min_budget_movie = df['budget_musd'].min()
highest_budget = df[df['budget_musd'] == max_budget_movie]['title']
print(f"\nHighest Budget is {highest_budget}")

# Highest Profit
# 
df['profit'] = df['revenue_musd'] - df['budget_musd']
highest_profit = df['profit'].max()
highest_profit_movie = df[df['profit'] == highest_profit]['title']
print(f"\nThe Highest movie profit is, {highest_profit_movie}")

# Lowest profit
lowest_profit_=  df['profit'].min()
lowest_profit_movie = df[df['profit'] == lowest_profit_]['title']
print(f"The lowest profit movie is {lowest_profit_movie}")

# Highest Return on Investment
# (=Revenue/Budget)(only movies with Budget >= 10)
#
df_budget = df.query("budget_musd > 10")['budget_musd']
highest_return_on_investment = (df['revenue_musd']/df_budget).max()
print(f"Highest Return on Investment")


