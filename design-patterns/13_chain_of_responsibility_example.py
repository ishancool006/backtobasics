"""
Goal of Chain of Responsibility Design Pattern: To achieve loose coupling

A request from the client is passed to a chain of objects to process them.

Object in the chain will decide themselves who will be processing the request and whether the request is required
to be sent to the next object in the chain or not.

Object Oriented Version of IF-ELSE ladder

if
.....
elif
.....
elif
.....
else
....

"""


import abc


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def handle_request(self, request):
        pass


class UserAuthorizationHandler(Handler):
    """
    Handle request and forward it to the successor.
    """

    @staticmethod
    def is_authorized_user(request, authentication_criteria):
        if authentication_criteria:
            print("Valid User.....!")
            return True
        else:
            print("Invalid User.....!")
            return False

    def handle_request(self, request):
        auth = self.is_authorized_user(request, authentication_criteria=True)
        if auth == True:
            print("Request handled in authorization handler.....!\n")
            self._successor.handle_request(request)
            print("Passed the request to next handler....!")


class SecurityHandler(Handler):
    """
    Handle request and forward it to the successor.
    """

    @staticmethod
    def is_secure(request, security_criteria):
        if security_criteria:
            print("System is secure.....!")
            return True
        else:
            print("System is not secure....!")
            return False

    def handle_request(self, request):
        security = self.is_secure(request, security_criteria=True)
        print(security)
        if security:  # if can_handle:
            print("Request handled in security handler.....!\n")
            print("Passing the request to next handler....!")
            self._successor.handle_request(request)


class SystemAttackHandler(Handler):
    """
        Handle request and forward it to the successor.
    """

    def handle_request(self, request):
        print("Request handled in system attack handler.....!\n")
        self._successor.handle_request(request)
        print("Passed the request to next handler....!")


class CacheHandler(Handler):
    def handle_request(self, request):
        if True:  # if can_handle:
            print("Request handled in cache attack handler.....!\n")
            # self._successor.handle_request(request)
            print("Passed the request to next handler....!")


def main():
    requests = ["request1"]

    #     Handle the request before passing it to the ordering system
    user_authorization_handler = UserAuthorizationHandler()
    security_handler = SecurityHandler()
    system_attack_handler = SystemAttackHandler()
    cache_handler = CacheHandler()

    user_authorization_handler._successor = security_handler
    security_handler._successor = system_attack_handler
    system_attack_handler._successor = cache_handler

    for request in requests:
        user_authorization_handler.handle_request(request=request)


if __name__ == "__main__":
    main()
