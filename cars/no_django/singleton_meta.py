
class SingletonMeta(type):
    instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instance:
            cls.instance[cls] = super().__call__(*args, **kwargs)
        return cls.instance[cls]


class SomeClass(metaclass=SingletonMeta):
    ...


a = SomeClass()
b = SomeClass()
print(a)
print(b)
print(a is b)

