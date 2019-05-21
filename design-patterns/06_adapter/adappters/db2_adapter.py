from analytics.adappters.base_adapter import BaseAdapter
from analytics.drivers.db2 import DB2
import analytics.properties.db2_properties as properties

class DB2Adapter(BaseAdapter):
    def __init__(self):
        self.name = "DB2Adapter"
        self.driver = DB2()

    def connect(self, parameters=None):
        return self.driver.db2_connect(parameters)

    def execute(self, query):
        if getattr(properties, query):
            return self.driver.db2_execute(query)
        else:
            return "DB2Adapter execute"