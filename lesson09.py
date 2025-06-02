count = 0
while (passwd := input("Введите пароль: ")) != "secret":
  print("Пароль неверный, попробуйте еще раз")
  count += 1
  if count == 5:
    print("Попытки закончились")
    break
else:
  print("Доступ разрешен")