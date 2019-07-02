class MySql:
    def __init__(self):
        self.name = "MySql"
        self.parameters = None

    def mysql_connect(self, parameters=None):
        self.parameters = parameters
        return "MySql Connection"

    def mysql_execute(self, query):
        if query in ["min", "max"]:
            return "MySql execute"
        else:
            return "NotImplemented"
