"""
Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoped!'.format(self.name))

    def turn(self, direction):
        print('{} is tern to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Warning! speed is more max')
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Warning! speed is more max')
        print('Current speed:', self.speed)


class PoliceCar(Car):
    pass


town_car = TownCar(150, "Синяя машина", "Грузовая машина", False)
sport_car = SportCar(250, "Красная машина", "Споривная", False)
work_car = WorkCar(180, "Серая машина", "Рабочая", False)
police_car = PoliceCar(220, "Белая машина", "Копы", True)

town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn("Left")








