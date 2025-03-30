# name = "Nick"
# print("Hello,", name, "!")
# age = 20
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# c = 5
# a = b
# print(id(a))
# print(id(b))
# print(id(c))
# from operator import index
# from turtledemo.sorting_animate import partition
# from operator import index
# from enum import unique
#   ----- множественное присваивание ------------
# from random import randint
# from itertools import count
# from email.charset import SHORTEST
# a = b = c = 6 # правильно
# d, f, r = 1 # это неправильно

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# name = 'Bob'
# print(name)

# name = "Nick"
# age = 20
# print('Меня зовут:', name,'. Мне', age, 'лет')  # проблема с точкой
# # print('Меня зовут: ' + name + '.Мне ' + age + 'лет')  # так нельзя
# print('Меня зовут: ' + name + '. Мне ' + str(age) + ' лет')

# a = 1
# b = 2
# print('a:', a)
# print('b:', b)
# # c = a
# # a = b
# # b = c
#
# # a, b = b, a
# a = a + b
# b = a - b
# a = a - b
# print('a:', a)
# print('b:', b)

# print("строка \
# символов")
# print('строка '
#       'символов')
#
# print("Документ 'script.py'")
# print("Документ \"script.py\" находятся по заданному пути \n \tD:\\\Python\project")

# s1 = "Hello"
# s2 = "Python"
# # print(s1 + ", " + s2 + "!")
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 3)
# print("*" * 15 )

# print(345689950494034954945)
# print(2.345689950494034954945)

# print(6 / 2)  # всегда вещественное число т.е. 3.0
# print(6//2)
# print(7//2)  # 3
# print(7%2)  # 1

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# a = 9753
# b = a % 10
# a //= 10
# c = a % 10
# a //= 10
# d = a % 10
# a //= 10
# e = a % 10
# print(b * 1000 + c * 100 + d * 10 + e )

# num = 4321
# res = (num % 10) * 1000
# num = num // 10
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += (num % 10)
# print(res)


# num1 = "2"
# num2 = 3
# num3 = "a"
# res1 = num1 + str(num2)
# res = int(num1) + num2
# # res2 = int(num3) + num2  # ошибка, не видит в "а" числа
# print(res1)
# print(res)
# print(res2)  #  ошибка

# print(int(3.8))
# print(round(3.8))
# print(round(3.896, 2))  # 3.90 ноль не виден и будет 3.9
# print(round(3.893, 2))  # 3.89

# a = 5 / 3
# print(a)
# print(round(a, 2))
# print(round(a, 6))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)
# print(int(float(a)) + b)

# a = 1
# b = 2
# print('a:', a,  'b:', b)
# print('a:', a, '\nb:', b)

# name = 'Виктор'
# age = 28
# print("Меня зовут", name, '. Мне', age, 'лет')
# print("Меня зовут " + name, '. Мне', age, 'лет')
# print("Меня зовут " + name + '. Мне ' + str(age )+ ' лет')
# print("Меня зовут ", name, '. Мне ', age, ' лет', sep='')
# print("Меня зовут", name, '. Мне', age, 'лет   ', sep=':', end='!!!')
# print("Меня зовут", name, '. Мне', age, 'лет', sep=':', end='\n\n ')
# print('Я учу Python.')
# print(5 + 2, 3 + 4, sep='******')


# name = input()  # так нельзя, нужно так
# name = input('Ваше имя: ')
# city = input("Ваш город: ")
# print((name, city))

# print('Маленький тест')
# num = input('Введите число: ')
# degree = input('Введите степень: ')
# print('Получили: ' + num + ' в степени ' + degree + ' равно: ' + str(int(num) ** int(degree)))

# print('Маленький тест')
# num = int(input('Введите число: '))
# degree = int(input('Введите степень: '))
# print('Получили: ' + str(num) + ' в степени ' + str(degree) + ' равно: ' + str(num ** degree))
# print('Получили:', num,  'в степени', degree,  'равно:', num ** degree)


# print('тест № 2')
# print("Введите четыре числа")
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c= int(input('Введите третье число: '))
# d = int(input('Введите четвёртое число: '))
# print('Результат: ', round((a + b) / (c + d), 3))


# a = True
# b = False
# print(a + 5)
# print(b + 5)
# print(bool('Python'))
# print(bool(''))  # False
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False
# print(bool(' '))  # True

# test = None
# test1 = None
# print(test, test1)

# print(7 == 3)  # False
# print('привет' == 'Привет')
# print('привет' > 'Привет')
# print(2 < 4 < 9)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False


# or логическое ИЛИ. False если False : False  остальные True
# and логическое И. True если True : True остальные False
# not логическое отрицание НЕ. меняет True на False и наоборот

# print(5 - 3 == 2 and 1 + 4 == 5)  # True(True : True)
# print(5 - 3 == 2 and 1 + 4 < 5)  #  False (True : False)
# print(5 - 3 > 2 and 1 + 4 < 5)  #  False (False : False)

# print(5 - 3 == 2 or 1 + 4 == 5)  # True(True : True)
# print(5 - 3 == 2 or 1 + 4 < 5)  #  True (True : False)
# print(5 - 3 > 2 or 1 + 4 < 5)  #  False (False : False)

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input('Введите свой возраст: '))
# if age >= 18:
#     print("Доступ разрешён")
# else:
#     print("Запрещено")

# a = 15
# b = 5
# if a > b:
#     print('a > b')
# elif a < b:
#     print('a < b')
# else:
#     print('b == a')  # else всегда относится к последнему if


# print('Определяем вид треугольника:')
# first_side = int(input('Введите первую сторону: '))
# second_side = int(input('Введите вторую сторону: '))
# third_side = int(input('Введите третью сторону: '))
#
# if (first_side + second_side <= third_side) \
#         or (first_side + third_side <= second_side) \
#         or (second_side + third_side <= first_side):
#     print('Такого треугольника не существует')
# elif first_side != second_side != third_side:
#     print('Треугольник разносторонний')
# elif first_side == second_side == third_side:
#     print('Треугольник равносторонний')
# else:
#     print("Треугольник равнобедренный")
# -----------------------------------------------------------------

# month = int(input('Введите номер месяца: '))
# if 12 >= month >= 1:
#     if 5 >= month >= 3:
#         print('Весна')
#     elif 6 >= month >= 8:
#         print('Лето')
#     elif 9 >= month >= 11:
#         print('Лето')
#     else:
#         print('Зима')
# else:
#     print('Такого месяца не существует')
# ------------------------------------------------------------------------

# day_week = int(input('Введите день недели (цифрой): '))
# if 1 <= day_week <= 5:
#     print("Рабочий день - ", end="")
#     if day_week == 1:
#         print("понедельник")
#     if day_week == 2:
#         print("вторник")
#     if day_week == 3:
#         print("среда")
#     if day_week == 4:
#         print("четверг")
#     if day_week == 5:
#         print("пятница")
# elif 6 <= day_week <= 7:
#     print("Выходной день - ", end="")
#     if day_week == 6:
#         print("суббота")
#     if day_week == 7:
#         print("воскресение")
# else:
#     print("Такого дня не существует")

# ----------------------------------------------------------------

# print('Считаем ворон')
# quantity = int(input('Сколько ворон Вы видите? (до 10 штук): '))
# if 1 > quantity > 10:
#     print('Неправильное количество')
# elif quantity ==1:
#     print("На ветке", quantity, "ворона")
# elif quantity == 2 or quantity == 3 or quantity==4:
#     print("На ветке",quantity, "вороны")
# else:
#     print("На ветке",quantity, "ворон ")

# # ---так не правильно, так как все elif будут работать

# print('Считаем ворон')
# quantity = int(input('Сколько ворон Вы видите? (до 10 штук): '))
# if 0 <= quantity <= 9:
#     print("На ветке ", end="")
#     if quantity == 1:
#         print(quantity, "ворона")
#     elif 2 <= quantity <= 4:
#         print(quantity, "вороны")
#     else:
#         print(quantity, "ворон")
# else:
#     print("Неправильное количество")


# _------ Тернарное выражение ------------------------

# number = 9
# abs_number = number if number > 0 else -number
# print(abs_number)

# a, b = 30, 20
# min_n = a if a < b else b
# print(min_n)

# a, b = 20, 20
# print('a == b' if a == b else "a > b" if a > b else 'b > a')

#  печатаем а == в, если они равны, иначе печатаем: а > в если это так,
#   а если не так, то печатаем в > а
#  в столбик то же самое:
# if a == b:
#     print('a == b')
# else:
#     if a > b:
#         print('a > b')
#     else:
#         print('b > a') `

# --------------------------------------

#  Проверка деления на ноль
# num1 = float(input("Введите делимое: "))
# num2 = float(input("Введите делитель: "))
#
# print(round(num1 / num2, 3) if num2 != 0 else "На ноль делить нельзя")


# ----------ИСКЛЮЧЕНИЯ--------------------------------------
# try:
#     n = int(input("Введите целое число"))
#     print(n * 2)
# except ValueError:
#     print('Что-то пошло не так')
# print('Код далее')

# --------------
# try:
#     n = int(input("Введите делимое целое число: "))
#     d = int(input("Введите делитель целым числом: "))
#     print(n / d)
# # except ValueError:
# #     print('нельзя вводить строки')
# # except ZeroDivisionError:
# #     print('на ноль делить нельзя')
# except (ValueError, ZeroDivisionError):
#     print('данные - это числа или на ноль делить нельзя')
# else:  # если не возникло исключений
#     print('всё корректно, Вы ввели', n, 'и', d)
# finally:  # выполняется в любом случае
#     print('Конец программы')
# -------------------------------------------


# n = input("Введите первое число: ")
# d = input("Введите второе число: ")
# try:
#     n = int(n)
#     d = int(d)
#     print(n + d)
# except ValueError:
#     n = str(n)
#     d = str(d)
#     print(n + d)
# можно короче

# try:
#     n = int(n)
#     d = int(d)
# except ValueError:
#     n = str(n)
#     # d = str(d)
# finally:
#     print(n + d)

# ---------------
# try:
#     print(int(n) + int(d))
# except ValueError:
#     print(str(n) + str(d))


# ----------------ЦИКЛЫ---------------------------------------

# i = 0
# while i < 5:
#     print('i =', i)
#     i += 1


# i = 10
# while i > 0:
#     print('i =', i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# ------------------------------------ряд звёздочек---

# row = input("Укажите количество символов: ")

# try:
#     n = int(row)
#     i = 0
#     while i < n:
#         i += 1
#         print('*' * i)
# except (TypeError, ValueError):
#     print("Количество символов это цифра")

#  ------------------------

# row = input("Укажите количество символов: ")
# try:
#     n = int(row)
#     i = 0
#     while i < n:
#         print('*', end='')
#         i += 1
# except (TypeError, ValueError):
#     print("Количество символов это цифра")

# row = input("Укажите количество символов: ")
# try:
#     n = int(row)
#     while n > 0:
#         print('*', end='')
#         n -= 1
# except (TypeError, ValueError):
#     print("Количество символов это цифра")

