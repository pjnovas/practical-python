# pcost.py
#
# Exercise 1.27

import sys
import csv


def portfolio_cost(filename):
    'Returns the total cost of the entire portfolio'

    f = open(filename, 'rt')
    rows = csv.reader(f)

    header = next(rows)

    total = 0
    for i, row in enumerate(rows, start=1):
        record = dict(zip(header, row))

        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total += nshares * price

        except ValueError:
            print(f'Row {i}: Bad Row: {row}')

    f.close()

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:0.2f}')
