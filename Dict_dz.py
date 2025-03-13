#  Во вложенном словаре меняем данные
# dict_task =  {
#     "John": {"N": 2056, "S": 8463, "E": 3497, "W": 3656},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anna": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 3451}
# }
# for element in dict_task:
#     print(element)
#     for i in dict_task[element]:
#         print(i +':', dict_task[element][i])
#
# index_name = input('У какого менеджера будете менять данные? : ')
# index_region = input('В каком регионе будете менять данные? : ')
# meaning = input('Данные, которые будете менять: ')
# new_meaning = input('Новые данные: ')
# print(index_name)
# print(index_region)
# print(meaning)
# print(new_meaning )
# print()
# dict_task[index_name][index_region] = new_meaning
# print(index_name)
# for i in dict_task[index_name]:
#     print('\t', i + ':', dict_task[index_name][i])
# ----------------------------------------------------------------
# from itertools import zip_longest
# import re

#  создаём вложенный словарь, ищем средний балл и студентов
# total_points = 0
# dict_study = {}
# quantity = int(input('Количество студентов в группе: '))
# for i in range(1, quantity + 1):
#     list_name = []
#     name = input(str(i) + '-й студент, имя: ')
#     lust_name = input('Фамилия студента: ')
#     list_name.append(lust_name)
#     try:
#         grade = int(input('Оценка студента: '))
#     except ValueError:
#         print('Оценка должна быть числом')
#         grade = int(input('Оценка студента: '))
#     list_name.append(grade)
#     total_points += grade
#     dict_study.setdefault(name, list_name)
#
# print('Средний балл: ', round(total_points / quantity, 1))
# print('Студенты с оценкой выше среднего: ')
# for el in dict_study:
#     for j in range(len(dict_study[el])):
#         if type(dict_study[el][j]) == int and \
#         int(dict_study[el][j]) > total_points / quantity:
#             print(el, dict_study[el][0])
# ----------------------------------------------------------------------

#  изменить данные во вложенном словаре

# dict_change = {
#     'emp1': {'name': 'John', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500}
# }
# who_has = input('У кого будете менять зарплату: ')
# which_one = int(input('Сколько он(а) будет получать: '))
# for el in dict_change:
#     print(el)
#     for key in dict_change[el]:
#         if dict_change[el][key] == who_has:
#             dict_change[el]['salary'] = which_one
#         print('\t', key + ':', dict_change[el][key] )
# -------------------------------------

#  два словаря объединить в один

# dict_1 = {1: 10, 2: 20}
# dict_2 = {3: 30, 4: 40}
# dict_3 = {5: 50, 6: 60}
# dict_union = {**dict_1, **dict_2, **dict_3}
# print(dict_union)
# ----------------------------------------------------

#  Площадь фигуры в зависимости от ввода

