# Задание 1
a = int(input())
b = int(input())
if a < b:
  for i in range(a, b + 1):
    print(i)
elif b < a:
  for i in range(a, b - 1, -1):
    print(i)
elif a == b:
  print("")    
  
  
  
  # Задание 2
a = int(input())
b = int(input())
if (a > 999 and a < 10000) and (b > 999 and b < 10000) and a < b:
  for i in range(a, b + 1):
    y = i // 1000 
    g = (i // 100) % 10
    q = (((i // 10) % 100) % 10)
    r = (((i % 1000) % 100) % 10)
    if (y == r) and (q == g):
      print(i)
else:
  print("Введите два четырехзначных числа, первое меньше второго!")
  
  
  
  
  # Задание под звездочкой
a = int(input())
a = str(a) # переводим число в строку
b = a[::-1] 
if b == a:
  print("Является палиндромом")
else:
  print("Не является палиндромом")
