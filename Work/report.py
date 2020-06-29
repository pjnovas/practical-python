# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        header = next(rows)
        types = [str, int, float]

        return [
            {name: func(val) for name, func, val in zip(header, types, row)}
            for row in rows
        ]


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


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report:
        p = f'${price:>0.2f}'
        print(f'{name:>10s} {shares:>10d} {p:>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
