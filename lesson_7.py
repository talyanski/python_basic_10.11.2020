#  lesson_7

# class MyClass:
#     def __init__(self, p_1, p_2):
#         self.p_1 = p_1
#         self.p_2 = p_2
#     # def __del__(self):
#     #     print("Объект удален")
#
#     def __add__(self, other): #  78 + 88
#         return MyClass(self.p_1 + other.p_1, self.p_2 + other.p_2)  # возвращает объект
#
#     def __str__(self):
#         return f"params: 1 - {self.p_1}, 2 - {self.p_2} "
#
#
# #     print("Объект удален")
#
# my_1 = MyClass(78, 87)
# my_2 = MyClass(88, 98)
# my_3 = MyClass(88, 98)
# # del my_1 # ручной вызов мусорщика
# print(my_1 + my_2 + my_3)


# class MyClass:
#     def __init__(self, p_1):
#         self.p_1 = p_1
#
#     def __call__(self, new_p):
#         self.p_1 = new_p
#
#     def __str__(self):
#         return f"params: 1 - {self.p_1}"
#
#
# my_1 = MyClass(78)
# my_2 = MyClass(88)
# print(my_1, my_2)
#
# print()
# my_1("one")
# my_2("two")
# print(my_1, my_2)

# from abc import ABC, abstractmethod
#
# class MyOwnABC(ABC):
#     @abstractmethod
#     def m_1(self):
#         pass
#
#     @abstractmethod
#     def m_2(self):
#         pass
#
# class MyClass(MyOwnABC):
#     def m_1(self):
#         pass
#
#     def m_2(self):
#         pass


# my_1 = MyClass()

# class Iterator:
#     def __init__(self, start=0):
#         self.i = start
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
#
# class IterObj:
#     def __init__(self, start=0):
#         self.start = start - 1
#
#     def __iter__(self):
#         return Iterator(self.start)
#
#
# obj = IterObj(2)
# for el in obj:
#     print(el)

# class Iter:
#     def __init__(self, start=0):
#         self.i = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
#
# obj = Iter(2)
# for el in obj:
#     print(el)
#
# print()
#
# obj_1 = Iter()
# for el in obj_1:
#     print(el)
#
# print()

# для второй задачи:

# class Auto:
#     def __init__(self, year):
#         self.year = year
#
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self, year):
#         if year < 2000:
#             self.__year = 2000
#         elif year > 2019:
#             self.__year = 2019
#         else:
#             self.__year = year
#
#     def get_auto_year(self):
#         return  f"Авто выпущен в {str(self.year)} году"
#
# auto = Auto(19)
# print(auto.get_auto_year())


# контейнерная технология расчет оклеиваемой площади без окон и дверей
class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height

class Room:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []

    def add_win_dor(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square

room = Room(7, 4, 3.7)
print(room.square)

room.add_win_dor(2, 2)
room.add_win_dor(2, 2)
room.add_win_dor(2, 2)
print(room.common_square())