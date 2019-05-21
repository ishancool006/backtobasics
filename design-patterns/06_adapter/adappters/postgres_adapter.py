from analytics.adappters.base_adapter import BaseAdapter
from analytics.drivers.postgres import PostgreSQL
import analytics.properties.postgres_properties as properties


class PostgreSQLAdapter(BaseAdapter):
    def __init__(self):
        self.name = "PostgreSQLAdapter"
        self.driver = PostgreSQL()

    def connect(self, parameters=None):
        return self.driver.postgres_connect(parameters)

    def execute(self, query):
        if getattr(properties, query):
            return self.driver.postgres_execute(query)
        else:
            return "PostgreSQLAdapter execute"
