# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num_n = int(input("Введите число : "))
degree = 0
while degree < num_n:
    if 2 ** degree < num_n:
        print(2 ** degree)
    degree += 1
