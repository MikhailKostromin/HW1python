# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
# проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# РЕШЕНИЕ

# a = int(input('введите день недели: '))
# if a > 5:
#     print('Выходной')
# else:
#     print('Рабочий')

# =============================
# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# not(X or Y or Z) = notX and notY and notZ

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            result1 = not (x or y or z)
            result2 = not x and not y and not z
            if result1 == result2:
                print(result1, '=', result2, '= Утверждение истинно')
            else:
                print(result1, '=', result2, '= Утверждение ложно')

# =======================================

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# РЕШЕНИЕ

# x = int(input('введите координаты точки x: '))
# y = int(input('введите координаты точки y: '))
# if x>0 and y>0:
#     print('Первая четверть')
# if x<0 and y>0:
#     print('Вторая четверть')
# if x<0 and y<0:
#     print('Третья четверть')
# if x>0 and y<0:
#     print('Четвертая четверть')
# else:
#     print('Нужно вводить числа больше или меньше нуля')

# =======================================================

# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).
# РЕШЕНИЕ

# x = int(input('Введите номер четверти: '))
# if x==1:
#     print('Диапозон возможных точек x>0, y>0')
# if x==2:
#     print('Диапозон возможных точек x<0, y>0')
# if x==3:
#     print('Диапозон возможных точек x<0, y<0')
# if x==4:
#     print('Диапозон возможных точек x>0, y<0')
# if x>4 or x<=0:
#     print('Указанной четверти нет')

# =======================================================
# Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# РЕШЕНИЕ
# x1 = int (input('Введите X координату первой точки А: '))
# y1 = int (input('Введите Y координату первой точким А: '))
# x2 = int (input('Введите X координату второй точки В: '))
# y2 = int (input('Введите Y координату второй точким В: '))
# distance = print('Расстояние',round(math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)),2))
