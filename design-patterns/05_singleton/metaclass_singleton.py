# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
# Creating Singleton using Metaclass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


print("Type of MyClass: ", type(MyClass))
assert MyClass() is MyClass()
