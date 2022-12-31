# class Human:
#     def __init__(self, firstname, lastname, age, year):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.year = year
#
#
# human = Human("Alex", "Ivanov", 26, 1996)
#
# print(human.lastname)
from dataclasses import dataclass, field


# data class
@dataclass()
class Human:
    firstname: str = 'Ivan'
    lastname: str = 'Petrov'
    age: int = 20
    year: int = 2002
    # не инициилизировать и не получать значения
    fullname: str = field(init=False, repr=False)

    # формирование параметра после инициализации
    def __post_init__(self):
        self.fullname = self.lastname + " " + self.firstname


human = Human("Alex", "Ivanov", 26, 1996)
print(human.fullname)

