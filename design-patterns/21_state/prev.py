# code before applying state pattern


class ATM:
    def __init__(self):
        self.card_present = False

    def insert(self):
        if self.card_present:
            print("Error : card already present")
        else:
            print("ok")
            self.card_present = True

    def eject(self):
        if self.card_present:
            print("ok")
            self.card_present = False
        else:
            print("Error : no card")


if __name__ == "__main__":
    atm = ATM()
    atm.eject()
    atm.insert()
    atm.insert()
    atm.eject()
    atm.eject()
