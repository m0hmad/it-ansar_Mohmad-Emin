#01 Функция которая принимаяет имя и выводит приветствие
def greet(name):
  print(f"Привет, {name}!")
  
greet("Алиса")

#02 Ф. принимает число и выводит сообщение четное/нечетное
def is_even(number):
  if number % 2 == 0:
    print(f"Число {number} является четным")
  else:
    print(f"Число {number} является нечетным")

is_even(4)

#03 Ф. принимает три числа и выводит ср. арифметическое
def calculate_average(a, b, c):
  print(f"Среднее ариыметическое: {(a + b + c) / 3}")
  
calculate_average(10, 20, 30)

#04 Ф. пповеряет является ли строка полиндромом
def is_polindrome(word):
  if word.lower() == word[::-1].lower():
    print(f"Слова {word} является палиндромом")
  else:
    print(f"Слова {word} не является палиндромом")

is_polindrome("radar")
is_polindrome("hello")

#05 
def print_collatz_sequence(number):
  while number != 1:
    if number % 2 == 0:
      number = int(number / 2)
    else:
      number = (number * 3) + 1
    print(number)
  
print_collatz_sequence(13)

#06 Ф возврашает True если число четное, иначе False
def is_even(number):
  return number % 2 == 0
  
result = is_even(4)
print(result)

#07 Ф. возврашает количество гласных букв
def count_vowels(string):
  count = 0
  for char in string:
    if char in "AaOoEeIiUu":
      count += 1
  return count
  
result = count_vowels("hello")
print(result)

#08 площад треугольника по высоте и основанию
def calculate_triangle_are(base, heigth):
  return (base * height) / 2
  
base = 10
height = 5
result = calculate_triangle_are(base, height)
print(result)

#09 счастливый билет
def is_lucky_ticket(number):
  num_list = [number // 10 ** i % 10 for i in range(6)]
  return sum(num_list[:3]) == sum(num_list[3:])
  
ticket = 123321
result = is_lucky_ticket(ticket)
print(result)

#10 Magic date
def is_magic_date(day, month, year):
  return day * month == year
  
day = 10
month = 5
year = 50
result = is_magic_date(day, month, year)
print(result)

