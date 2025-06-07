# 01 
for i in range(1, 11):
  print(i)

# 02
word = input("Введите слово: ")
for char in word:
  print(char)

# 03
sum = 0
for i in range(100):
  sum += i
print(sum)

# 04
word = input("Введите слово: ")
count = 0
for char in word:
  if char in "AaEeIiOoUu":
    count += 1
print("Количество гласных:", count)

# 05
word = input("Введите слово:")
for i in range (0, len(word), 2):
  print(word[i])

# 06
count = 0
for i in range(1, 51):
  if i % 7 != 0:
    count += i:
print("Сумма чисел от 1 до 50, исключая кратные 7:", count)

# 07
num = int(input("Введите число: "))
fact = 1
for i in range(1, num + 1):
  fact *= i
print("Факториал числа", num, "равен:", fact)

# 08
sum_squares = 0
for i in range(1, 11):
  sum_squares += i ** 2
print(f"Сумма квадратов чисел от {1} до {10} равен: {sum_squares}")
