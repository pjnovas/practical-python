# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    'Returns the total cost of the entire portfolio'
    total = 0

    f = open(filename, 'rt')

    next(f)  # read header

    for line in f:
        row = line.split(',')
        try:
            total += int(row[1]) * float(row[2])
        except ValueError:
            print(f'missing value on line {line}')

    return total


# cost = portfolio_cost('Data/portfolio.csv')
# print(f'Total cost {cost:0.2f}')