#  ----------------------------------------

# print("Считаем сумму нечётных чисел в диапазоне")
# start = input("Введите начало диапазона числом: ")
# finish = input("Введите конец диапазона числом: ")
# su_m = 0
# try:
#     a = int(start) if start < finish else int(finish)
#     b = int(finish) if start < finish else int(start)
#     while a <= b:
#           # = if a% 2:
#         su_m += a if a % 2 != 0 else 0
#         a += 1
#     print("Сумма нечётных чисел:", su_m)
# except ValueError:
#     print("Введённые параметры должны быть целыми числами")
#  -------------------------------------------------------------

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print(""
#           "чётное")
# else:
#     print("Нечётное")
# ---------------------------------------------------------------
#                -break-   -continue-

# i = 0
# while i < 10:  # или while True
#     if i == 2:
#         i += 1
#         # continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")
# ------------------------------------------------------

# while True:
#     n = int(input("Введите положительное число: "))
#     if n > 0:
#         break

# -----поиск произведения последовательности чисел-----------

# print("    Введённый ноль останавливает работу и выводит произведение чисел")
# digit = 1
# while True:
#     n = float(input("Введите любое число: "))
#     if n == 0:
#         break
#     digit *= n
# print("Произведение равно:", digit)
# ------------------------------------------------------

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:  # отработает, если цикл не прервался
#     print("Цикл окончен", "i =", i)
# -----------------------------------------------

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВложенный цикл: j =", j)
#         j += 1
#     i += 1
# ----------------------------------------------------

#            -Таблица умножения---

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end= "\t\t")
#         j += 1
#     print()
#     i += 1
# --------------------------------------------------------
#   --------    прямоугольник из символов
#   ------------------------

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("0", end="  ")
#         j += 1
#     print()
#     i += 1

# ---------- прямоугольник из чередующихся символов

# i = 0
# while i < 5:
#     j = 0
#     while j < 10:
#         if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
#             print("0", end=" ")
#         else:
#             print("+", end= " ")
#         j += 1
#     print()
#     i += 1
# ------------------------------------

# for element in collection:
#     print(element)

# for i in "Hello":
#     print( i)

# for color in 'red', 'orange', 'yellow', 8, 5.6:
#     print('color:', color, type(color))


# for i in range(n):
#     Тело цикла

# print(range(9))

#  range(start, stop, step)

# for i in range(2, 9, 3):
#     print(i, end=" ")

# print()
# j = 2
# while j < 9:
#     print(j, end=" ")
#     j += 3

# for i in range(9, -1, -1):
#     print(i, end=" ")
# print()
# for i in range(100, 0, -10):
#     print(i, end=" ")
# ---------------------------------------

#             про целые делители числа без остатка
# digit = input("Введите целое число: ")
# try:
#     num = int(digit)
#     for i in range(1, num + 1):
#         if num % i == 0:
#             print(i, end=' ')
# except ValueError:
#     print("целое число")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
# else:
#     print('done')

# -----------------------------------

# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('--' )


# -----------------------------------------
#         прямоугольник из звёздочек

# long = input("Введите длину прямоугольника: ")
# elevation = input("Введите высоту прямоугольника: ")
# try:
#     lon = int(long)
#     el = int(elevation)
#     for i in range(el):
#         print("o" * lon)
# except ValueError:
#     print("long  и elevation целые числа")
# ----------------------------------------------

#                ещё один прямоугольник

# a = int(input('ширина: '))
# b = int(input('высота: '))
# for i in range(b):
#     if i == 0 or i == (b - 1):
#         print('*' * a)
#     else:
#         print('*', ' ' * (a - 2), '*', sep='')
#     ещё один вариант

# for i in range(b):
#     for j in range(a):
#         if i == 0 or j == 0 or i == b - 1 or j == a - 1:
#             print("*", end='')
#         else:
#             print(' ', end='')
#     print()
# -----------------------------------------------

# print('          Нечётные в диапазоне')
# start_diapason = int(input('Введите начало диапазона: '))
# finish_diapason = int(input('Введите конец диапазона: '))
# for i in range(start_diapason, finish_diapason +1):
#     if i % 2 != 0:
#         print(i, end=' ')
# --------------------------------------

# ---------------- Угадай число -------------------
# print('                Угадай число')
# sought_for = 49
# count_num = 1
# x = int(input('Назовите число: '))
# while True:
#     if x == 0:
#         break
#     if x == sought_for:
#         print('Вы угадали с', count_num, 'попытки')
#         break
#     else:
#         if x < sought_for:
#             print('Это число меньше. ',end='')
#             x = int(input('Назовите число: '))
#             count_num += 1
#         elif x > sought_for:
#             print('Это число больше. ', end='')
#             x = int(input('Назовите число: '))
#             count_num += 1
# print('Количество попыток:', count_num)
# --------------------------------------------

#       Перемена полей одного на другое--------------

# size = int(input('Введите размер поля: '))
# symbol = int(input('Введите количество символов: '))
# for i in range(5):  # кол-во общих рядов (строк)
#     for j in range(3):  # кол-во рядов (строк) звёздочек или пробелов
#         for n in range(5): #  кол-во общих столбцов
#             for m in range(3):  # число символов в малёньких рядах
#                 #   print(" " if (i + n) % 2 else "*", end='')
#                 if (i + n) % 2 == 0:
#                     print("*", end="")
#                 else:
#                     print(" ", end="")
#         print( )
# --------------- 9-я пара -------------------

# a = [letter * 2 for letter in 'Hello']
# print(a)


# num = [i for i in range(30) if i % 2 == 0]
# print(num)

#  СПИСКИ !!! [LIST] !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# num = [8, 3, 'one', 3.4, [1, 2, 3]]
# print(num, type(num))
# print(num[4][1])  # 2
# print(num[-1][1])  # 2
# num[2] = 256
# print(num, id(num))
# num[1] += 100
# print(num, id(num))
# print('Длина списка: ', len(num))

# s = []
# print(type(s))
# b = list()
# print(b)

# s = [5, 1 ] * 6
# print(s, id(s))

# n = range(10)
# print(n)
# n = list(range(10))
# print(n)

# n = list(range(2, 10, 2))
# print(n, id(n))
# n2 = [2, 4, 6, 8]
# print(n2, id(n2))
# if n == n2:
#     print("=")
# else:
#     print('!=')

#  [выражение for переменная in последовательность]

# a = [0 for i in range(5)]  # == [0 for _ in range(5)]
# print(a)  # [0, 0, 0, 0, 0]
# #  если вместо 0 применяем i, то _ использовать нельзя

# n = 5
# a = [i ** 2 for i in range(n) if i % 2 == 0]
# print(a)

# a = [1, 2, 3]
# b = [5, 6]
# c = a + b
# d = b + a
# f = c * 2
# print(c)
# print(d)
# print(f)

#  --------------     10-я пара ------------------------------

# Ввод списков с клавиатуры -----------------
# a = [0] * int(input('Введите количество элементов списка: '))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('-> '))
# print(a)

# a = [input("-> ") for i in range(int(input('Введите кол-во эл-тов списка: ')))]
# print(a)

# a = [4, 8, 9, 3, 2]
# for i in range(len(a)):
#     print(a[i], end=' ')

# lst = ['один', 'два', 'три']
# for elem in lst:
#     print(elem, end=' ')
# print()
# for i in range(len(lst)):
#     print(i, end=' ')
#     print(lst[i], end=' ')
# ------------------------------------------

# n = 0
# lst = [int(input('->')) for i in range(int(input('Кол-во: ')))]
# for elem in lst:
# #     # if elem < 0:
# #     #     n += elem
#     n += elem if elem < 0 else 0
# print('Сумма: ', n)

# lst = list(range(21, 41))
# k = s = 0
# for i in lst:
#     k += 1 if i % 2 == 0 else 0
#     s += i if i % 2 != 0 else 0
# print('Кол-во чётных:', k, '\nСумма отрицательных:', s)
# -------------------------------------

#  ========= Среднее арифметическое ==============
# summa = 0
# lst = [(input('->')) for i in range(int(input('Кол-во: ')))]
# quantity = len(lst)
# try:
#     for i in lst:
#         i = int(i) or float(i)
#         quantity -= 1 if i <= 0 else 0
#         summa += i
#     print('Среднее арифметическое: ', summa / quantity)
#
# except (ValueError, ZeroDivisionError):
#     print('Значения должны быть числами  и не все быть нулями')

#  =========== Элементы с чётными индексами ===========
# lst = [(input('->')) for i in range(int(input('Введите кол-во элементов : ')))]
# for i in range(len(lst)):
#     if i % 2 == 0:
#         print(lst[i], end=' ')

# for i in range(0, len(lst), 2):
#     print(lst[i], end=' ')
#  --------------------------------------------

# a = [7, 8, 2, 1, 17]
# a[0], a[-1] = a[-1], a[0]
# print(a)

# -----------------DZ -----------
# s = [2, 9, 4, 6, 3, 5, 6, 8]
# for i in range(len(s) - 1):
#     if  s[i] < s[i + 1]:
#         print(s[i + 1], end=' ')
# ----------------------------------

# !!!!!!!!!!!!!!!!! СРЕЗЫ --------------------

#  список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[1:4:2])
# print(s[:2])
# print(s[::2])
# print(s[-2:2:-1])  # 1, 7

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[::])  #  print(s[:])
# print(s[-1::-1])  #  print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[::7])  # print(s[:1])
# print(s[-1:7])  # print(s[-1:])
# print(s[-3::])
# print(s[-3:1:-1])
# print(s[2:-2])  # print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# s[1:3] = [0, 0, 0]
# print(s)

# ============= МЕТОДЫ СПИСКОВ =================

# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
#
# # s.extend((9, 8, 7))  #   добавляет множество элементов в конец списка
# s.extend([9, 8, 7])  #   добавляет множество элементов в конец списка
# s.extend(list('ad d'))
# print(s)
# s.insert(1, 100)
# print(s)

# s = []
# s.extend([i ** 2 for i in range(1, 11)])
# print(s)
#  ---------------------------------

# lst = []
# n = int(input('Кол-во эл-тов списка: '))
# for num in range(n):
#     x = int(input('Введите число: '))
#     # lst.append(x)
#     # lst.extend([x])
#     # lst.insert(-1, x)  # insert нельзя добавлять в конец списка
# print(lst)
# -----------------------------------------

#  кратность трём
# lst = [(input('->')) for i in
#        range(int(input('Введите кол-во элементов : ')))]
# lst = []
# part = int(input('Введите кол-во элементов : '))
# for i in range(part):
#     number = int(input('Введите число кратное трём: '))
#     if number % 3 == 0:
#         lst.append(number)
#     else:
#         print(number, 'не делится на три без остатка')
# print(lst)

#  ещё вариант
# part = int(input('Введите кол-во элементов : '))
# i = 0
# lst = []
# while i < part:
#     number = int(input('Введите число кратное трём: '))
#     if number % 3 != 0:
#         print(number, 'не делится на три без остатка')
#     else:
#         lst.append(number)
#     i += 1
# print(lst)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# for i in a:
#     for j in b:
#         if i == j:
#             if i not in c:
#                 c.append(i)
#
# print(c)
# -----------------------------------------------

