class House:
    # константа - условная неизменяемая переменная
    FOUNDATION = 'strip'
    roof = 'шифер'

    # конструктор
    def __init__(self, floor):
        self.__square = 15
        # скрытый атрибут
        self._floor = floor
        # приватный атрибут
        self.__wall = 'кирпич'
        print("Дом с заданными параметрами построен")

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, set_square):
        if set_square < 15:
            self.__square = 15
        elif set_square > 100:
            self.__square = 100
        else:
            self.__square = set_square

    @property
    def wall(self):
        return self.__wall

    @wall.setter
    def wall(self, wall):
        self.__wall = wall

    def build_balcony(self, i):
        self.__square -= i

    def build_roof(self):
        print('Построили крышу с помощью материала - ' + self.roof)


my_house = House(3)

print(my_house)

my_house.wall = 'брус'
print(my_house.wall)

my_house.square = 100
print(my_house.square)

# # обращение к скрытому атрибуту
# print(my_house._wall)
# # обращение к приватному атрибуту
# print(my_house._House__wall)

# print(my_house.square)
# my_house.build_balcony(10)
# print(my_house.square)
# print(type(my_house))
# my_house.build_roof()
