class House:

    roof = 'шифер'
    # конструктор
    def __init__(self, square, floor, wall):
        self.square = square
        self.floor = floor
        self.wall = wall
        print("Дом с заданными параметрами построен")

    def build_balcony(self, i):
        self.square -= i

    def build_roof(self):
        print('Построили крышу с помощью материала - ' + self.roof)


my_house = House(100, 3, 'кирпич')
print(my_house.square)
my_house.build_balcony(10)
print(my_house.square)
print(type(my_house))
my_house.build_roof()
