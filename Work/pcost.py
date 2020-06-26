# pcost.py
#
# Exercise 1.27

import csv


def portfolio_cost(filename):
    'Returns the total cost of the entire portfolio'
    total = 0

    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            total += int(row[1]) * float(row[2])
        except ValueError:
            print(f'missing value on line {row}')

    f.close()

    return total


# cost = portfolio_cost('Data/portfolio.csv')
# cost = portfolio_cost('Data/missing.csv')

# print(f'Total cost {cost:0.2f}')
