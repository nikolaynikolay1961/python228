#  Задача № 1
# lst = [int(input('-> ')) for _ in range(int(input('Кол-во эл-тов: ')))]
# print(lst)
# positive = []
# for a in lst:
#     if a > 0:
#         positive.append(a)
# print('Список с положительными элементами: ', positive)
# m = 0
# for i in range(len(positive) - 1):
#     m = positive[i] if positive[i] > positive[i + 1] else positive[i + 1]
# print('Максимальное число: ', m)

#  Задача № 2
# sps = [int(input('-> ')) for _ in range(int(input('Кол-во эл-тов: ')))]
# print(sps)
# c = input("Какой эл-т вставить: ")
# k = int(input('по какому индексу вставить эл-т: '))
# con = [int(i) for i in range(len(sps))]
#
# if k in con:
#     sps.insert(k, c)
#     print('Новый список: ', sps)
# else:
#     print('Такого индекса нет, список без изменений')


#  Задача № 3
# sps = [int(input('-> ')) for _ in range(int(input('Кол-во эл-тов: ')))]
# print(sps)
# z = int(input('Какое число хотите проверить? '))
# if z in sps:
#     print('Число входит в список')
# else:
#     print('Число не входит в список')


# from random import randint, randrange

# задача № 1 из урока 14
# sort_sps = [randint(-10,10) for i in range(11)]
# print('Начальный список:', sort_sps)
# print("Сортированный список:", sorted(sort_sps, reverse=True))

# задача № 2 из урока 14
# num_sps = [randint(1, 40) for i in range(20)]
# print(num_sps)
# sum_sps = 0
# for el in num_sps:
#     sum_sps += a
# print('Summa:', sum_sps)

# задача № 3 из урока 14
# inp_cps= [int(input('-> ')) for i in range(int(input('Обозначьте число элементов: ')))]
# print(inp_cps)
# k = int(input('Какой элемент хотите убрать? -> '))
# new_sp = []
#
# # for i in range(len(inp_cps)):
# #     if inp_cps[i] != k:
# #        new_sp.append(inp_cps[i])
#
# for el in inp_cps:
#     if el != k:
#         new_sp.append(el)
# print(new_sp)
# ------------------------------------------

#      разворачиваем матрицу
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20]
# ]
# for el in matrix:
#     for z in el:
#         print(z, end='\t')
#     print()
# print()
# q = len(matrix)
# z = len(matrix[q - 1])
# print(q)
# print(z)
# for i in range(z):
#     for d in range(q):
#         print(matrix[d][i], end='\t')
#     print()
# ----------------------------------------

#  Задача: замена строки в матрице

# sps = [[randint(0, 10) for i in range(6)] for j in range(6)]
# for el in sps:
#     for b in el:
#         print(b, end='\t')
#     print()
# print()
# sp_change = [randint(0, 10) for i in range(6)]  # строка для замены
# print(sp_change)
# for d in range(len(sps)):
#     if d % 2 == 0:
#         sps[d] = sp_change
# print()
# for el in sps:
#     for b in el:
#         print(b, end='\t')
#     print()
# ------------------------------------

# list_num = [i for i in range(1, 21)]
# print(list_num)
# --------------------------------------

# lst_mil = [i for i in range(1, 1_000_001)]
# print(max(lst_mil))
# print(min(lst_mil))
# print(sum(lst_mil))
# ---------------------------------

# print([i for i in range(1, 21, 2)])
#
# for i in range(1, 21, 2):
#     print(i, end=' ')
# -------------------------------------

# lst_multiple_of_three = [i for i in range(3, 31, 3)]
# for element in lst_multiple_of_three:
#     print(element, end=' ')
# ----------------------------------

# list_of_cubes = [i ** 3 for i in range(1, 11)]
# for element in list_of_cubes:
#     print(element, end=' ')

# -----------------------------------------------

#  статистика частотности
# tuple_period = tuple(input('Введите по порядку, без пробелов, элементы кортежа: '))
#
# def frequency_number(block):
#     """находим количество повторений элемента в кортеже"""
#     assistant_list = []
#     for element in block:
#         if element not in assistant_list:
#             assistant_list.append(element)
#     for el in assistant_list:
#         print('Количество', el + ':', block.count(el))
#
# frequency_number(tuple_period)
# ---------------------------------------------

#  Наибольшее число, кратное 13-ти

# def multiplicity_num(enumeration):
#     """Наибольшее число, кратное 13-ти"""
#     sps = []
#     for num in enumeration:
#         if num % 13 == 0 and num > 0:
#             sps.append(num)
#     if not sps:
#         return 'Нет'
#
#     return max(sps)
#
#
# print(multiplicity_num((2, 7, 0, 3, 1, 5, -13, 1)))
# print(multiplicity_num((2, 7, 0, 3, 1, 5, -13, 13)))
# print(multiplicity_num((26,)))
# print(multiplicity_num((99, 99, 100, 34, -39)))
# print(multiplicity_num((99, 39, 99, 100, 34)))
#------------------------------------

#  вхождение элемента в кортеж

# def entry(sps, element):
#     if element in sps:
#         return 'Yes'
#     else:
#         return 'Noy'
#
#
# example = ('ab', 'abcd', 'cde', 'abc', 'def')
# unit = 'ab'
# print(entry(example, unit))
