#      комбинация двух списков
# sps = [1, 2, 3, 4]
# lst = [11, 22, 33]
# sp = []
# l = len(sps) if len(sps) <= len(lst) else len(lst)
# m = len(lst) if len(lst) > len(sps) else len(sps)
# for i in range(l):
#     sp.extend((sps[i], lst[i] ))
#     # sp.append(sps[i])
#     # sp.append(lst[i])
# for j in range(l, m):
#     if len(sps) > len(lst):
#         sp.append(sps[j])
#     else:
#         sp.append(lst[j])
#
# print(sp)
# ------------------------------------------------------

# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(id(s))
# s[4:] = []
# s.remove(0)  # удаляет первое совпадение
# s[2:6] = []

# pop - удаляет последний эл-т списка(по умолчанию) и возвращает удаляемый эл-т

# last = s.pop()
# print(last)
# second = s.pop(-2)
# print(second)
# print(s, id(s))

# s.clear()  # очищает весь список
# print(s)

# del  s[2]  # удаляет по индексу
# print(s)
# --------------------------------------------

#      Задача про удаление -------------------

# lst = [(int(input('-> '))) for i in
#        range(int(input('Введите кол-во элементов : ')))]
# print("Список: ", lst)
# k = int(input('Введите индекс удаляемого элемента: '))
# if 0 <= k <= len(lst):
#     lst.pop(k)
#     print("Изменённый список: ", lst)
# else:
#     print('Такого индекса нет')
# --------------------------------------------

# print(dir(list))
# s = [1, 20, 0, 4, 0, 5, 6, 7, 0, 2]
# num = s. count(0)
# print(num)

# ind = s.index(0, 0, -1)
# print(ind)

# x = 0
# for i in  range(len(s)):
#     if s[i] == x:
#         print(i)
# ----------------------------

# a = [1, 2, 3]
# b = a
# s_copy = a.copy()
# print('a =', a, id(a))
# print('b =', b, id(b))
# print('s_copy =', s_copy, id(s_copy))
#
# a.append(20)
# print('a =', a, id(a))
# print('b =', b, id(b))
# print('s_copy =', s_copy, id(s_copy))
#
#
# b.append(30)
# print('a =', a, id(a))
# print('b =', b, id(b))
# print('s_copy =', s_copy, id(s_copy))
# ---------------

# s = [1, 20, 0, 4, 0, 5, 6, 7, 0, 2]
# s.reverse()
# print(s)
#
# s.sort()
# print(s)
# s.sort(reverse=True)  # reverse=True - это сортировка по убыванию
# print(s)
# -----------------------

# s2 = ['Виталий', 'Сергей', 'Александр', 'Анна']
# print(s2)
# s2.sort()
# print(s2)
#
# s2.sort(key=len)  # по длине элементов списка
# print(s2)
#
# s2.sort(reverse=True)
# print(s2)
# print(sorted(s2))
# sps = sorted(s2)
# print(sps)
# ------------------------------------------

#  ------ ГЕНЕРАЦИЯ СЛУЧАЙНЫХ ДАННЫХ  !!!!!!!!!!!!!!!!

# import random as r
# from random import randint, randrange
# from random import *

# print(r.random())
# print(randint(0, 9))  # 9 включается
# print(randrange(0, 10, 2))  # 10 не включается
# print(round(uniform(10.5, 25.5), 2))

# s =[55, 66, 77 , 88, 99, 20, 30, 80, 90]
# # print(choice(s))  # одно значение из списка
# # print(choices(s, k=5))  # k- значений из списка, может одинаковых
#
# print(s)
# shuffle(s)
# print(s)

# mas = [randint(0, 100) for i in range(10)]
# mas2 = [uniform(0, 100) for j in range(10)]
#
# print(mas)
# print(mas2)


# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(sum(lst))  # только с числами
# print(min(lst))
# print(max(lst))
# ----------------------------

#  задача
# sps = [randint(0, 100) for i in range(11)]
# print(sps)
# m = max(sps)
# sps.remove(m)
# sps.insert(0, m)
# print('Max:', max(sps))
# z = sps.pop(sps.index(max(sps)))
# sps.insert(0, z)
# print(sps)
# -------------------------------------

#  сортировка с разворотом
# sp = [randint(-20, 20) for n in range(11)]
# print(sp)
# sp_sort = sorted(sp, reverse=True)
# print(sp_sort)
# sp.sort(reverse=True)
# print(sp)
# -----------------------

# sp = [randint(0, 100) for n in range(11)]
# print(sp)
# z = sp.index(min(sp))
# print('Min: ', sp[z])
# print('Index min: ', z)
# sp_d = sp[z:]
# del sp[:z]
# print(sp)
# print(sp_d)
# -----------------------

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)  #True
# print('a' not in x)  #False

# lst = []
# # if len(lst) == 0:
# #     print('Список пустой')
# print(bool(lst))
# if not lst:
#     print('Список пустой')
# ---------------------------------

# size_1 = int(input('Обозначьте размер первого списка: '))
# size_2 = int(input('Обозначьте размер второго списка: '))
# sps_1 = [randint(0, 10) for i in range(size_1)]
# sps_2 = [randint(0, 10) for j in range(size_2)]
# print('Первый список:', sps_1)
# print('Второй список:', sps_2)
# general_sp = sps_1 + sps_2
# print('Общий список:', general_sp)
# no_repeat = []
# for a in general_sp:
#     if a not in no_repeat:
#         no_repeat.append(a)
# print('Общий список без повторений:', no_repeat)
# all_el =[]
# for k in sps_1:
#     if k in sps_2 and k not in all_el:
#         all_el.append(k)
# print('Общие элементы списков:', all_el)
# mn_mx = [min(sps_1), max(sps_1), min(sps_2), max(sps_2)]
# print('Min_Max:', mn_mx)
# ----------------------------------------

# Список уникальных случайных чисел
# len_sps = int(input('Введите длину списка: '))
# un_iq_ue = []
#
# # while len(un_iq_ue) < len_sps:
# #     i = randint(0,len_sps - 1)
# #     if i not in un_iq_ue:
# #         un_iq_ue.append(i)
# # print(un_iq_ue)
#
# s = [i for i in range(1, len_sps + 1)]
# shuffle(s)
# print(s)
# ---------------------------------

#    МАТРИЦЫ   !!!!
# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
# print(m)
# print('m[1][2] = ' ,m[1][2])
#
# # for row in range(len(m)):
# #     # print(m[row])
# #     for col in range(len(m[row])):
# #         print(m[row][col], end=' ')
# #     print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end='\t')
#     print()
# ------------------------------

#  Каждый элемент матрицы в квадрат
# matr = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# for sp in matr:
#     for el in sp:
#         print(el, end='\t')
#     print()
# print()
#
# q = [[el ** 2 for el in sp]for sp in matr]
# print(q)
# print()
# for sp in matr:
#     for el in sp:
#         print(el ** 2, end='\t')
#     print()
# -------------------------------------

#  Задача: сетка из символов
# st_r = int(input('Кол-во строк, (высота): '))
# ro_w = int(input('Кол-во рядов: '))
# symbol = input('Из каких символов будем делать сетку: ')

# for i in range(st_r):
#     for j in range(ro_w):
#         print(symbol, end=' ')
#     print()

# matr = [[symbol for  i in range(ro_w)] for j in range(st_r)]
# for x in matr:
#     for y in x:
#         print(y, end='\t')
#     print()
# ------------------------------------

# for x, y in [[1, 2],[3, 4], [5, 6], [7, 8]]:
#     print(x, y, '\t', x , '+', y, '=', x + y)
# ---------------------------------

# from random import randint, randrange

# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# ------------------------------------------

#   кол-во ненулевых эл-тов
# w, h = 3, 4
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# quantity_negative_int = 0
# for row in matrix:
#     for x in row:
#         if x < 0:
#             quantity_negative_int += 1
#         print(x, end='\t\t')
#     print()
# print('Отрицательных чисел:', quantity_negative_int)
# ----------------------------------

#  Произведение ненулевых эл-тов

# w, h = 3, 4
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# work = 1
# for row in matrix:
#     for x in row:
#         if x != 0:
#             work *= x
#         print(x, end='\t\t')
#     print()
# print('Произведение положительных чисел:', work)
# --------------------------------

#   Поменять местами строки
# w, h = 6, 6
# matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#     print()
# print()
# for i in range(len[matrix]):
#     if i % 2 == 0:
#         matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
#     for x in matrix[i]:
#         print(x, end='\t\t')
#     # print(matrix[i])
#     print()

# -- вариант
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         for col in range(len(matrix[row])):
#             print(matrix[row + 1][col], end='\t')
#         print()
#         for col in range(len(matrix[row])):
#             print(matrix[row][col], end='\t')
#         print()
# -----------------------------------------------------------

#  модуль MATH
# import math

# print(dir(math))
# num1 = math.sqrt(2)
# print(num1)  # будет корень из двух
#
# num2 = math.ceil(num1)  # округление вверх
# print(num2)
#
# num3 = math.floor(num1)  # округление вниз
# print(num3)
#
# print(math.pi)  # число пи

# radius = 2
# print('площадь с радиусом',radius, '=>', math.pi * radius ** 2)

# radius_circle = 9
# print('Длина окружности:', round(2 * math.pi * radius_circle, 2))

# import time

# print(dir(time))

# second = time.time()
# print('Секунды с 1-го января 1970-го года:', second)
# localtime= time.ctime(second)
# print(localtime)
#
# res = time.localtime(second)
# print(res)
# print(res.tm_year)
# print(time.strftime('Today is %B %d, %Y, %Z'))
# print(time.strftime(' %m/%d/%Y, %H:%M:%S, %Z'))

# pause = 6
# print('Program started...')
# time.sleep(pause)
# print('Прошло', pause, 'sec')

# text = input('Название напоминания: ')
# local_time = float(input('Через сколько минут: '))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# ---------------
# start = time.monotonic()
# time.sleep(5)
# # finish = time.time()
# finish = time.monotonic()
# res = finish - start
# print(res)
# # start = time.time()

# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime('Сегодня: %B %d, %Y, %Z'))


#    ---------- ФУНКЦИИ ------------------------------


# def hello(name, word):
#     print('Hello', name)
#     print('Hello', name, word)
#
# hello('Irina', 'hi')


# def get_summ(a, b):
#     print(a + b)
#
# get_summ(2, 5)


# def simba(a, b, count):
#     # print((a + b ) * count + a)
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#
# simba('X', 'O', 7)


# def get_summ(a, b):
#     return a + b
#
# x = 2
# y = 5
# res = get_summ(x, y)
# print(res)
# print(get_summ(1, 9))


# def max_min(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
# print(max_min(2, 8))
# -------------------------------


