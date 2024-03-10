# for loop list
fruits = ['Appels', 'Banana', 'Orange']

for fruit in fruits:
  print(f'I Love {fruit}')

# for loop range()
""" Syntax
range(start, stop, step)
"""
for number in range(10):
  print(number)

# Ini akan me-return 0 - 9 tidak termasuk 10
  
total = 0
for num in range(1, 101):
  total += num

print(total)