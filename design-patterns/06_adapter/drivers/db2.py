class DB2:
    def __init__(self):
        self.name = "DB2"
        self.parameters = None

    def db2_connect(self, parameters):
        self.parameters = parameters
        return "DB2 Connection"

    def db2_execute(self, query):
        if query in ["count"]:
            return "DB2 execute"
        else:
            return "NotImplemented"