# num1 = int(input('Первое число: '))
# num2 = int(input('Второе число: '))
#
# def sum_dif(numb1, numb2):
#     if numb1 > numb2:
#         return 'Разность чисел: ', numb1 - numb2
#     else:
#         return "сумма чисел: ", numb2 + numb1
#
#
# print("Результат: ", sum_dif(num1, num2))


# def change_lst(lst):  # ф-ция меняет местами 1-й и последний эл-т
#     for el in lst:
#         z = el[0]
#         y = el[-1]
#         el[0] = y
#         el[-1] = z
#         print(el)
#     print()


# change_lst(l)


# def change_lst(lst):  # ф-ция меняет местами 1-й и последний эл-т
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
# print(change_lst([1, 2, 3]))
# print(change_lst([9, 12, 33, 54, 105]))
# print(change_lst(['c', 'л', 'о', 'н']))


# def change_lst(lst):  # ф-ция меняет местами 1-й и последний эл-т
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
# print(change_lst([1, 2, 3]))
# print(change_lst([9, 12, 33, 54, 105]))
# print(change_lst(['c', 'л', 'о', 'н']))

# ------------------------------------

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))

# ------------------------------


# def check_password(password):  # проверка пароля
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Надёжный пароль')
# else:
#     print("Ненадёжный пароль")
# ---------------------------------------------------------------


# def get_sum(a, b, c=0, d=1):  # d - это именованный параметр
#     return a + b + c + d
#
#
# print(get_sum(1, 4, 3, 5))
# print(get_sum(4, 5, 6))
# #  именованных параметров может быть несколько
# print(get_sum(1, 5, d=9))
# -------------------------------------------

# def num_sim(n=20, s='-'):  # сколько каких символов
#     return n * s
#
# print(num_sim(9, "+"))
# print(num_sim(4, "*"))
# print(num_sim(12, "#"))
# print(num_sim())
# -----------------------------------


# def even_odd(z, even=True):
#     even_sum = 0
#     while z > 0:
#         cur_digit = z % 10
#         if even and cur_digit % 2 == 0:
#             even_sum += cur_digit
#
#         elif not even and cur_digit % 2 != 0 :
#             even_sum += cur_digit
#         z //= 10
#     return even_sum
#
# # print('Сумма чётных: ')
# # print(even_odd(9874023))
# # print(even_odd(38271))
# # print(even_odd(123456789))
# print('Сумма нечётных: ')
# # print(even_odd(9874023, even=False))
# # print(even_odd(38271, even=False))
# print(even_odd(123456789, even=False))
# -------------------------------------------------------

# def display_info(name, age):
#     print('Name:', name, '\nAge:', age)
#
#
# display_info('Ira', 23)
# display_info(23, 'Ira')
# display_info(age=23, name='Ira')
# -------------------------------------------


#    !!! СТРОКА - ЭТО НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ

# s = 'Hello'
# print(id(s))
# s += 'World'
# print(id(s))
# # s[1] ='a'


#           КОРТЕЖ - НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)
# a = 1, 2, 3, 4, 5
# print(type(a))
# b = tuple((1, 2, 3, 4, 5))
# print(type(b))
#
# c = tuple('Hello')
# print(c)


# t = (1,)
# print(t)
# print(type(t))


# b = tuple((1, 2, 3, 4, 5))
# print(b)
# print(b[2])
# print(b[1:3])


# s = [int(input('-> ')) for i in range(3)]  # list
# print(s)
# s = ([int(input('-> ')) for i in range(3)])  # list
# s1 = tuple(int(input('-> ')) for j in range(3))  # tuple
# print(s1)
# print(type(s1))
# s3 = list(s1)
# print(s3)
# print(type(s3))

# d = input('Строка: ')
# a = tuple(d)
# print(a)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
# print(tuple(randint(0, 100) for _ in range(10)))
# -------------------------------


# from random import choice
#
# z = [2 ** i for i in range(1, 13)]
# ch = choice(z)
# b = [ choice([2 ** i for i in range(1, 13)]) for j in range(10)]
# print(z)
# print(ch)
# print(b)
# #  доработать сделал
# ---------------------------------

# t1 = tuple('Hello')
# t2 = tuple('World')
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.index('l'))
# print(t3.index('l', 3))
#
# for i in t3:
#     print(i, end=' ')


# from random import randint
#
#
#
# lst_for_tuple = [randint(1, 26) for j in range(10)]
# task_for_tuple = (tuple(lst_for_tuple), randint(2, 26))
# print(task_for_tuple)
# print(task_for_tuple[-1])
# print(task_for_tuple[0])
# tps = task_for_tuple[0]
# r_el = task_for_tuple[-1]
#
#
# def slicer(tp, rel):
#     """ Сравниваем элементы по индексам, и по результатам сравнения
#     определяем, что пойдёт в return"""
#     if rel in tp:
#         z = tp.index(rel)
#         if tp.count(rel) == 1:
#             if z == -1:
#                 return tuple(rel)
#             else:
#                 return tuple(tp[z:])
#         else:
#             z2 = tp.index(rel, z + 1) + 1
#             return tuple(tp[z:z2])
#     else:
#         return []
#
#
# # print(slicer(tps, r_el))
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8,9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# -----------------------------------------------------------

# lst_for_tuple = [choice([i for i in range(0, 5)]) for j in range(10)]
# print(lst_for_tuple)

# def func_for_tuple(a, b, c):
#     """Заполняем кортеж случайными числами"""
#     # return tuple(choice([i for i in range(a, b)]) for _ in range(c))
#     return tuple(randint(a, b) for _ in range(c))
#
# tuple_1 = func_for_tuple(0, 6, 10)
# tuple_2 = func_for_tuple(-5, 1, 10)
# tuple_3 = tuple_1 + tuple_2
#
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print("Кол-во нулей:", tuple_3.count(0))
# --------------------------------------

# число в строку и наоборот
# a = 123456
# s = str(a)
# lst = list(s)
# print(lst)
#
# str_1 = ''
# for j in range(len(lst)):
#     str_1 += lst[j]
# print(str_1, type(str_1))
# num = int(str_1)
# print(num, type(num))
# --------------------------------

# tup = (10, 11, [1, 2, 3], (4, 5, 6), ['Hello', 'World'])
# print(tup, id(tup))
# tup[-1][0] = 'First'
# print(tup, id(tup))
# tup[4].append('new')
# print(tup, id(tup))
# ------------------------------


# def reverse_list(lst):
#     """Разворачиваем и ищем уникальные, на выходе - кортеж """
#     sps = []
#     # lst.reverse()
#     # for elem in lst:  # lst[::-1], тогда reverse() не нужен
#     #     if elem not in sps:
#     #         sps.append(elem)
#     [sps.append(i) for i in lst[::-1] if i not in sps]  # reversed(lst)
#     return tuple(sps)
#
#
# list_1 = [1, 2, 3, 3, 2]
# list_2 = [2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]
# print(reverse_list(list_1))
# print(reverse_list(list_2))
# ------------------------------------------


# ===========  РАСПАКОВКА КОРТЕЖА  =================

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)


# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# user = get_user()
# print(user)
# print(user[0])
# name1, age1, is_user1 = user
# print(name1)


# a = (1, 2, 3)
# # del a
# print(a, id(a))
# lst = list(a)
# print(lst)
# tpl = tuple(lst)
# print(tpl, id(tpl))
# ---------------------------------------


# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
# # print(countries)
#
# for country in countries:
#     # print(country)
#     country_name, country_population, cities = country
#     print('\nСтрана:', country_name + ",", "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население =", city_population)


# --!!!--- МНОЖЕСТВО --------- SET --------

# s = {'banana', 'apple', 'orange', 'apple'}
# print(type(s))
# print(s)

# a = ()  # кортеж
# a1 = set()  # множество
# print(type(a))

# list_sp = ['Hello', 'world']
# set_s = set(list_sp)
# print(set_s)
# -------------------------------------

# sps = [x for x in range(10)]
# set_x = {x for x in range(10)}
# set_sq = {x * x for x in range(10)}
# print(sps)
# print(set_x)
# print(set_sq)
# --------------------------------------

# num = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# set_num = set(num)
# print(set_num)
# list_num = list(set(num))
# print(list_num)
# -------------------------------

#  Функция: из строки множество и длина множества

# def str_set(argument):
#     return set(argument), len(set(argument))
#
#
# str_ing = 'я обычная строка'
# list_num = [4, 5, 6, 2, 9, 11, 3, 4, 2]
#
# print(str_set(str_ing))
# print(str_set(list_num))
# ----------------------------------------

# set_color = {'red', 'green', 'blue'}
# # print('green' not in set_color)
# for color in set_color:
#     print(color, end='  ')
# ---------------------------------------

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in r if 'a' not in i}
# # a = {'A' + i[1:] for i in r if i[0] == 'a' or 'b'}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r }
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c' }
# print(a)
# ---------------------------------------

# a = {0, 1, 2, 3}
# a.add(4)
# a.add(4)
# print(a)
# a.remove(2)
# print(a)

# a = {'Tom', 'Bob', 'Alice'}
# a.add('Ann')
# print(a)
# a.remove('Tom')
# print(a)
# user ='Tom'
# if user in a:
#     a.remove(user)
# print(a)
# --------------------------------------

# b = {1, 8, 3, 9}
# print(b)
# discard() - удаляет, если есть и не выбрасывает ошибку, если нет
# pop() - удаляет первый элемент
# ---------------------------------------

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}

# c = a.union(b)  # возвращает объединение (уникальные из 2-х мн-ств)
# c = a | b
# print(c)

# a.update(b)  # добавляет в "а" эл-ты из "в"
# a |= b
# print(a)

# c = a & b
# print(c)

# a &= b
# print(a)

# c = a - b
# print(c)

# c = a ^ b
# print(c)
# -------------------------------------

#  уникальные эл-ты, их кол-во, мин-ый и макс-ный эл-ты

# union_set = {1, 2} | {3} | {4, 5} | {3, 2, 6} | {6} | {7, 8} | {9, 8}
# print(union_set)
# print('Кол-во уник-х эл-тов:', len(union_set))
# print('Минимальный эл-т:', min(union_set))
# print('Максимальный эл-т:', max(union_set))
# ------------------------------------------

# Общие буквы в разных строках

# str_1 = input('Введите первую строку: ')
# str_2 = input('Введите вторую строку: ')
# print("Общими буквами являются: ", '\n', set(str_1) & set(str_2))
# --------------------------------

# буквы первой строки, отсутствующие во второй
# str_1 = input('Введите первую строку: ')
# str_2 = input('Введите вторую строку: ')
# print("Разными буквами являются: ", '\n', set(str_1) - set(str_2))
# -----------------------------------


# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# print("Только одно хобби:", drawing ^ music)
# print("Бросил оба занятия:", drawing & music)
# print("Рисуют:", drawing - (drawing & music))
# ---------------------------------------


# set_frozen = frozenset([1, 2, 3, 4, 5])
# print(set_frozen)
#
# set_set = frozenset({'Hello', 'world'})
# print(set_set)


#   ===========  СЛОВАРИ    ==========      !!!!!!

