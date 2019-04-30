"""
- When your code needs to work with various families of related products, but you don’t want it to depend on the
concrete classes of those products.
- ShapeFactory, 2DShapeFactory, Circle, Square, 3DShapeFactory, Sphere, Cube
- More ex: Black Theme/White Theme IDE
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


class SuperMan(SuperHero):
    def action(self):
        print(f"{self.__class__.__name__} fighting..")


class BatMan(SuperHero):
    def action(self):
        print(f"{self.__class__.__name__} fighting..")


class SuperHeroFactory:
    @staticmethod
    def create(league):
        if league == "avengers":
            return AvengersFactory()
        elif league == "justice league":
            return JusticeLeagueFactory()
        else:
            assert 0, "No Super Hero Factory found!"


class AvengersFactory:
    a = {"fancy weapons": IronMan()}

    def create(self, power):
        return AvengersFactory.a[power]


class JusticeLeagueFactory:
    jl = {"super power": SuperMan()}

    def create(self, power):
        return JusticeLeagueFactory.jl[power]


if __name__ == "__main__":

    def save_city(heros):
        for h in heros:
            h.action()

    save_city([SuperHeroFactory.create("avengers").create("fancy weapons")])
