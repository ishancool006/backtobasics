# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
# Creating Singleton using Decorator


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class MyClass:
    pass


print("Type of MyClass: ", type(MyClass))
assert MyClass() is MyClass()
