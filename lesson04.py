first = 1
second = 100
"""
sum = 0
for i in range(first, second + 1):
  sum += i
print(f'Сумма чисел от {first} до {second}: {sum}')
"""
print(f'Сумма чисел от {first} до {second}: {int(((first + second) * second) / 2)}')