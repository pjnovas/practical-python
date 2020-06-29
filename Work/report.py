# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        header = next(rows)
        types = [str, int, float]

        for row in rows:
            holding = {name: func(val)
                       for name, func, val in zip(header, types, row)}
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


def make_report(portfolio, prices):
    report = []

    for s in portfolio:
        row = (s['name'], s['shares'],
               prices[s['name']], prices[s['name']] - s['price'])
        report.append(row)

    return report


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)

for title in headers:
    print('-' * 10 + ' ', end='')
print()

for name, shares, price, change in report:
    p = f'${price:>0.2f}'
    print(f'{name:>10s} {shares:>10d} {p:>10s} {change:>10.2f}')
