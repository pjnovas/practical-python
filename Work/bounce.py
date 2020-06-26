# bounce.py
#
# Exercise 1.5

height = 100

for bounce in range(10):
    height *= 3/5
    print(bounce + 1, round(height, 4))
