class Oracle:
    def __init__(self):
        self.name = "Oracle"
        self.parameters = None

    def oracle_connect(self, parameters=None):
        self.parameters = parameters
        return "Oracle Connection"

    def oracle_execute(self, query):
        if query in ["min", "max", "count"]:
            return "Oracle execute"
        else:
            return "NotImplemented"