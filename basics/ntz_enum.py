# перечисления - набор ограниченных неизменяемых значений, которые можно присвоить переменной
from enum import Enum


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


for day in Days:
    print(f'{day.name} это {day.id} день недели. На русском - {day.russian}')
