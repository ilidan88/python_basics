"""Дан список, содержащий искажённые данные с должностями и именами сотрудников:
Известно, что имя сотрудника всегда в конце строки.
Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' Подумать,
как получить имена сотрудников из элементов списка, как привести их к корректному виду.
 Можно ли при этом не создавать новый список?"""

name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for name in name_list:
    name = name.split( )[-1]
    print(f'Привет, {name.title()}!')

#fff