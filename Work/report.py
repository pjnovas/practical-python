# report.py
#
# Exercise 2.4

from fileparse import parse_csv


def read_portfolio(filename):
    return parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(filename):
    pricelist = parse_csv(filename, types=[str, float], has_headers=False)
    return dict(pricelist)


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