# s = ['one', 'two']
# print(s[0])
# d = {1: 'one', 2: 'two'}
# print(d[1])

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))
#
# d1 = dict(one= 1, two= 2)  #  в этом случае ключ не может быть числом
# print(d1)
# print(type(d1))
# -------------------------------------------------------


# a = (
#     ('igor@mail.com', 'igor'),
#     ('irinf@gmail.com', 'irina'),
#     ('anna@mail.com', 'anna')
# )
# d = dict(a)
# print(d)
# -----------------------------------------------------------

# d = {a: a ** 2 for a in range(1, 7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# d[6] = 4 ** 2
# print(d)
# -----------------------------------------

# d = {0: 'text', 'one': 45, (1, 2, 3): 'кортеж', 42: [2, 3, 6, 7]}
# print(d)  # ключ не может быть в виде списка
# print('one' in d)
# print(d.keys())
# if 'one' in d:
#     print('TRUE')

# key = 3
# if key in d:
#     del d[key]
# print(d)

# try:
#     del d[key]
# except KeyError:
#     print(f"Элемента с ключом " + str(key) + " нет в словаре")


# for key in d:
#     print(key, '->', d[key], end='\t\t')

# for key in range(len(d)):  # так не работает
#     print(key, '->', d[key], end='\t\t')
# ------------------------------------------------

#   Задача
#  Перемножить значения словаря
# dict_for_example = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(dict_for_example)
# product = 1
# for key in dict_for_example:
#     product *= dict_for_example[key]
# print("Произведение значений:", product)
# ------------------------------------------------

# dict_user = dict()
# dict_user[1] = input('->')
# dict_user[2] = input('->')
# dict_user[3] = input('->')
# dict_user[4] = input('->')
# print(dict_user)

# dict_user = {a: input('название овоща: ') for a in range(1,5)}
# print(dict_user)
# exclude = input('Какой овощ убрать?: ')
# x = None
# for key in dict_user:
#     if dict_user[key] == exclude:
#         x = key
# if x in dict_user:
#     del dict_user[x]
#     print(dict_user)
# else:
#     print('такого овоща :', exclude, 'нет в списке')
# ------------------------------------------------------

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
# # print(capitals)
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print('Столица страны ' + country + ': ' + capitals[country])
#     else:
#         print('В базе нет страны с таким названием - ' + country)
# ----------------------------------------------------------------

#  задача данные о товарах, их цене и количестве

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium 63220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
# for key in goods:
#     print(key, ')', goods[key][0], ' -', goods[key][1], 'шт. по', goods[key][2],
#           'руб')
# while True:
#     n = input('№: ')
#     if n != '0':
#         cnt = int(input('Количество: '))
#         goods[n][1] = cnt
#     else:
#         break
# for key in goods:
#     print(key, ')', goods[key][0], ' -', goods[key][1], 'шт. по', goods[key][2],
#           'руб')
# ----------------------------------------------------------------

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# value = d.get('a')
# value_1 = d.get('e', 'No')
# print(value)
# print(value_1)
# item = d.items()
# print(item)
# key = d.keys()
# print(key)
# value_2 = d.values()
# print(value_2)

# for el in d:
#     print(el, end='  ')
# print()
# for mean in d.values():
#     print(mean, end='\t')

# for key , mean in d.items():
#     print(key + ':', mean)
# print()
# d.clear()
# item = d.pop('e', 6)
# print(item)
# item_1 = d.pop('b', 6)
# print(item_1)
# print(d)

# item_2 = d.popitem()  # удаляет произвольный ключ-значение
# print(item_2)
# print(d)
# print()
# item_3 = d.setdefault('c')  # вернёт значение ключа, если ключ есть
# print(item_3)
# print(d)
# item_4 = d.setdefault('e')  # добавит ключ "е" со значением None
# print(item_4)
# print(d)
# item_5 = d.setdefault('f', 5)  # добавит пару - ключ:значение ('f': 5)
# print(item_5)
# print(d)
# print()
# d.update([("r", 7), ('q', 9)])  # можно добавлять
# print(d)
# d.update([('q', 12)])  # можно менять и можно писать в {'q', 12}
# print(d)
# print()
# d2 = d
# print('D = ', d)
# print('D2 = ', d2)
# d['e'] = 7
# d2['b'] = 5
# print('D = ', d)
# print('D2 = ', d2)

# d3 = d.copy()
# print('D = ', d)
# print('D3 = ', d3)
# d['e'] = 7
# d3['b'] = 5
# print('D = ', d)
# print('D2 = ', d3)
# -----------------------------------

#  из двух словарей сделать один
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # c = x.copy()
# # c.update(y)
# c = x | y
# print(c)
# -------------------------------------------------------

#  про словари
# dict_name = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# # dict_fin = dict()
# # dict_fin['name'] = dict_name.pop('name')
# # dict_fin['salary'] = dict_name.pop('salary')
# dict_name['location'] = dict_name.pop('city')
# #
# #
# print(dict_name)
# # print(dict_fin)
# -------------------------------------------------

# dict_nested = {
#     'First': {1: 'one', 2: 'two', 3: 'three'},
#     'Second': {4: 'four', 5: 'fife'}
# }
# for el in dict_nested:
#     print(el)
#     for y in dict_nested[el]:
#         print('\t', str(y) + ':', dict_nested[el][y])
# ----------------------------------------------

# dict_nest = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# dict_new = {key: value for key, value in dict_nest.items()}
# dict_new_2 = {value: key for key, value in dict_nest.items()}
# print(dict_nest)
# print(dict_new)
# print(dict_new_2)
# dict_new_3 = {key: value for key, value in dict_nest.items() if value <= 2}
# print(dict_new_3)
# dict_4 = {}
# z = 0
# for el in dict_nest:
#     z += 1
#     if z < 3:
#         dict_4[el] = dict_nest[el]
# print(dict_4)
# ------------------------------------------------------------------

# dict_multiply = {i: i * 5 for i in [10, 20, 30, 40]}
# print(dict_multiply)
#
# dict_multiply_2 = {i: i * 5 for i in "Hello"}  # ключей будет четыре
# print(dict_multiply_2)

# value_input = int(input('->'))
# lt = [1,2, 3, 4, 5]
# dict_multiply_3 = {i: value_input for i in lt}  # in range(1, 9)
# print(dict_multiply_3)
# -------------------------------------------------

# dict_from = dict.fromkeys(['a', 'b'], 100)
# print(dict_from)
# ----------------------------------------------

# figures = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# value = list(figures)  # равнозначно: value = list(figures.keys()) ключи
# value_s = list(figures.values())  # значения
# key_value = list(figures.items())  # ключи и значения
# print(value)
# print(value_s)
# print(key_value)
# ---------------------------------------

# задача: преобразовать список в словарь, строки-ключи, числа-значения
# list_example = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# dict_reply = {}
# key_str = None
# for i in list_example:
#     if type(i) == str:
#         dict_reply[i] = []
#         key_str = i
#     else:
#         dict_reply[key_str].append(i)
#
# print(dict_reply)
# -----------------------------------------

# zip()
# dict_1 = zip([12, 1, 2], ['Dec', 'Jan', 'Feb'])
# print(dict_1)
# print(list(dict_1))
# print(dict(dict_1))  # будет пустой словарь, надо так
# #  dict_1 = list(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))

# list_1 = [12, 1, 2]
# list_2 = ['Dec', 'Jan', 'Feb']
# # overall_dict = {k: v for k, v in zip(list_1, list_2)}
# overall_dict = {k: v for k, v in zip(list_2, list_1)}
# print(overall_dict)
# --------------------------------

# print(list(zip(range(5), range(100, 150))))
# a = [1, 2, 3]
# b = [5, 6, 7, 4]
# print(list(zip(a, b)))
# --------------------------------------------

# dict_1 = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# dict_2 = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (key, value), (key_2, value_2) in zip(dict_1.items(), dict_2.items()):
#     print(key, '->', value, value_2)
#     # print(key_2, value_2)
#
# for (key, value),  value_2 in zip(dict_1.items(), dict_2.values()):
#     print(key, '->', value, value_2)
#     # print(key_2, value_2)
# ----------------------------------------------

# list_a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# x, y = zip(*list_a)
# print(x)
# print(y)
# dict_a = {x: y}
# print(dict_a)
# -----------------------------------------

# lt1 = [2, 1, 4, 3]
# lt2 = ['d', 'a', 'c', 'b']
# a1 = list(zip(lt1, lt2))
# print(a1)
# a1.sort()
# print(a1)
# print()
# # a2 = list(zip(lt2, lt1))
# # print(a2)
# # a2.sort()
# # print(a2)
# b = sorted(zip(lt2, lt1))
# print(b)
# -------------------------------------------

# задача про таблицу

# month = ['January', 'February', 'March']
# total_sales = [52_000.00, 51_000.00, 48_000.00]
# production_cost = [46_800.00, 45_900.00, 43_200.00]
# # x, y, z = list(zip(month, total_sales, production_cost))
# # print(x)
#
# for sales, cost, mon in zip(total_sales, production_cost, month):
#     # res = sales - cost
#     print('Чистая прибыль в:', mon, 'равна', sales - cost)
# ------------------------------------------------------------

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# # print({one, two})  # так не работает
# print({**one, **two})
# print([one, two])  # работает без вопросов
# ----------------------------------------

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
#
# for key, value in {**one, **two}.items():
#     print(key, '->', value)
# -----------------------------------------------

# en = ['red', 'green', 'blue']
# j = 1
# for i in en:
#     print(j, '-й цвет: ', i, sep='')
#     j += 1

# en = ['red', 'green', 'blue']
# for j, i in enumerate(en, 1):
#     print(j, '-й цвет: ', i, sep='')
#     j += 1
# --------------------------------------------------

# en = {0: 3, 1: 6, 2: 9 }
# for i, j in enumerate(en):
#     print(i, ':', j, '->', en[j], sep='')
# ------------------------------------

# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# c = [*a, 4, 5, 6]
# print(b)
# print(c)


# def func(*args):
#     return args
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# print(func())
# ---------------------

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
# num_1 = summa(1, 2, 3, 4, 5, 6, 7, 8)
# num_2 = summa(6, 7, 8)
# print(num_1)
# print(num_2)
# -------------------------


#   словарь из аргументов
# def to_dict(*args):
#     # d = {}
#     # for i in args:
#     #     d.setdefault(i, i)   # d[i] = i
#     # return d
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


#  среднее арифметическое из значений
# def arithmetic(*args):
#     list_answer = [d for d in args if d < sum(args) / len(args)]
#     print('среднее арифметическое:', sum(args)/ len(args))
#     return  list_answer
#
#
# print(arithmetic(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(arithmetic(3, 6, 1, 9, 5))
# -----------------------------------------------

# def func(a, *args):
#     return a, args
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# -------------------------------------------

# def print_scores(stud, *scores):
#     print('Student name:', stud)
#     for score in scores:
#         print(score, end=' ')
#     print()
#
# print_scores('John', 100, 95, 88, 92, 99)
# print_scores('Rick',  99, 23, 92, 99)
# ------------------------------------------


