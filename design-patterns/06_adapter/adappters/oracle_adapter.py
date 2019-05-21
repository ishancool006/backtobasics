from analytics.adappters.base_adapter import BaseAdapter
from analytics.drivers.oracle import Oracle
import analytics.properties.oracle_properties as properties


class OracleAdapter(BaseAdapter):
    def __init__(self):
        self.name = "OracleAdapter"
        self.driver = Oracle()

    def connect(self, parameters=None):
        return self.driver.oracle_connect(parameters)

    def execute(self, query):
        if getattr(properties, query):
            return self.driver.oracle_execute(query)
        else:
            return "OracleAdapter execute"
