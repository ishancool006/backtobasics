class DB2:
    def __init__(self, parameters):
        self.name = "DB2"
        self.parameters = parameters
        print("DB2 Connection")

    def execute(self, query):
        print("DB2 Execute")
        return "count"



class DB2Proxy:
    def __init__(self, parameters):
        self.name = "DB2 Proxy"
        self.parameters = parameters
        self.db2 = None
        self.cached_result = None

    def execute(self, query):
        if self.db2 is None:
            self.db2 = DB2(self.parameters)
            self.cached_result = self.db2.execute(query)

        return self.cached_result



def show_some_results():
    proxy_object = DB2Proxy("parameters")
    results = proxy_object.execute("count")
    print(results)
    results = proxy_object.execute("count")
    print(results)

if __name__ == "__main__":
    show_some_results()