# def rever(n):
#     """""вспомогательная функция"""
#     s = str(n)
#     return int(s[::-1])
#
#
# def reversal(*args, only_odd=False):
#     """""разворачиваем каждое число в списке"""
#     # if not only_odd:
#     #     lst = [int(str(i)[::-1]) for i in args]
#     # else:
#     #     lst = [int(str(i)[::-1]) for i in args if i % 2 != 0]
#     lst_1 = []
#     for i in args:
#         if not only_odd or only_odd and i % 2:
#             lst_1.append(rever(i))
#     return lst_1
#
# print(reversal(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(reversal(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))
# ----------------------------------------------


# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2,c=3))
# print(func())
# print(func(a='Python'))
# ---------------------------------------------

# def info(**data):
#     """""распаковка и оформление словаря"""
#     for key, value in data.items():
#         print(key, '->', value)
#     print()
# info(first_name='Irina', last_name='Petrova', age=22, phone=1234567890)
# info(first_name='Igor', last_name='Ivanov', age=34, email='ihor@mail.com',
#      country='Russia', phone=6789012345)
# ---------------------------------------------------

# my_dict = {'one': 'first'}
#
# def dict_add(**kwargs):
#     """""добавляем в словарь новые параметры"""
#     my_dict.update(kwargs)
#     # for key, value in kwargs.items():
#     #     # my_dict.setdefault(key, value)
#     #     my_dict[key] = value
#     print('my_dict = ', end='')
#     return my_dict
#
# print(dict_add(k1=22, k2=31, k3=11, k4=91))
# print(dict_add(name='Bob', age=31, weight=61, eyes_color='grey'))
# ---------------------------------------------------

# def func_1(*args):
#     print(args[0])
#
# def func_2(**kwargs):
#     print(kwargs['one'])
#
# func_1(1, 2, 3, 4, 5)
# func_2(one=123, two=456)
# -------------------------------------------------

# def func(a, *args, one=True, **kwargs):
#     return a, args, kwargs, one
#
#
# print(func(5, 9, 7, 8, 6, one=False, b=2, c=3, d=4))
# -------------------------------------------------


#  ОБЛАСТЬ ВИДИМОСТИ (SCOPE) !!!!!!!!!!!!

# for i in range(5):
#     a = 5
#     print(i)
#
# print('i за пределами цикла =', i, "a =", a)


# if True:
#     a = 5
#
# print('a =', a)
# --------------------------------------


# name = 'Tom'
#
# def hi():
#     print('Hello', name)
#
# def bye():
#     global name
#     name = 'Bob'
#     print('Good bye', name)
#
# hi()
# bye()
# print(name)
# ------------------------------------------------------

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # = 5
# print(i)  # = 6
# -------------------------------------------------------------


# def add_two(a):
#     x = 2
#     return a + x
#
# print(add_two(3))
# # print(x)
# ------------------------------------------------

# def func(a):
#     x = 2
#
#     def inner():
#         print('x = ', x)
#         return a + x
#     return inner()
#
#
# print(func(1))
# --------------------------------------

# import builtins  #  !!!!!!!!!!!
#
# print(dir(builtins))
# --------------------------------------------
#    27-я пара

# def outer_func():
#     def inner_func():
#         print("Hello, World!")
#
#     inner_func()
#
# outer_func()

# как бы то же самое
# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("World!")
# -------------------------------------------

# def func_1():
#     a = 6  # 2
#
#     def func_2(b):
#         a = 4  # 5
#         print('Сумма:', a + b)  # 6
#
#     print("a:", a)  # 3
#     func_2(4)  # 4
#
# func_1()  # 1
# -----------------------------------------


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     print('global:', x)
#
#     def inner():
#         nonlocal a  # для присваивания вышестоящей "а" нового значения
#         a = 35
#         print('nonlocal:', a)
#
#     inner()
#     print('a:', a)
#     t = a
#
#
# fn()
# z = x + t
# print('rez:', z)
# -------------------------------------------

# def fn1():
#     x = 25
#
#     def fn2():
#
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2, x =', x)
#
#     fn2()
#     print('fn1, x =', x)
#
# fn1()
# ----------------------------------------

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print('a, b = ', a, b)
#
#     inner()
#     print(a, b)
#     return [a, b]
#
# res = outer(2, 3, -1, 4)
# print(res)
# -------------------------------------------

# def increment(number):
#     def inner():
#         return number + 1
#     return inner()
#
# print(increment(10))
# res = increment(12)
# print(res)
# -------------------------------------------------------

#            !!!  Замыкание !!!

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner

# print(outer(5)(10))

# df = outer(4)(10)
# print(type(df))

# res = outer(5)
# print(res(10))
# print(res(2))
#
# res2 = outer(7)
# print(res2(12))
# print(res2(21))
# print(type(res))
# ----------------------------------------------

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + '_new'
#         return a, b, c
#
#     return func2
#
# func = func1()
# print(func())
# ---------------------------------------------

#  Задача про посещения городов


# def town(name_town):
#     """""Считаем посещения городов"""
#     vizit = 0
#
#     def counter():
#         nonlocal vizit
#         vizit += 1
#         print( name_town, vizit)
#     return counter
#
#
# moscow = town('Москва')
# sochi = town('Сочи')
# moscow()
# moscow()
# sochi()
# sochi()
# moscow()
# ---------------------------------------------

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
#     'Grace': 69,
# }
#
# def make_classifier(lowe_r, upper):
#     """""Определяем группы по баллам"""
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lowe_r <= v < upper}
#
#     return classify_student
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 800)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))
# -----------------------------------------------------

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# ------------------------------------------------

# 29-й урок
#  Анонимные функции, lamda-выражения

# print((lambda x, y: x + y)(1, 3))
# print((lambda x, y: x + y)('a', 'b'))

# сумма квадратов двух чисел
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
# print(summ())
# print(summ(10))
# print(summ(10, 20))
# print(summ(10, 20, 30))
# ------------------------------------------------

# func1 = lambda *args: args
# print(func1(1, 2, 3, 4))


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4
#      )
# for t in c:
#      print(t('abc_'))
# -------------------------------------------------------


# def inc1(n):  # если без lamda-функции
#      def wrap(x):
#           return x + n
#
#      return wrap

# def inc(n):
#      return lambda x: x + n
#
# f = inc(42)
# print(f(3))
# #----------------------------------
#
# inc2 = (lambda n: (lambda x: x + n))  # 3-й вариант
# # f2 = inc(42)
# # print(f2(3))
# print(inc(42)(3))

# print((lambda n: (lambda x: x + n))(42)(3))
# z = ((lambda n: (lambda x: x + n))(42)(3))
# print(z)
# ----------------------------------------------------

# лямбда-выражение для суммы трёх чисел
# z = (lambda x, y ,n: x + y + n)(2, 4, 6)
# z = (lambda n: (lambda x, y: x + n + y))(2)(4, 6)
# z = (lambda n: (lambda x: lambda y: y + x + n))(2)(4)(6)
# print(z)
# -----------------------------------------------

# d = {'b': 15, 'a': 10, 'c': 4}
# lst =  list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1], reverse=True)
# print(lst)
# tp = tuple(lst)
# print('tp=', tp)
#
# d1 = dict(lst)
# d2 = dict(lst)
#
# print(d1)
# print('d2= ', d2)
# ----------------------------------------------

# lst = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 19},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Фёдор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семёнов', 'rating': 6}
# ]
# print(sorted(lst, key=lambda x: x['last name']))
# ---------------------------------------------------------


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y),
#      (lambda x, y: x / y)]
# b = a[2](12, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# # print(abs(-3))
# for i in b:
#     if i < 0:
#         print('i<0:', a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print('0:', a['three'](i))
# -----------------------------------------

# d = {
#     1: (lambda : print('Понедельник')),
#     2: (lambda : print('Вторник')),
#     3: (lambda : print('Среда')),
#     4: (lambda : print('Четверг')),
#     5: (lambda : print('Пятница')),
#     6: (lambda : print('Суббота')),
#     7: (lambda : print('Воскресение'))
# }
#
# d[1]()
# ---------------------------------------

# maximum = (lambda a, b: a if a > b else b)
# print(maximum(15, 13))

# minimum = (lambda a, b, c: print(min(a, b, c)))
# minimum(9, 8, 5)

# minimum = (lambda a, b, c: (a if a < b else b) if a < c else(b if b < c else c))
# minimum = (lambda a, b, c: a if (a < b and a < c) else (b if b < a and b < c else c))
# # minimum = (lambda a, b, c: a if a < b else b if b < c else c)
#
# print(minimum(91, 11, 25))
# -------------------------------------------


# ФУНКЦИЯ MAP

# def multiply(t):
#     return t * 2
#
# lst = [2, 8, 12, -5, -10]
#
# print(map(multiply, lst))
# print(list(map(multiply, lst)))
# # print(list(zip(lst)))
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda t: t * 2, range(2, 12))))
# print(list(map(lambda t: t * 2, [i ** 2 for i in range(2, 6)])))


# t = 2.88, -1.75, 100.55
#
# print(tuple(map(lambda x: int(x) ** 2, t)))
# print(list(map(lambda x: str(x), t)))
#
# a = ['2.88', '-1.75', '100.55']
# print(list(map(float, a)))


# areas = [3.584902, 5.7892549, 7.456789, 56.413546, 9.209855, 32.085243]
#
# print(list(map(round, areas, range(1, 7))))
# print(list(map(round, areas, [1, 1, 1, 1, 1, 1])))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# lst = list(map(lambda x, y: (x, y), st, num))
# lst1 = list(map(lambda x, y: [x, y], st, num))
# tp = dict(map(lambda x, y: (x, y), st, num))
#
# print(lst)
# print(lst1)
# # tp = dict(lst)
# print(tp)


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))
# --------------------------------------------------------------

#  31-пара
#   ФИЛЬТР FILTER ---------- !!!!!!!!!!!!!!!!!

# filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# print(dir(filter))

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: 88 > s > 75, b))
# print(res)
# ----------------------------------------------------

# from random import randint
#
# sps = [randint(1, 41) for i in range(1, 11)]
# print(sps)
# print('[10; 20] =', list(filter(lambda x: 10 <= x <= 20, sps)))
# -------------------------------------------------------------

# sp = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda x: x % 15 == 0, sp)))
# -------------------------------------------------

#  ДЕКОРАТОРЫ  !!!!!!!!!!!!!!!!!!!!!!!!!!!

# def hello():
#     return 'Hello, I am func "hello"'
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
# super_func(hello)
# ------------------------------------------------

# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
# def func_test():
#     print('Hello, I an func  "func_test"')
#
# test = my_decorator(func_test)
# test()
# my_decorator(func_test)()
# ----------------------

# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I an func  "func_test"')
#
# func_test()
# ---------------------------------------------

# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
# @italic
# @bold
# def hello():
#     return "text"
#
# print(hello())
# ----------------------------------------------


