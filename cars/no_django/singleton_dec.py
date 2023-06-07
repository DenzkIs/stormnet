# В базовом примере синглтона параметры менялись, объект оставался (надо переопределить __call__)
# С декоратором - параметры остаются как при первом вызове

def singleton_dec(some_class):  # оборачиваю класс в декоратор
    instance = {}  # завожу хранилище

    def wrapper(*args, **kwargs):
        if some_class not in instance.keys():  # если в instance нет ключей с именем класса
            instance[some_class] = some_class(*args, **kwargs)  # передаю туда класс с его параметрами (если есть)
        print(instance)

        return instance[some_class] # и возвращаю этот класс

    return wrapper


@singleton_dec
class Volume:
    def __init__(self, level):
        self.level = level


a = Volume(2)
b = Volume(1)
print(a.level)
print(b.level)
print(a is b)
