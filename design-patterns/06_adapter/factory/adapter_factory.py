from analytics.adappters.base_adapter import BaseAdapter
from analytics.adappters.db2_adapter import DB2Adapter
from analytics.adappters.mysql_adapter import MySqlAdapter
from analytics.adappters.oracle_adapter import OracleAdapter
from analytics.adappters.postgres_adapter import PostgreSQLAdapter

import analytics.properties.config as config


class DBFactory:
    @staticmethod
    def create():
        adapter = globals()[config.db + "Adapter"]
        return adapter()
