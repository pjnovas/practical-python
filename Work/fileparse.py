# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(iterable, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    '''
    Parse CSV iterable lines into a list of records
    '''
    if type(iterable) is str:
        raise RuntimeError(
            'iterable cannot be an string, filename paths are not supported')

    indices = None
    rows = csv.reader(iterable, delimiter=delimiter)

    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    if has_headers:
        headers = next(rows)
        indices = [i for i, name in enumerate(headers)]

    if select:
        indices = [headers.index(name) for name in select]
        headers = select

    records = []
    for index, row in enumerate(rows, start=1):
        if not row:    # Skip rows with no data
            continue

        try:
            if indices:
                row = [row[i] for i in indices]

            if types:
                row = [func(value) for func, value in zip(types, row)]

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f'Row {index}: Could not convert', row)
                print(f'Row {index}: Reason', e)

    return records