# def square_body(figure_1=None, **kwargs):
#     """""площади различных фигур"""
#     if figure_1 == 1:
#         s = 1
#         for i in kwargs.values():
#             s *= i
#         print('Площадь ромба:', end=' ')
#         return s / 2
#     if figure_1 == 2:
#         s = 1
#         for i in kwargs.values():
#             s = i ** 2
#         print('Площадь квадрата:', end=' ')
#         return s
#     if figure_1 == 3:
#         lst = []
#         for i in kwargs.values():
#             lst.append(i)
#         lust = lst.pop()
#         print('Площадь трапеции:', end=' ')
#         return sum(lst) * lust / 2
#     if figure_1 == 4:
#         s = 1
#         for i in kwargs.values():
#             s = i ** 2 * 3.14
#         print('Площадь круга:', end=' ')
#         return s
#     else:
#         print('Несуществующая площадь:,', end=' ')
#         return {}
#
#
# body_type = int(input('Выберите фигуру: 1 - это ромб, 2 - квадрат, 3 - трапеция, '
#                   '4 - круг и 5 - не знаю: '))
# if body_type == 1:
#     param_s = {}
#     a = 'd'
#     size_body_1 = int(input('Введите первую диагональ ромба: '))
#     size_body_2 = int(input('Введите вторую диагональ ромба: '))
#     param_s[a + str(1)] = size_body_1
#     param_s[a + str(2)] = size_body_2
# elif body_type == 2:
#     param_s = {}
#     a = 'a'
#     size_body_1 = int(input('Введите сторону квадрата: '))
#     param_s[a + str(1)] = size_body_1
# elif body_type == 3:
#     param_s = {}
#     a, b, h = "a", "b", "h"
#     size_body_1 = int(input('Введите длину нижней стороны трапеции: '))
#     size_body_2 = int(input('Введите длину верхней стороны трапеции: '))
#     size_body_3 = int(input('Введите высоту трапеции: '))
#     param_s[a] = size_body_1
#     param_s[b] = size_body_2
#     param_s[h] = size_body_3
#     print(param_s)
# elif body_type == 4:
#     param_s = {}
#     r = 'r'
#     size_body_1 = int(input('Введите радиус круга: '))
#     param_s[r] = size_body_1
#     print(param_s)
# else:
#     param_s = {}
#     a, b, c = 'a', 'b', 'c'
#     size_body_1 = int(input('Введите произвольный параметр: '))
#     size_body_2 = int(input('Введите произвольный параметр: '))
#     size_body_3 = int(input('Введите произвольный параметр: '))
#     param_s[a] = size_body_1
#     param_s[b] = size_body_2
#     param_s[c] = size_body_3
#     print(param_s)
#
#
# print(square_body(figure_1=body_type, **param_s))
# --------------------------------------------------------------------

#  предыдущее с последующим

# def previous_subsequent(*args):
#     """""Складывает предыдущее значение с последующим"""
#     z = 0
#     for i  in args:
#         z += i
#         print(z, end=', ')
#     print()
# previous_subsequent(3, 9, 1)
# previous_subsequent(2, 5, 4, 2)
# previous_subsequent(3, 5, 10, 6, 3)
# -----------------------------------------------------------

#  произведение элементов

# def product(*args):
#     """""Произведение аргументов коллекции"""
#     interim = 1
#     list_element = []
#     list_num = []
#     for el in args:
#         if type(el) == int:
#             list_num.append(el)
#             interim *= el
#         else:
#             list_element.append(el)
#     if len(list_element) > 0:
#         print("Вводимые значения должны быть числами")
#     if len(list_num) == 0:
#         interim = None
#         print('Чисел нет')
#     else:
#         print("Произведение чисел:", end=' ')
#     return  interim
#
# print(product(10, 9))
# print(product(2, 3, 4))
# print(product("три", 'пять'))
# --------------------------------------------------------------

#  задача про области видимости

# s = 0
#
# def square(height, length, width):
#     def rectangle(x, y):
#         global s
#         s = x * y
#         return s
#
#     return 2 * (rectangle(height, length) + rectangle(height, width)
#                + rectangle(length, width))
#
#
# print(square(2, 4, 6))
# --------------------------------------------------


# def square(height, length, width):
#     s = 0
#
#     def rectangle(x, y):
#         nonlocal s
#         s = x * y
#         return s
#
#     return 2 * (rectangle(height, length) + rectangle(height, width)
#                + rectangle(length, width))
#
#
# print(square(2, 4, 6))
# ---------------------------------------------------


# def square(height, length, width):
#     def rectangle(x, y):
#         s = x * y
#         return s
#
#     return 2 * (rectangle(height, length) + rectangle(height, width)
#                + rectangle(length, width))
#
#
# print(square(2, 4, 6))
# -----------------------------------------------------------

#  увеличиваем значения аргументов на заданное число

# def increase(num):
#     def inner(x):
#         return num * x
#     return inner
#
# en = increase(2)
# print(en(15))
# -------------------------------------------------------

# lst1 = [1, 2, 3]
# lst2 = ['aa', 'vv']
# print(list(zip_longest(lst1, lst2, fillvalue=0)))
# ------------------------------------------------------

