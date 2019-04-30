"""
- Interface to create objects, but defer object creation at run time
- Separation of creation vs usage
- First steps towards plugin arch
- e.g. ShapeFactory, Shape, Circle, Square
"""


class SuperHero:
    def action(self):
        pass


class IronMan(SuperHero):
    def action(self):
        print(f"{self.__class__.__name__} fighting..")


class Hulk(SuperHero):
    def action(self):
        print(f"{self.__class__.__name__} fighting..")


class AvengersFactory:
    d = {"fancy weapons": IronMan()}

    @staticmethod
    def create(power):
        return AvengersFactory.d[power]


if __name__ == "__main__":

    def save_city(heros):
        for h in heros:
            h.action()

    save_city([AvengersFactory.create("fancy weapons")])
