"""
- The one constant in software development
- Encapsulate what varies/Separating what changes from what stays the same
- OCP
- Programming to an interface, not to a implementation (not applicable in Python)
- Duck example
"""


class Duck:
    def __init__(self, fly):
        self._fly = fly

    def quack(self):
        print(f"{type(self)} quacking")

    def swim(self):
        print(f"{type(self)} swimming")

    def display(self):
        pass

    def fly(self):
        self._fly()


class RedHeadDuck(Duck):
    def display(self):
        pass


class RubberDuck(Duck):
    def display(self):
        pass


class WoodenDuck(Duck):
    def display(self):
        pass


# behaviour
def fly():
    print("flying")


def nofly():
    print("no flying")


if __name__ == "__main__":
    d1 = RedHeadDuck(fly)
    d1.fly()

    d2 = WoodenDuck(nofly)
    d2.fly()