# a = 4
# b = 8
# c = 34
# d = (lambda x, y, z: x * y * z)
# print(d(a, b, c))
# print((lambda x, y, z: x * y * z)(a, b,c))
# -----------------------------------------------


# list_stud = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nicolas', 'final': 98}
# ]
# print(sorted(list_stud, key=lambda x: x['name']))
# print(sorted(list_stud, key=lambda x: x['final'], reverse=True))
# print('C макс-ой', (sorted(list_stud, key=lambda x: x['final'], reverse=True))[0])
# print('C минимальной', (sorted(list_stud, key=lambda x: x['final']))[0])
# ---------------------------------

# list_number = [3, 5, 7, 9, 5, 7, 2]
# product = list(map(lambda x: (x ** 2, x ** 3), list_number))
# print(product)
# -----------------------------------------------

# def decor(fn):
#     def wrap(*args):
#
#         a = ''
#         for i in args:
#             a  += str(i) + ", "
#         print("Сумма чисел:", a[:-2], "=", str(fn(*args)))
#         print( "Среднее арифметическое чисел:", a[:-2], "=",  fn(*args) / len(list(args)))
#     return wrap
#
#
# @decor
# def cum(*args):
#     return sum(list(map(lambda x: x, args)))
#
# cum(2, 3, 4, 5)
# -------------------------------------------------------------------


# def conversion_to_binary():
#     """
#     Преобразует целое десятичное число в двоичное число
#
#     :return: число в двоичной системе
#     """
#     s = ''
#     n = int(input("Введите целое число для преобразования в двоичную систему число: "))
#     try:
#         type(n) == int
#     except (TypeError, ValueError):
#         print("Число должно быть целым и не строкой")
#         n = int(input("Введите число ещё раз: "))
#
#     while n:
#         s += str(n % 2)
#         n //= 2
#     print(s[::-1], end='')
#
# def again():
#     z = int(input('Число кроме нуля: начать, ноль - стоп: '))
#     while z != 0:
#         conversion_to_binary()
#         z = int(input('\nЧисло кроме нуля: продолжить, ноль - стоп: '))
#     else:
#         return
#
# again()
# ------------------------------------------------------------------

# st_r = 'ст(рока символов, среди которых есть одна открыв)ающаяся'
# str_new = st_r.lstrip('ст(').rstrip(')ающяс')
# print(str_new)
# -------------------------------------------------------------

# Замена подстроки на подстроку

# str_old = input("Строка: ")
# str_replace = input('Какую подстроку Вы хотите заменить? ')
# substring = input('На что хотите заменить? ')
# new = []
# a = ''

# for i in  range(len(list(str_old))):
#     if list(str_old)[i] != ' ':
#         a += list(str_old)[i]
#     else:
#         new.append(a)
#         a = ''
# for j in range(len(new)):
#     if new[j] == str_replace:
#         new[j] = substring
# s = ''
# for i in new:
#     s += (str(i) + ' ')
#
# print("Получилось:", s)

# правильное решение
# i = str_old.find(str_replace)
# while i != -1:
#     l = len(str_replace)
#     str_old = str_old[0:i] + substring + str_old[i + l:]
#     i = str_old.find(str_replace)
#
# print(str_old)

# самое короткое решение

# print(str_old.replace(str_replace, substring))


# ------------------------------------------------------------

# Найти слова, начинающиеся на букву "е"
#
# test = """Ежевику для ежей
#         приносили два ежа.
#         Ежевику еле-еле
#         ежата возле ели съели
# """
#
# print(test.title().count('Е'))
# print(test.title())

# ----------------------------------------------------
# import re
#
# test = """Замените в этой строке все появления буквы 'о' на букву 'О',
#  кроме первого и последнего вхождения"""
#
# reg = 'о'
# reg1 = 'О'


