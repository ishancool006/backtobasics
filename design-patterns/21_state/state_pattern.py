import abc


class State(metaclass=abc.ABCMeta):
    def insert(self, atm):
        raise NotImplementedError

    def eject(self, atm):
        raise NotImplementedError


class HasCard(State):
    def insert(self, atm):
        print("Error : card already present")

    def eject(self, atm):
        print("ok")
        atm.state = NoCard()


class NoCard(State):
    def eject(self, atm):
        print("Error : no card")

    def insert(self, atm):
        print("ok")
        atm.state = HasCard()


class ATM:
    def __init__(self):
        self.state = NoCard()

    def insert(self):
        self.state.insert(self)

    def eject(self):
        self.state.eject(self)


if __name__ == "__main__":
    atm = ATM()
    atm.eject()  # default state is no card error no card
    atm.insert()  # ok state is has card
    atm.insert()  # error  card already in
    atm.eject()  # ok  state become no card
    atm.eject()  # error no card
