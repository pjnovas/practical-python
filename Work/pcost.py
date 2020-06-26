# pcost.py
#
# Exercise 1.27

total = 0

f = open('Data/portfolio.csv', 'rt')

next(f)  # read header

for line in f:
    row = line.split(',')
    total += int(row[1]) * float(row[2])

print(f'Total cost {total:0.2f}')
