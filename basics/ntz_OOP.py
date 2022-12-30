class SuperHouse:
    # константа - условная неизменяемая переменная
    FOUNDATION = 'strip'
    roof = 'шифер'

    # конструктор
    def __init__(self, floor):
        self._square = 15
        # скрытый атрибут
        self._floor = floor
        # приватный атрибут
        self.__wall = 'кирпич'
        print("Дом с заданными параметрами построен в классе SuperHouse")

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, set_square):
        if set_square < 15:
            self._square = 15
        elif set_square > 100:
            self._square = 100
        else:
            self._square = set_square

    @property
    def wall(self):
        return self.__wall

    @wall.setter
    def wall(self, wall):
        self.__wall = wall

    def build_balcony(self, i):
        self._square -= i

    def build_roof(self):
        print('Построили крышу с помощью материала - ' + self.roof + '. В классе SuperHouse')


class House(SuperHouse):
    def __init__(self, floor):
        super().__init__(floor)
        print("Дом с заданными параметрами построен в классе House")

    # полиморфизм - переопределение метода родительского класса
    def build_roof(self):
        print('Построили крышу с помощью материала - ' + self.roof + '. В классе House')

    def build_balcony(self, i):
        self._square -= i


house = House(3)
house.build_balcony(5)
print(house.square)

print(type(house))





# my_house = House(3)
#
# print(my_house)
#
# my_house.wall = 'брус'
# print(my_house.wall)
#
# my_house.square = 100
# print(my_house.square)

# # обращение к скрытому атрибуту
# print(my_house._wall)
# # обращение к приватному атрибуту
# print(my_house._House__wall)

# print(my_house.square)
# my_house.build_balcony(10)
# print(my_house.square)
# print(type(my_house))
# my_house.build_roof()
