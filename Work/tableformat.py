
class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''

        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''

        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h:s}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d:s}</td>', end='')
        print('</tr>')


def create_formatter(name):
    formatters = {
        'txt': TextTableFormatter(),
        'csv': CSVTableFormatter(),
        'html': HTMLTableFormatter()
    }

    formatter = formatters.get(name)

    if not formatter:
        raise RuntimeError(f'Unknown format {name}')

    return formatter


def print_table(data, fields, formatter):
    formatter.headings(fields)

    for item in data:
        rowdata = [str(getattr(item, name)) for name in fields]
        formatter.row(rowdata)
