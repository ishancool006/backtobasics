# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
# Creating Singleton using BaseClass


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    pass


print("Type of MyClass: ", type(MyClass))
assert MyClass() is MyClass()
