num_list = list()
while (num := int(input("Введите число (0 для завершения): "))) != 0:
  num_list.append(num)
print(float(sum(num_list)) / len(num_list))