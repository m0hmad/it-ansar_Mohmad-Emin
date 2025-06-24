#01 случайное число от 1 до 100
from random import randint
r = randint(1, 100)
print(r)

#02 Угадай случайное число
#from random import randint
r = randint(1, 50)
count = 0
while True:
  num = int(input("Угадай число от 1 до 50: "))
  if num > r:
    print("Загаданное число меньше")
    count += 1
  elif num < r:
    print("Загаданное число больше")
    count += 1
  else:
    break
print(f"Поздравляю! Вы угадали число {r} за {count + 1} попыток")
    
#03 Вывести время
from time import strftime
t = strftime('%H:%M:%S')
print(t)
 
#04 Ожидание заданное кол-во секунд
from time import sleep
s = int(input("Сколько секунд вы хотите подождать? "))
sleep(s)
print("Время вышло")

#05 дата и время в формате гггг-мм-дд и чч:мм:сс
from time import strftime

print(strftime("%Y-%m-%d"))
print(strftime("%H:%M:%S"))

#06 
#string_utils.py
def toggle_case(text):
  st = ''
  for ch in text:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      st += chr(ord(ch) + 32)
    elif ch in "abcdefghijklmnopqrstuvwxyz":
      st += chr(ord(ch) - 32)
  return st
  
def count_vowels(text):
  count = 0
  for ch in text:
    if ch in "AaEeIiOoUu":
      count += 1
  return count
  
def reverse_string(text):
  return text[::-1]
  
#main.py
import string_utils

text = input("Введите строку: ")
print("Измененный регистр:", string_utils.toggle_case(text))
print("Количество гласных букв:", string_utils.count_vowels(text))
print("Перевернутая строка:", string_utils.reverse_string(text))

#07 
from random import randint
from time import time, sleep

print("Готовтесь!")
r = randint(1, 5)
sleep(r)
start = time()
input("Нажмите Enter!")
end = time()
print(round(end - start, 2)

#08 
from random import randint
from time import time

def is_odd(num):
  num = num % 2
  return not num

def user_response(text):
  if text in 'четное':
    return True
  elif text in 'нечетное':
    return False

r = randint(1, 10)
start = time()
message = input("Четное или нечетное? (введи 'четное' или 'нечетное'): ")
if is_odd(r) == user_response(message):
  print(f"Число было {r}. Правильно!")
else:
  print(f"Число было {r}. Неправильно!")

end = time()
print(f"Тест занял {round(end - start, 2)} секунд.")

#09
#------------------------

#10
from random import randint
from time import time, sleep

start = time()
rand_dice = randint(1, 6)
num = int(input("Введите число от 1 до 6"))

if num == rand_dice:
  sleep(1.5)
  print(f"Выпала {rand_dice}, вы выйграли")
else:
  sleep(1.5)
  print(f"Выпала {rand_dice}, вы проиграли")
end = time()
print(f"Время игры: {round(end - start, 2)} сек.")
