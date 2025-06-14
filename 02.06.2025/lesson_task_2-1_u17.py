#01 Введите промокод
while promocode := input("Введите промокод: ") != "dixxy555":
  print("Промокод неверный. Попробуйте еще раз...")
print("Промокод принят!")

#02 Подсчет количество введенных слов
count = 0
while word_input := input("Введите слово: ") != "end":
  count += 1
print("Количество введенных слов: ", count)

#03 Регистрации участников
total = int(input("Введите кол-во участников: "))
participants = list()
for i in range(total):
  participants.append(input("Введите имя участника: "))
  print(f"Игрок {participants[i]} - зарегистрирован")
print("Все участники зарегистрированы")

#04 Четное не четное
while (number := int(input("Введите число: "))) != 0:
  if (number % 2) == 0:
    print("Да")
  else:
    print("Нет")
  
#05 Сумма чисел от 1 до 100
n = 100
sum100= 0
for i in range(1, n + 1):
  sum100 += i
print(f'Сумма чисел от {1} до {n}: {sum100}')
# вариант с формулой Гуасса n(n + 1)/2
print(f'Сумма чисел от {1} до {n}: {int((n * (1 + n)) / 2)}')

#06 таблица умножения
num = int(input("Введите число: "))
for i in range(1, 11):
  print(f'{num} x {i} = {num * i}')
  
#07 Факториал числа
count = (num := int(input("Введите число: "))) - 1
print("Факториал числа", num, "равен: ", end = "")
while count > 0:
  num *= count
  count -= 1
print(num)

#08 Каждая буква на новой страке
string = "hello"
count = 0
while count < len(string):
  print(string[count])
  count += 1

#09 среднее значение введенных чисел
num_list = list()
while (num := int(input("Введите число (0 для завершения): "))) != 0:
  num_list.append(num)
print(float(sum(num_list)) / len(num_list))

#10 Идентификация
count = 0
while (passwd := input("Введите пароль: ")) != "secret":
  print("Пароль неверный, попробуйте еще раз")
  count += 1
  if count == 5:
    print("Попытки закончились")
    break
else:
  print("Доступ разрешен")