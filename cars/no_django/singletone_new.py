# Синглтон (реализация через базовый класс)

class SingletonBase:
    __instance = None  # ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # создаем объект
            print("Объект создается 1 раз!")
        return cls.__instance  # иначе объект уже создан и мы возвращаем созданный объект

    def __del__(self):
        print('Объект удалился!')
        SingletonBase.__instance = None  # Если объект удален, опять выставляем None

    def __init__(self, x=0, y=0):
        print("Вызов метода __init__ объекта " + str(self))
        self.x = x
        self.y = y


sb = SingletonBase(1, 1)
print(sb.x)
sb2 = SingletonBase(2, 2)
print(sb2.x)
sb3 = SingletonBase()
sb.__del__()
a = SingletonBase(3, 3)
print(a.x)


# class Logger:
#     @staticmethod
#     def get_instance():
#         if '_instance' not in Logger.__dict__:
#             Logger._instance = Logger()
#         return Logger._instance
#
#     def write_log(self, path):
#         pass
#
#
# if __name__ == "__main__":
#     s1 = Logger.get_instance()
#     s2 = Logger.get_instance()
#     assert s1 is s2
#     print(s1)
#     print(s2)
