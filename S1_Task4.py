print("\033[H\033[J", end="")
'''Задача №7. Решение в группах
Дано нат-число. Определить, яв-ся ли год с данным номером високосным. Если год високосный.
Напомним, что в соответствии с григорианским календарем, год является високосным, 
если его номер кратен 4, но не кратен 100, а также если он кратен 400.
Input: 2016
Output: YES      '''
year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Текущий год - високосный.')
else:
    print('Текущий год - не високосный.')
# ч/з Тернарный оператор:  print(Действие  ЕСЛИ  (условие)  ИНАЧЕ  (действие ес Условие = Ложь.))  if можно без скобок.
print('Текущий год - високосный.' if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else 'Нет.')