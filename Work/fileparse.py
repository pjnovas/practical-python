# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        indices = None
        rows = csv.reader(f, delimiter=delimiter)

        if has_headers:
            headers = next(rows)
            indices = [i for i, name in enumerate(headers)]

        if select:
            indices = [headers.index(name) for name in select]
            headers = select

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue

            if indices:
                row = [row[i] for i in indices]

            if types:
                row = [func(value) for func, value in zip(types, row)]

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records
