count = (num := int(input("Введите число: "))) - 1
print("Факториал числа", num, "равен: ", end = "")
while count > 0:
  num *= count
  count -= 1
print(num)
