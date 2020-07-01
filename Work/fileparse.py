# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None):
    '''
    Parse a CSV file into a list of records
    '''

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = [i for i, name in enumerate(headers)]

        if select:
            indices = [headers.index(name) for name in select]
            headers = select

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue

            row = [row[i] for i in indices]

            if types:
                row = [func(value) for func, value in zip(types, row)]

            record = dict(zip(headers, row))
            records.append(record)

    return records
