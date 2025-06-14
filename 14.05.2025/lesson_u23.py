#01 Две фунции, 1ое удваивает, 2ое проверяет яв-ся ли полиндр
def double_number(num):
  return num * 2
  
def is_polindrome(num):
  return str(num) == str(num)[::-1]

num = 103
double_res = double_number(num)
result = is_polindrome(double_res)
print(result)

#02 ends_with_vowel и add_suffix
def ends_with_vowel(word):
  return word[-1] in "AaEeIiOoUu"

def add_suffix(word):
  if ends_with_vowel(word):
    return word + "ly"
  else:
    return word[:-1] + "ily"

print(add_suffix("happy"))
print(add_suffix("blue"))

#03 площажь треугольника
def calculate_triangle_area(base, height):
  return (base * height) / 2

res = calculate_triangle_area(5, 10)
print(res)

#04 Годовая скидачная дисконт карта
def calculate_discount(price, discount_percentage):
  return price - price * (discount_percentage / 100)

def check_discount(price_amout):
  if price_amout <= 2350:
    print("Благодарим за покупку. Может в следующий раз:)")
  elif price_amout > 2350 and price_amout <= 8450:
    print("Вы были близки к получению нашей дисконт карты :(")
  elif price_amout > 8450:
    print("Поздравляю! Вы получили годовую скидочную дисконт карту для сети наших магазинов")
    
check_discount(calculate_discount(2350, 10))
check_discount(calculate_discount(8450, 5))
check_discount(calculate_discount(16750, 5))

#05 калькулятор индекса массы тела
def calculate_bmi(weight, height):
  return weight / (height ** 2)

def info_bmi(bmi):
  if bmi < 18.5:
    return "Недостаток веса"
  elif bmi >= 18.5 and bmi <= 24.9:
    return "Здоровый вес"
  elif bmi >= 25 and bmi <= 29.9:
    return "Присутствует избыточный вес"
  elif bmi >= 30 and bmi <= 34.9:
    return "Ожирение I типа"
  elif bmi >= 35 and bmi <= 39.9:
    return "Ожирение II типа"
  elif bmi > 40:
    return "Критично. Ожирение III типа"
    
bmi = calculate_bmi(85, 1.85)
print(info_bmi(bmi))
