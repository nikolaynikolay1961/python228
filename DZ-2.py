# ---------------Задача № 1--------------------------------
# five_digit = int(input('ВВедите целое пятизначное число: '))
# num = five_digit % 10
# work = num
# arithmetic = num
#
# five_digit //= 10
# num = five_digit % 10
# work *= num
# arithmetic += num
#
# five_digit //= 10
# num = five_digit % 10
# work *= num
# arithmetic += num
#
# five_digit //= 10
# num = five_digit % 10
# work *= num
# arithmetic += num
#
# five_digit //= 10
# num = five_digit % 10
# work *= num
# arithmetic += num
#
# print('Произведение цифр числа равно', work, '\nСреднеарифметическое:', arithmetic / 5)

# ---------------------------Задача № 2------------------------------------
# print('Меняем чётность числа')
# num = int(input('Введите любое целое число (отрицательное или положительное): '))
# if num == 0:
#     print('Это ноль, у него знака нет')
# elif num > 0:
#     print('Было положительное, стало с минусом:', -num)
# else:
#     print('Было отрицательное, стало с плюсом:', -num)

# --------------------------Задача № 3---------------------------------
#
# print('КАЛЬКУЛЯТОР')
# print(1, "- Меняем знак (унарный минус)", "\n",
#       2, "- Сложение", "\n",
#       3, "- Вычитание", "\n",
#       4, "- Деление", "\n",
#       5, "- Умножение", "\n",
#       6, "- Деление без остатка (деление по модулю)", "\n",
#       7, "- Минимальное число из двух", "\n",
#       8, "- Максимальное число из двух", sep='')
# select = int(input('Выберите действие: '))
# if select == 1:
#     num = int(input('Введите число: '))
#     print("Поменяем знак, было:", num, "стало:", -num)
# else:
#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))
#     if select == 2:
#         print("Сумма двух чисел равна: ", num1 + num2)
#     elif select == 3:
#         print("Разность двух чисел равна: ", num1 - num2)
#     elif select == 4:
#         num1 = float(input("Введите делимое число: "))
#         num2 = float(input("Введите делитель: "))
#         if num2 == 0:
#             print("На ноль делить нельзя")
#         else:
#             print("Частное двух чисел равно: ", num1 / num2)
#     elif select == 5:
#         print("Произведение двух чисел равно: ", num1 * num2)
#     elif select == 6:
#         num1 = float(input("Введите делимое число: "))
#         num2 = float(input("Введите делитель: "))
#         if num2 == 0:
#             print("На ноль делить нельзя")
#         else:
#             print("Остаток от деления двух чисел равен: ", num1 % num2)
#     elif select == 7:
#         if num1 < num2:
#             print("Минимальное число:", num1)
#         else:
#             print("Минимальное число:", num2)
#     elif select == 8:
#         if num1 < num2:
#             print("Максимальное число:", num2)
#         else:
#             print("Максимальное число:", num1)
#     else:
#         print("Такого действия нет")

#--------------------- Задача № 4 ----------------------------------------------

# print('Пишем правильно "копейки"')
# cent = int(input('Введите количество копеек в количестве до 99 : '))
# if 0 > cent or cent  > 99:
#     print('На такое количество мы не договаривались')
# elif (cent // 10 == 0) and (cent == 1) or (cent > 19 and cent % 10 == 1):
#     print(cent, 'копейка')
# elif cent // 10 == 0 and (cent == 2 or cent == 3 or cent == 4) \
#     or cent > 19 and (cent % 10 == 2 or cent % 10 == 3 or cent % 10 == 4):
#     print(cent, "копейки")
# else:
#     print(cent, "копеек")

#-------------- не правильно, все elif работают
#-------------------- вариант правильный--------------------------------

# print('Пишем правильно "копейки"')
# cent = int(input('Введите количество копеек в количестве до 99 : '))
# kop = cent
# if 11 <= kop <= 14:
#     print(cent, "копеек")
# elif 1 <= cent <= 10 or 15 <= cent <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(cent, "копейка")
#     elif 2 <= kop <=4:
#         print(cent, "копейки")
#     else:
#         print(cent, "копеек ")
# else:
#     print("На такое количество мы не договаривались")































