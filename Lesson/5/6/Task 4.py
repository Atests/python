'''
    Реализуйте базовый класс Car. 
    У данного класса должны быть следующие атрибуты: 
    speed, color, name, is_police (булево). 
    А также методы: go, stop, turn(direction), которые должны сообщать, 
    что машина поехала, остановилась, повернула (куда). 
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
    Добавьте в базовый класс метод show_speed, 
    который должен показывать текущую скорость автомобиля. 
    Для классов TownCar и WorkCar переопределите метод show_speed. 
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться 
    сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stop')

    def turn_right(self):
        print(f'{self.name} turned right')

    def turn_left(self):
        print(f'{self.name} turned left')

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'

car1 = Car(100, 'red', 'car1', False)
car1.go()
car1.stop()
print(car1.show_speed())

bmw = TownCar(100, 'black', 'BMW')
nissan = SportCar(200, 'red', 'NISSAN')
bugatti = WorkCar(10, 'blue','BUGATTI', True)
ferrari = PoliceCar(200, 'gray', 'FERRARI', True)


bmw.go()
print(bmw.show_speed())
print(nissan.show_speed())
print(bugatti.show_speed())
print(ferrari.show_speed())
print(ferrari.police())