# перечисления - набор ограниченных неизменяемых значений, которые можно присвоить переменной
from enum import Enum


# перечисления - списки
class Season(Enum):
    Winter = ['January', 'February', 'December']
    Spring = ['March', 'April', 'May']
    Summer = ['June', 'July', 'August']
    Autumn = ['September', 'October', 'November']


for season in Season:
    print(f'Время года: {season.name}')
    for month in season.value:
        print(f'Месяц: {month}')


class Days(Enum):
    Monday = (1, 'Понедельник')
    Tuesday = (2, 'Вторник')
    Wednesday = (3, 'Среда')
    Thursday = (4, 'Четверг')
    Friday = (5, 'Пятница')
    Saturday = (6, 'Суббота')
    Sunday = (7, 'Воскресенье')

    def __init__(self, id, russian):
        self.id = id
        self.russian = russian


class Month(Enum):
    January = 1  # Январь
    February = 2  # Февраль
    March = 3  # Март
    April = 4  # Апрель
    May = 5  # Май
    June = 6  # Июнь
    July = 7  # Июль
    August = 8  # Август
    September = 9  # Сентябрь
    October = 10  # Октябрь
    November = 11  # Ноябрь
    December = 12  # Декабрь


for month in Month:
    print(f'{month.name} это {month.value} месяц.')

for day in Days:
    print(f'{day.name} это {day.id} день недели. На русском - {day.russian}')
