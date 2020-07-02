#!/usr/bin/env python3
# report.py

# Import statements (libraries)
from fileparse import parse_csv
from stock import Stock
import tableformat

# Functions


def read_portfolio(filename):
    with open(filename, 'rt') as file:
        portdicts = parse_csv(
            file, select=['name', 'shares', 'price'], types=[str, int, float])
        return [Stock(s['name'], s['shares'], s['price']) for s in portdicts]


def read_prices(filename):
    with open(filename, 'rt') as file:
        pricelist = parse_csv(file, types=[str, float], has_headers=False)
        return dict(pricelist)


def make_report(portfolio, prices):
    report = []

    for s in portfolio:
        row = (s.name, s.shares,
               prices[s.name], prices[s.name] - s.price)
        report.append(row)

    return report


def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)

    print_report(report, formatter)


# Main function
def main(argv):
    portfolio_report(argv[1], argv[2], argv[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)
