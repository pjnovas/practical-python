# pcost.py
#
# Exercise 1.27

import sys
from report import read_portfolio


def portfolio_cost(filename):
    'Returns the total cost of the entire portfolio'
    portfolio = read_portfolio(filename)
    return sum([s.cost for s in portfolio])


# Main function
def main(argv):
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f'Total cost {cost:0.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)
