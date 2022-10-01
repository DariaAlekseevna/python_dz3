# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math


data = list(map(float,input('введите список вещественных чисел через пробел: ').split()))
print(data)
data= list(map(lambda i:round(i - int(i), 4), data))
print(data)

max_n = data[0]
for i in range(1, len(data)):
    if max_n < data[i]:
        max_n = data[i]

print(max_n)
    
min_n = data[0]
for i in range(1, len(data)):
    if min_n > data[i]:
        min_n = data[i]

print(min_n)
print(f"разницa между максимальным и минимальным значением дробной части элементов: {max_n - min_n}")