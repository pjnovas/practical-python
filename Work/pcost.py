# pcost.py
#
# Exercise 1.27

import sys
import csv


def portfolio_cost(filename):
    'Returns the total cost of the entire portfolio'

    f = open(filename, 'rt')
    rows = csv.reader(f)

    next(rows)  # Read header

    total = 0
    for row in rows:
        try:
            total += int(row[1]) * float(row[2])
        except ValueError:
            print(f'missing value on line {row}')

    f.close()

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:0.2f}')
