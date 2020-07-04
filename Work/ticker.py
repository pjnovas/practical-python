# ticker.py

from follow import follow
import csv
import report
import tableformat


def convert_types(rows, types):
    return ([func(val) for func, val in zip(types, row)] for row in rows)


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def select_columns(rows, indices):
    return ([row[index] for index in indices] for row in rows)


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def ticker(portfile, logfile, fmt):
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])

    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))

    holdings = (row for row in rows if row['name'] in portfolio)

    for stock in holdings:
        formatter.row(
            [stock['name'], f"{stock['price']:0.2f}", f"{stock['change']:0.2f}"])


if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
