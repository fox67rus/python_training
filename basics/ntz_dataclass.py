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
    # не инициализировать и не получать значения
    fullname: str = field(init=False, repr=False)

    # формирование параметра после инициализации
    def __post_init__(self):
        self.fullname = self.lastname + " " + self.firstname


@dataclass()
class Additional:
    growth: int
    weight: int


@dataclass()
class Data:
    human: Human
    additional: Additional


def get_data(firstname, lastname, age, year, growth, weight) -> Data:
    data = Data(
        human=Human(
            firstname=firstname,
            lastname=lastname,
            age=age,
            year=year
        ),
        additional=Additional(
            growth=growth,
            weight=weight
        )
    )
    return data


get_values = get_data('Maxim', 'Sidorov', 25, 1997, 180, 70)
print(get_values)

# human = Human("Alex", "Ivanov", 26, 1996)
# print(human.fullname)