# def counter(func):
#     i = 0
#     def wrap():
#         nonlocal i
#         func()
#         i += 1
#         print('Вызов функции:', i)
#
#     return wrap
#
# @counter
# def hello():
#     print('Hello')
#
# hello()
# ---------------------------------------------

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print('*' * 25)
#         fn(arg1, arg2)
#         print('*' * 25)
#
#     return wrap
#
# @args_decorator
# def print_full_name(first, last):
#     print('Меня зовут', first, last)
#
#
# print_full_name('Ирина', "Лаврова")
# -----------------------------------------------------------


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print('*' * 25)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         print('*' * 25)
#
#     return wrap
#
# @args_decorator
# def print_full_name(*args, study='Python'):
#     print(args, 'изучают', study)
#
#
# print_full_name('Ирина', "Борис", "Светлана", study="JavaScript")
# print()
# print_full_name("Владимир", "Екатерина")
# print()
#
# @args_decorator
# def hello():
#     print('Hello')
#
# hello()
# ----------------------------------------------------------

#  32-пара


# def decor(args_1, args_2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args_1, x, args_2, y, "=", end=' ')
#             fn(x, y)
#         return wrap
#     return args_dec
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
# -----------------------------------------------------

# def mult_num(a):  # 1-й вариант
#     def for_func(fn):
#         def wrap(x):
#             print("Результат произведения:", a, "*", x, "=", a * x)
#             fn(x)
#         return wrap
#     return for_func
#
# @mult_num(3)
# def num_for(a):
#     return a
#
# num_for(5)
# ------------------------------------------------

# def mult_num(a):  # 2-й вариант
#     def for_func(fn):
#         def wrap(x):
#             fn(x)
#             # return "Результат произведения: " + str(a) + " * " + str(x)\
#             #         + " = " + str(a * x)
#             return "Результат произведения: " + str(a) + " * " + str(x) \
#                 + " = " + str(a * fn(x))  # 3-й вариант
#         return wrap
#     return for_func
#
# @mult_num(3)
# def num_for(a):
#     return a
#
# print(num_for(5))
# ---------------------------------------------------------
# что бы функция принимала только числа

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z=None):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn2("Hello ", "World", "!"))
# print(typed_fn3("Hello, ", "World   ", z=5))
# ------------------------------------------------


# def decor(tx=None, decor_text='  '):
#     def wrapper(fn):
#         def wrapp(*args):
#             print(decor_text, end='')
#             fn(*args)
#
#         return wrapp
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
# hello_world2("Hi")
#
#
# @decor(decor_text='Hello, ')
# def hello_world(text):
#     print(text)
#
# hello_world("world!")
# ----------------------------------------------------------


# print(int("100", 2))
# print(int("100", 8))
# print(int('100', 16))
# print(int('100', 10))


# print(bin(18))  # 0b10010  2-ная
# print(oct(18))  # 0o22  8-ная
# print(hex(18))  # 0x12  16-ная

# print(0b100)
# print(0o100)
# print(0x100)
# -----------------------------------------------------

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print('y' in e)
# print(e[2])
# print(e[-2])
# print(e[1:-1])
# print(e[::-1])
# print(e[-1:0:-1])
# e = e[:3] + 't' + e[4:]
# print(e)
# -----------------------------------------

#   34-я пара --------------------------------------

# Заменить символ в строке

# str1 = ("Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык "
#         "программирования")
#
#
# def change_letter(s, c_old, c_new):
#     st = ''
#     for i in s:
#         if i != c_old:
#             st += i
#         else:
#             st += c_new
#     return st
#
#
# st2 = change_letter(str1, 'N', 'P')
# print(st2)
# ---------------------------------------------------------------


# print(r'C:\file.txt')  # сырые строки, игнорируют спецсимволы(читают как строки)
# print('C:\\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + '\\')
# print('C:\\file.txt\\')

# name = "Дмитрий"
# age= 25
#
# print("Меня зовут " + name + '. Мне ' + str(age) + ' лет')
# print("Меня зовут ", name, '. Мне ', age, ' лет', sep='')
# print(f"Меня зовут {name}. Мне {age} лет")
#
# print(f"{round(2.356789, 2)}")
# print(f"{2.356789:.2f}")
# print(f"{int(2.356789)}")

# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}"
#       f" - выражение")

# d = 74
# print(f"{{{d}}}")

# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# ----------------------------------------------------

# s = """<fiv>
#     <a href="#"content<a/>
# </div>
# """
# print(s)

# 'Привет'
# "Привет"


# def square(n):
#     """Принимает число и возвращает его квадрат"""
#     return n ** 2


# print(square(5))
# print(square.__doc__)
# # print(min.__doc__)
# ----------------------------------------------------

# import math


# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# ---------------------------------------------------------

# 35-я пара символы ASCII

# print(ord('a'))  # 97
# print(ord('а'))  # русская "а" 1072

# while True:
#     n = input("-> : ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break
# __________________________________________

#  Задача

# my_str = 'Test string for me'
# arr = [ord(x )for x in my_str]
# print(arr)
#
# # arr.append((int((sum(arr) / len(arr)))))
# # arr.append((sum(arr) // len(arr)))
# # arr[-1], arr[0] = arr[0], arr[-1]
#
# # arr.insert(0, (sum(arr) // len(arr)))
#
# arr = [sum(arr) // len(arr)] + arr
# print(arr)
#
# # arr += [x for x in [ord(x) for x in (input("-> "))] if x not in arr]
# arr += [ord(x) for x in (input("-> ")) if ord(x) not in arr][:3]
# print(arr)
#
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
# else:
#     print("Zero")
#
# arr.sort(reverse=True)
# print(arr)
# -------------------------------------------------------

# print(chr(97))
# print(chr(35))
# print(chr(8364))


# -----------------------------------------------------------

# b = 122
# a = 97
#
# st =''
# for i in [ chr(x) for x in (range(b, a + 1) if a >= b else range (a, b + 1)) ]:
#     st += (i + ' ')
# print(st)
# --------------------------------------------------------------------------

# print('apple' == 'Apple')
# print('apple' > 'Apple')  # True
# print('apple' > 'A')  # True
# ------------------------------------


#  36-я пара -----!!!!

#  случайный пароль

# from random import randint
#
# SHOR_TEST = 7
# LONG_EST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def random_password():
#     random_length = randint(SHOR_TEST, LONG_EST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print('Ваш случайный пароль:', random_password())
# ------------------------------------------------------


# МЕТОДЫ СТРОК

# print(dir(str))

# s = 'hello, WORLD! I am learning Python.'
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase()) # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.

# print(s.count('l', 3, 8))
# print(len(s))
# print(s.find('Python'))  # первое вхождение обозначенного элемента 28
# # print(s.find('Python1'))  # -1 если нет
# --------------------------------------------------

# st = 'один два'  # задача - переставить местами
# ind = st.find(' ')
# # print(st[ind::])
# # print(st[ind::] + " " + st[0:ind])
# a = st[:st.find(' ')]
# b = st[st.find(' '):]
# print(b + " " + a)
# ---------------------------------------

# s = 'ab12c59p7dq'  # задача извлечь цифры
# int_s = []
# for i in s:
#     # if i in '1234567890':  # 1-й вариант
#     if '1234567890'.find(i) != -1 :  # 2-й вариант
#         int_s.append(int(i))
#
# print(int_s)

# for i in s:  # 3-й вариант
#     try:
#         int_s.append(int(i))
#     except ValueError:
#         continue
#
# print(int_s)
# -----------------------------------------------------------

# s = 'hello, WORLD! I am learning Python.'
# print(s.index('Python'))
# print(s.index('Python1'))  # ValueError  выбрасывает исключение

# print(s.rfind('l'))
# print(s.find('l'))
# print(s.rindex('l'))
# -----------------------------------------

# s1 = 'I am learning Python. hello, WORLD!' # убрать h и всё между ними
# print(s1[0:s1.find('h')] + s1[s1.rfind('h') + 1:])
# -------------------------------------------------------

# print('abc123'.isalnum())  # состоит ли строка только из цифр и букв True
# print('abc 123'.isalnum())  # состоит ли строка только из цифр и букв False
# print('ABCabc'.isalpha())  # состоит ли строка только из букв True
# print('123'.isdigit())  # состоит ли строка только из цифр True
# print('abc'.islower())  # состоит ли строка только из строчных букв True
# print('ABC6'.isupper())  # состоит ли строка только из заглавных букв True
# --------------------------------------------------------------------

# print('pw'.center(10))  # выравнивание строки по центру на 10 символов
# print('pw'.center(10, '-'))  # выравнивание строки по центру на 10 символов

# print('      py  '.strip())  # удаляет пробелы по краям
# print('      py  '.lstrip())  # удаляет пробелы по краю слева
# print('      py  '.rstrip())  # удаляет пробелы по краю справа
# print('**    py**'.strip("*"))  # удаляет "*" по краям
# print('https://www.python.org'.lstrip('/:pths'))

# print('py.$$$;'.rstrip(';$.'))
# print('https://www.python.org'.lstrip('htps:/w').rstrip('org.'))
# print('https://www.python.org'.strip('htps:/worg.'))
# print('https://www.python.org'.strip('htps:/worg').strip('.'))
# ------------------------------------------------------------------

# 37-я пара !!!!!!--------- МЕТОДЫ СТРОК

# str1 = ("Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык"
#         "программирования")
# print(str1.replace('Nython', 'Python', 2)) # что, на что и сколько
# ----------------------------------------------------

# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))  # a-b-c
#
# print('..'.join(seq))  # a..b..c
# print('..'.join(['1', '2', '3']))
# # print('..'.join([1, 2]))  # так не работает
#
# print(':'.join("Hello"))  # H:e:l:l:o

# join - объединяет итерируемую последовательность (список, кортеж, другая строка)
# в одну строку через заданный символ-разделитель

# split - разделяет строку указанным символом, сам разделитель удаляется,
# делит строку на список из подстрок

# print('Строка разделённая пробелами'.split())
# print('Строка разделённая пробелами'.split('_'))
# print('Строка разделённая пробелами'.split('а'))

# print('www.python.org.ru'.split('.', 2))


# a = input('->').split()
# a = list(map(int, input('->').split()))
# print(a)
# ------------------------------------------

# задача
# s = list(input('Введите свои фамилию, имя, отчество: ').split())
# print(s[0], s[1][0] + '.' +  s[2][0] + '.')
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')
# -----------------------------------------------

# print('www.python.org.ru'.split('.', 2))  # ['www', 'python', 'org.ru']
# print('www.python.org.ru'.rsplit('.', 2))  # ['www.python', 'org', 'ru']

# задача: в строке пробелы заменить на *

# str_ex = input('Введите строку: ').split()
# print('*'.join(str_ex))

# str_ex = input('Введите строку: ').replace(' ', '*')
# print(str_ex)
# ----------------------------------------------------

# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ !!!!!!!!!!!!!!

# import re

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = 'я'
# rg = 'совпадения'
# print(s.find(reg))  # 15
# print(re.findall(reg, s))  # ['я', 'я']
# print(re.findall('12', s))  # []

