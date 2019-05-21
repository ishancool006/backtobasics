class PostgreSQL:
    def __init__(self):
        self.name = "PostgreSQL"
        self.parameters = None

    def postgres_connect(self, parameters):
        self.parameters = parameters
        return "PostgreSQL Connection"

    def postgres_execute(self, query):
        if query is None:
            return "PostgreSQL execute"
        else:
            return NotImplemented