from analytics.adappters.base_adapter import BaseAdapter
from analytics.drivers.mysql import MySql
import analytics.properties.mysql_properties as properties

class MySqlAdapter(BaseAdapter):
    def __init__(self):
        self.name = "MySqlAdapter"
        self.driver = MySql()

    def connect(self, parameters=None):
        return self.driver.mysql_connect(parameters)

    def execute(self, query):
        if getattr(properties, query):
            return self.driver.mysql_execute(query)
        else:
            return "MySqlAdapter execute"