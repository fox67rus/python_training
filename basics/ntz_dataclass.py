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
from dataclasses import dataclass


# data class
@dataclass
class Human:
    firstname: str
    lastname: str
    age: int
    year: int


human = Human("Alex", "Ivanov", 26, 1996)
print(human)
