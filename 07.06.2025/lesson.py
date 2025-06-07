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
  

