print("\033[H\033[J", end="")
'''
Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один 
разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Выведите yes или no соответственно.
'''
a = int(input('Введите число a, первую сторону исходного прямоугольника: '))
b = int(input('Введите число b, вторую сторону исходного прямоугольника: '))
c = int(input('Введите число c, кол-во отламываемых долек: '))
if (c%a == 0 or c%b == 0) and c <= a*b:
    print('yes')
else: print('no')