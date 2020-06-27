# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)  # header

        for row in rows:
            holding = {
                'name': row[0],
                'share': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        for row in rows:
            if row:
                prices[row[0]] = float(row[1])

    return prices


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
current_value = 0.0

for stock in portfolio:
    total_cost += stock['share'] * stock['price']

for stock in portfolio:
    price = prices[stock['name']]
    current_value += stock['share'] * price

print('Total cost', total_cost)
print('Current value', current_value)
print(f'Gain/Loss {current_value - total_cost:0.2f}')
