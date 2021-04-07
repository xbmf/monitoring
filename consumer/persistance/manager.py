import logging

import psycopg2
import psycopg2.extras

from config import config
from persistance import IManager, IConnectionProvider

logger = logging.getLogger()


class PostgresConnectionProvider(IConnectionProvider):
    def connect(self):
        try:
            return psycopg2.connect(
                database=config.DB_NAME,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                host=config.DB_HOST,
                port=config.DB_PORT,
            )
        except (Exception, psycopg2.DatabaseError) as error:
            logger.exception(error)
            raise error


class PostgreDbManager(IManager):
    def __init__(self):
        self.connection_provider = PostgresConnectionProvider()

    def read_one(self, query, params=()) -> dict:
        connection, cursor = None, None
        try:
            connection = self.connection_provider.connect()
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(query, params)
            return cursor.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
            raise error
        finally:
            if connection is not None:
                connection.close()
                cursor.close()

    def execute_update(self, query, params=()) -> int:
        connection, cursor = None, None
        result = 0
        try:
            connection = self.connection_provider.connect()
            cursor = connection.cursor()
            cursor.execute(query, params)
            result = cursor.rowcount
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
            raise error
        finally:
            if connection is not None:
                connection.close()
                cursor.close()
            return result

    def clean(self, initial_sql: str):
        return self.execute_update(initial_sql)
