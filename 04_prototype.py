from abc import ABCMeta, abstractstaticmethod

import copy


class IPrototype(metaclass=ABCMeta):
    @abstractstaticmethod
    def clone(self):
        pass


class Users(IPrototype):
    def __init__(self):
        self.user_list = []

    def get_user_list(self):
        return self.user_list

    def insert_user(self):
        self.user_list.append("Tushar")
        self.user_list.append("Kshitij")
        self.user_list.append("Amar")
        self.user_list.append("Piyush")

    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    user = Users()
    user.insert_user()
    print(user.get_user_list())

    user1 = user.clone()
    user1.get_user_list().append("Swapnil")
    print(user1.get_user_list())

    user2 = user.clone()
    user2.get_user_list().remove("Amar")
    print(user2.get_user_list())
