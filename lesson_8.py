class MyClass:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    # def m_1(self):
    #     # return self.m_2()  #  или return MyClass.m_2()  # обращение к m_2
    #     print("hi-end")
    #     # return self.m_3() # или return MyClass.m_3()
    #
    #
    # @staticmethod
    # def m_2():
    #     # return MyClass().m_1() # обращение к m_1
    #     print(MyClass(88).p)
    #
    # @classmethod
    # def m_3(cls):
    #     return cls(78).m_1()
    @classmethod
    def fio(cls, data):
        name, surname = data
        return cls(name, surname)
    @staticmethod
    def get_fio(obj):
        return f"all name: {obj.name} {obj.surname}"
my_list = ["Ms", "Lu"]

my_1 = MyClass.fio(my_list)
print(my_1.get_fio(my_1))
print()

# print(MyClass.__name__)
# print(MyClass.__module__)
# print(MyClass.__doc__)
# print(MyClass.__init__)
# print(MyClass.__dict__)



my_1.m_3()

my_1.m_1  ()
my_1.m_2()
MyClass.m_3()

