# Паттерн "Моносостояние"
# Гарантирует одинаковое состояние всех объектов, но объекты разные
# Где его применять на практике in field?

class MonoStateExample:
    __some_params = {
        'f': 'first_param',
        's': 2,
        't': {}
    }

    def __init__(self, x):
        self.__dict__ = self.__some_params
        self.x = x


a = MonoStateExample(1)
b = MonoStateExample(2)
a.id = 'new_attr_id'
a.f = 'i changed you'

print(a.__dict__)
print(a.x)
print(b.__dict__)
print(b.x)