# test = (re.sub(reg, 'О', test))  # замена "о" на "О"
# print(test)
# print(re.search(reg1, test).start())  # индекс первого вхождения "О"
# print(test.rfind(reg1))  # индекс последнего вхождения "О"
#
# test = (test[:re.search(reg1, test).start()] + 'о'
#         + test[re.search(reg1, test).end():test.rfind(reg1)]
#         + 'о' + test[test.rfind(reg1) + 1:])

# 2-й вариант
# test1 = test[:re.search(reg, test).start() +1]
# test2 = test[re.search(reg, test).start() + 1:test.rfind(reg)]
# test3 = test[test.rfind(reg):]
# test = test1 + re.sub(reg, 'О', test2) + test3
#
# print(test)
# ---------------------------------------------------------------
# import re
#
# roman_numeral = "MCXIII"
#
# def roman_numeral_check(m):
#     stencil = re.findall(r'''
#     ^(M{0,3})?
#     (CM|CD|D?C{0,3})?
#     (XC|XL|L?X{0,3})?
#     (IX|IV|V?I{0,3})?$''', m, re.VERBOSE)
#     r_n = []
#     for i in stencil:
#         r_n += i
#     if m == ''.join(r_n):
#         print('yes')
#     else:
#         print('no')


# roman_numeral_check(roman_numeral)
#----------------------------------------------------

# пароль должен содержать цифры, буквы англ-го алфавита, "-", "_", @

# password = 'my_p@sswOrd345-23'
# sample = re.findall(r'^[\d\w@-]{6,18}$', password)
# print(sample)
#
# def check_password(line):
#     if re.findall(r'^[\d\w@-]{6,18}$', line, re.ASCII):
#         print('Пароль написан корректно')
#     else:
#         print('Лучше придумать другой пароль')
#
# check_password(password)

# import re
#
# roman_numeral = "MCXIIII"
#
# def roman_numeral_check(m):
#     stencil = re.findall(r'''
#     ^(?:M{0,3})?
#     (?:CM|CD|D?C{0,3})?
#     (?:XC|XL|L?X{0,3})?
#     (?:IX|IV|V?I{0,3})?$''', m, re.VERBOSE)
#
#     if stencil:
#         print('yes')
#     else:
#         print('no')
#
#
# roman_numeral_check(roman_numeral)
#-------------------------------------------------------------
# import re
#
# data = '10-02-2021'
# sample = r'^(0[1-9]|[1-2][0-9]|30|31)-(0[1-9]|1[0-2])-(195[0-9]|20[0-2][0-5])?'
# result = re.findall(sample, data)
# print(result)
#
#
# def check_of_data(arg):
#     """Проверка правильности ввода числа, месяца и года"""
#     check_of_day = re.findall(r'^(0[1-9]|[1-2][0-9]|30|31-)?', arg)
#     if check_of_day == ['']:
#         print('Неправильно введено число')
#     check_of_month = re.findall(r'-(0[1-9]|1[0-2])-', arg)
#     if check_of_month == ['']:
#         print('Неправильно введен месяц')
#     check_of_year = re.findall(r'-(195[0-9]|20[0-2][0-5])', arg)
#     if check_of_year == ['']:
#         print('Неправильно введён год')
#     if check_of_month == ['02'] and check_of_day == ['30'] or check_of_day ==['31']:
#         print('В феврале не бывает столько дней')
#     else:
#         print('Дата введена правильно')
#
#
# check_of_data(data)
#---------------------------------------------------------------------------

# проверка валидности номера телефона

# phone_number1 = '+7 499 456 - 45 78'
# phone_number2 = '+74994564578'
# phone_number3 = '7 (499)4564578'
# phone_number4 = '7 (499) 456- 45- 78'
#
# reg = r'^[+]?7\s*\(*[0-9]{3}\s*\)*\s*[0-9]{3}\s*\-*\s*[0-9]{2}\s*\-*\s*[0-9]{2}?'
# print(re.findall(reg, phone_number1))
# print(re.findall(reg, phone_number2))
# print(re.findall(reg, phone_number3))
# print(re.findall(reg, phone_number4))













