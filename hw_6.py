# Homework 6:

#  1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
#  зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
#  (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
#  (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

from time import sleep

class TrafficLight:
    __color = "Выключен"

    def running(self):
        try:
            count_left = (int(input("Введите количество циклов светофора: ")))
            while count_left > 0:
                print("\033[31m{}".format("Светофор горит красным"))
                sleep(7)
                print("\033[33m{}".format("Светофор горит желтым"))
                sleep(2)
                print("\033[32m{}".format("Светофор горит зеленым"))
                sleep(7)
                print("\033[33m{}".format("Светофор горит желтым\033[30m"))
                sleep(2)
                count_left -= 1
        except ValueError:
            print('Это не число. Выходим.')


light = TrafficLight()
light.running()

#  2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#  Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
#  Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#  Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
#  толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#  Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, lenght, width, mass=25, thickness=5):
        self._lenght = lenght
        self._width = width
        self.mass = mass
        self.thickness = thickness

    def calculate(self):
        print(f"\nмасса асфальта, необходимая для покрытия дороги длинной \033[31m{self._lenght}\033[30m м и шириной"
              f" \033[31m{self._width}\033[30m м\n"
              f"равна \033[31m{int((self._lenght * self._width * self.mass * self.thickness) / 1000)}\033[30m тонн\n")


road = Road(5000, 20)
road.calculate()

#  3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
#  income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
#  например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
#  реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
#  атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"


    def get_total_income(self):
        return f"{sum(self._income.values())}"


woker = Position("Alex", "Talyanski", "SEO", 2000, 500)
print(f'сотрудник\033[34m {woker.get_full_name()}\033[30m доход и премия\033[31m {woker.get_total_income()}\033[30m $')
woker = Position("Mark", "Ronin", "manager", 1000, 100)
print(f'сотрудник\033[34m {woker.get_full_name()}\033[30m доход и премия\033[31m {woker.get_total_income()}\033[30m $')

#  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
#  А также методы: go, stop, turn(direction), кот-е должны сообщать, что машина поехала, остановилась, повернула (куда).
#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
#  который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#  Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#  Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"машина {self.name} поехала")


    def stop(self):
        print(f"машина {self.name} остановилась")


    def turn(self, direction):
        if direction == "left":
            print(f"машина {self.name} повернула налево")
        elif direction == "right":
            print(f"машина {self.name} повернула направо")
        else:
            print(f"машина {self.name} едет прямо")

    def show_speed(self):
        if self.speed > 0:
            print(f"машина {self.name} едет со скоростью: {self.speed}")
        else:
            print(f"машина {self.name} стоит")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} {self.color} цвета привысил скорость на {(self.speed - 60)} км/ч, разрещенная 60 км\ч")
        else:
            print(f"машина {self.name} скорость {self.speed} км/ч)")


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} {self.color} цвета привысил скорость на {(self.speed - 40)}км/ч, разрещенная 40 км\ч)")
        else:
            print(f"{self.name} {self.color} цвета скорость {self.speed} км/ч)")


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


print("----------------1------------------")
my_car = TownCar("Автобусик", "Желтого", 70)
my_car.go()
my_car.turn("left")
my_car.show_speed()
my_car.stop()
print("----------------2------------------")
my_car = TownCar("Автобус", "Белого", 55)
my_car.go()
my_car.turn("left")
my_car.show_speed()
my_car.stop()

print("----------------3------------------")
my_car = SportCar("Ferrari", "Красного", 140)
my_car.go()
my_car.turn(0)
my_car.show_speed()
my_car.stop()
print("----------------4------------------")
my_car = WorkCar("Трактор", "Красного", 55)
my_car.go()
my_car.turn("left")
my_car.turn("right")
my_car.turn(0)
my_car.show_speed()
my_car.stop()
print("----------------5------------------")
my_car = WorkCar("Снегоуборщик", "Оранжевого", 15)
my_car.go()
my_car.turn("left")
my_car.turn(0)
my_car.turn("right")
my_car.turn(0)
my_car.turn("left")
my_car.turn(0)
my_car.show_speed()
my_car.stop()
print("-----------------6-----------------")
my_car = PoliceCar("Полицейский Ford", "Сенего", 60)
my_car.go()
my_car.turn(0)
my_car.show_speed()
my_car.stop()
print("----------------end----------------")

#  5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
#  (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
#  Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
#  выводить уникальное сообщение. Создать экз-ры классов и проверить, что выведет опис-ый метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("запуск отрисовки", self.title)


class Pen(Stationery):
    def draw(self):
        print(f"\033[31m запуск написания красной ручкой {self.title}\033[30m")

class Pencil(Stationery):
    def draw(self):
        print(f"\033[34m запуск шкрябанья синим карандашом {self.title}\033[30m")

class Handle(Stationery):
    def draw(self):
        print(f"\033[42m запуск выделения зеленым маркером {self.title}\033[30m")

print("-------обращение к родительскому классу:-------")
father = Stationery("какой-то строчки")
father.draw()
print()
print("-------обращение к первому дочернему классу:----")
pen = Pen("строки")
pen.draw()
print()
print("-------обращение ко второму дочернему классу:----")
pencil = Pencil("по странице")
pencil.draw()
print()
print("-------обращение к третьему дочернему классу:----")
handle = Handle("всей строчки")
handle.draw()
