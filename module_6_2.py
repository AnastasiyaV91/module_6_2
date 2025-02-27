class Vehicle:
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner                           # владелец транспорта
        self.__model = model                         # модель(марка) транспорта
        self.__engine_power = engine_power           # мощность двигателя
        self.__color = color                         # название цвета

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())                      # Вывод в консоль возвращенного значения функции get_model()
        print(self.get_horsepower())                 # Вывод в консоль возвращенного значения функции get_horsepower()
        print(self.get_color())                      # Вывод в консоль возвращенного значения функции get_color()
        print(f"Владелец: {self.owner}")             # Вывод в консоль имени владельца

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:   # Поиск цвета в списке
            self.__color = new_color                     # Переопределения цвета
        else:
            print(f"Нельзя сменить цвет на {new_color}")  # Если цвета нет в списке, выводим сообщение в консоль

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()