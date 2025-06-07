# 01 Вывести числа от 1 до 10
for i in range(1, 11):
  print(i)

# 02 Вывести каждый символ на отдельной строке
word = input("Введите слово: ")
for char in word:
  print(char)

# 03 Суммирует числа от 1 до 100
sum = 0
for i in range(1, 101):
  sum += i
print(sum)

# 04 Подсчет количества гласных
word = input("Введите слово: ")
count = 0
for char in word:
  if char in "AaEeIiOoUu":
    count += 1
print("Количество гласных:", count)

# 05 Выводит символы на четных позициях
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

# 08 Сумма квадратов чисел от 1 до 10
sum_squares = 0
for i in range(1, 11):
  sum_squares += i ** 2
print(f"Сумма квадратов чисел от {1} до {10} равен: {sum_squares}")

# 09 Подсчет количества пробелов
string = input("Введите строку: ")
count = 0
for char in string:
  if char == " ":
    count += 1
print(f"Количество пробелов: {count}")

# 10 Вывести числа от 1 до 10 исключая 5
or i in range(1, 11):
  if i == 5:
    continue
  print(i)