# search - месторасположение первого совпадения объекта
# print(re.search(rg, s))
# print(re.search(rg, s).span())  # (6, 16)
# print(re.search(rg, s).start())  # 6
# print(re.search(rg, s).end())  # 16
# print(re.search(rg, s).group())  # совпадения

# 38-я пара !!!!!!!-----------------------------

# print(re.split(reg, s))  # возвращает список, в котором строка разбита по шаблону
# rb = '.'  # "." - это любой символ
# print(re.split(rb, s))

# rd = r'\.'
# print(re.split(rd, s))
# print(re.split(rd, s, 1))

# print(re.sub(reg, '!', s, 1))  # поиск и замена

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = '2023'
# rg = '[203]'
#
# print(re.findall(reg, s))
# print(re.findall(rg, s))
# ----------------------------------------------------------------------------


# import re

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.9578 Ё'
# reg = '2023'
# rg = '[203]'
# rgg = r'[0-9]'
# rgg1 = r'[0-5]'
# reg2 = r'[12][90][0-9][0-9]'

# print(re.findall(reg, s))
# print(re.findall(rg, s))
# print(re.findall(rgg, s))
# print(re.findall(rgg1, s))
# print(re.findall(reg2 , s))

# rwg = r'[а-яё]'
# rwg2 = r'[А-яЁё]'  # r'[А-Яа-яЁё]'
# rwg3 = r'[А-яЁё][А-яёЁ]'
# rwg4 = r'[А-яЁё.]'

# print(re.findall(rwg, s))
# print(re.findall(rwg2, s))
# print(re.findall(rwg3, s))
# print(re.findall(rwg4, s))

# s1 = "Ели[-ели]."
# pattern = r'[А-яё.-]'  # "-" ставится либо в начале, либо в конце
# pattern2 = r'[А-яё.\[\]-]'  # квадрат-е скобки обязательно экранируются
# print(re.findall(pattern, s1))
# print(re.findall(pattern2, s1))
# ---------------------------------------------

# Задача: найти время в формате: [16:25]
# test = """Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45.
# Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09"""
#
# pat = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(pat, test))
# ---------------------------------------------------------------

# import re
#
# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.95_ 7 8'
# reg = r'[.]'
# reg1= r'\.'
# reg2 = r'[^0-0]'  # всё, кроме этих цифр
# print(re.findall(reg, s))
# print(re.findall(reg1, s))
# print(re.findall(reg2, s))

# reg = r'\d'
# reg1 = r'\w'
# reg2 = r'\W'
# reg3 = r'\s'  # ищет пробелы


# print(re.findall(reg, s))
# print(re.findall(reg1, s))
# print(re.findall(reg2, s))
# print(re.findall(reg3, s))

# ----------------------------------------------------------

# 39-я пара регулярные выражения !!!!!!!!!!!!-----------------


# reg4 = r'\w\s\w\Z'
# reg5 = r'\AЯ ищу'  # = r\A\w\s\w+
# reg6 = r'\b\w\s\w'
# reg7 = r'\w\s\w\b'
# reg8 = r'\Bсов'
#
# print(re.findall(reg4, s))
# print(re.findall(reg5, s))
# print(re.findall(reg6 , s))
# print(re.findall(reg7 , s))
# print(re.findall(reg8, s))
# -----------------------------------------------------

# import re

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.95_ 7 8'
#
# reg = r'\w+'
# rg = r'\d'
# rg1 = r'\d+'
# rg2 = r'20*'  # * относится только к последнему символу
# # rg3 = r'2*0*'
#
# # print(re.findall(reg, s))
# print(re.findall(rg, s))
# print(re.findall(rg1, s))
# print(re.findall(rg2, s))
# print(re.findall(rg3, s))

# повторения:
# + это от единицы до бесконечности
# * это от нуля до бесконечности
# ? это нуль или один

# s1 = 'Цифры: 7, +17, -42, 0013, 0.3'
# pattern = r'\d'
# pattern1 = r'\d+'
# pattern2 = r'\+\d+'
# pattern3 = r'\S*'
# pattern4 = r'\S*\d'
# pattern5 = r'[+-]?\d+'
# pattern6 = r'[+-]?\d+[.\d]*'  # лучше r'[+-]?d+\.?\d*
# pattern7 = r'\s?\d+'


# print(re.findall(pattern, s1))
# print(re.findall(pattern1, s1))
# print(re.findall(pattern2, s1))
# print(re.findall(pattern3, s1))
# print(re.findall(pattern4, s1))
# print(re.findall(pattern5, s1))
# print(re.findall(pattern6, s1))
# print(re.findall(pattern7, s1))
# ------------------------------------------------------

# import re

# s2 = '05-03-1987 # Дата рождения'
# print(re.sub(r'#.*', '', s2))
# print(re.sub(r'\d-?', '', s2))
# print(re.sub(r'\s+#\s?', '', re.sub(r'\d-?', '', s2)) + ': ' +
#       re.sub(r'-', '.', re.sub(r'#.*', '', s2)))
#
#
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s2)))
# print(re.sub(r'.*#\s', '', s2) + ': ' + re.sub(r'-', '.', re.sub(r'#.*', '', s2)))
# --------------------------------------------------------------------------

# Рег.выражение для всех ключей и значений

# st = 'autor=Пушкин А.С; title = Евгений Онегин; price =200; year= 1831'
# print(re.findall(r'\w+\s*=[^;]+', st))
# print(re.findall(r'\w+\s*=\s*\w+\s*[.\w]*', st))
# ---------------------------------------------------

# st2 = '12 сентября 20215 года'
# reg1 = r'\d'
# reg2 = r'\d{4}'
# reg3 = r'\d{2}'
# reg4 = r'\d{2,4}'
# reg5 = r'\d{2,}'
# reg6 = r'\w{2,}'
#
#
#
# print(re.findall(reg1, st2))
# print(re.findall(reg2, st2))
# print(re.findall(reg3, st2))
# print(re.findall(reg4, st2))
# print(re.findall(reg5, st2))
# print(re.findall(reg6, st2))
# ----------------------------------------------

# # найти номер тел-на в формате +7******* или 7*******
# test = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# print(re.findall(r'\+?7\d{10}', test))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.95_ 7 8'
# reg = r'\w+\s\w+'
# reg2 = r'^\w+\s\w+'
# reg3 = r'\w+\s\w+$'
#
# print(re.findall(reg, s))
# print(re.findall(reg2, s))
# print(re.findall(reg3, s))
# ----------------------------------------------------

# def login(a):
#     return re.findall(r'^[\w!@$-]{8,25}$', a)
#
# print(login('admin_admin'))
# print(login('*admin_admin'))
# print(login('admin_admin##'))
# ----------------------------------------------

# флаги

# print(re.findall(r'\w+', "12 + й"))
# print(re.findall(r'[а-я]', "Я я", flags=re.IGNORECASE))
# print(re.findall(r'[а-я]', "Я я", re.IGNORECASE))

# text = """
# one
# two
# """
# text2 = "one\ntwo"
#
# print(text)
# print(re.findall(r'^one$', text))
# print(re.findall(r'^one$', text, re.MULTILINE))
# print(re.findall(r'^one$', text2, re.MULTILINE))
# ------------------------------------------------------------

# import re

# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# ------------------------------------------------

# 41-пара !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# print(re.findall("""
# [A-z.-]+  # part1
# @  # поск символов @
# [a-z_.-]+  # part2
# """, "test@mail.ru", re.VERBOSE))


# text = 'hello world'
# print(re.findall(r'\w+', text, re.DEBUG))

# text1 = """Python,
# python
# PYTHON"""
# reg = '^python'
# reg2 = "(?im)^python"
# print(re.findall(reg, text1, flags=re.IGNORECASE | re.MULTILINE))
# print(re.findall(reg2, text1))
# ----------------------------------------------------------------------------

# найти адрес электронной почты
# test = ("123456@.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru,"
#         " login.3-67@i.ru, 1login@ru.name.ru.")
#
#
# rege1 =r"[\w.-]+@[\w.]+\w{2,3}"
# rege2 =r"[\w.-]+@[\w.]+[^., _]"
#
# print(re.findall(rege1, test))
# print(re.findall(rege2, test))
# ------------------------------------------------------------------

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.+>", text))
# print(re.findall("<.+?>", text))
#
# # *?, +?, ??
# # {m,n}?,  {,n}?, {m,}?
# # это ленивые выражения
#
# t = '2324 786 22 4569'
# r1 = r'\d{1,3}'
# r2 = r'\d{1,3}?'
# print(re.findall(r1, t))
# print(re.findall(r2, t))
# -----------------------------------------------------

# greedy (жадный) по умолчанию
# lazy (ленивый) ?

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# s2 = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# rg = r'<img.*?>'
# rg2 = r'<img[^>]*>'
# rg3 = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
#
# print(re.findall(rg, s))  # <img src='bg.jpg'> это нужно получить
# print(re.findall(rg2, s))  # <img src='bg.jpg'> это нужно получить
# print(re.findall(rg3, s2))  # <img src='bg.jpg'> это нужно получить
# ------------------------------------------------

# 42-пара ---------5555555555555555555555

# test = ('Python (в русском языке встречается названия питон[16] или пайтон[17]) -'
#         'высокоуровневый язык программирования общего назначения с'
#         'динамической строгой типизацией и автоматическим '
#         'управлением памятью[18][19].')
#
# reg = r'\[\d+]'
# print(re.findall(reg, test))
# print(re.findall(r'\[\d+]', test))
# ---------------------------------------------------

# s = 'Пётр и Ольга отлично учатся!'
# reg = 'Пётр|Виталий|Ольга'
# print(re.findall(reg, s))

# st = "int = 4, float = 4.0, double = 8.0f"
# rg = r'\w+\s*=\s*\d+\.*\w*'
# rg2 = r'\w+\s*=\s*\d+[.\w+]*'
# rg3 = r'(?:int|double)\s*=\s*[.\w+]*'
#
# print(re.findall(rg, st))
# print(re.findall(rg2, st))
# print(re.findall(rg3, st))
#--------------------------------------

# 192.168.255.255
# s = '127.0.0.1'
# rg3 = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# rg4 = r'(?:\d{1,3}.*){4}'
# print(re.findall(rg3, s))
# print(re.findall(rg4, s))
#-------------------------------------------

# st = 'Word2016, PS6, AI5'
# reg = r'[A-z]+\d*'
# reg2 = r'([A-z]+)(\d*)'
#
# print(re.findall(reg, st))
# print(re.findall(reg2, st))

# s = '5 + 7 * 2 - 4'
# reg = '\s*([+*-])\s*'  # ['5', '+', '7', '*', '2', '-', '4']
# reg2 = '\s*[+*-]\s*'  # ['5', '7', '2', '4']
#
# print(re.split(reg, s))
# print(re.split(reg2, s))
#------------------------------------

# import re
#
# s = 'Я ищу совпадения в 2023 году. И я их найду в 2000000000 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])  # 1-я круглая скобка
# print(m[2])  # 2-я круглая скобка
# print(m[0])
#--------------------------------------------------------

print('Hello world')





























