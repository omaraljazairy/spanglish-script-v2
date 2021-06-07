# from dataclasses import dataclass
import logging
from mysql.connector import Error, pooling
from datetime import datetime
import os

logger = 'database' if os.getenv('ENVIRONMENT') != 'TEST' else 'test'
logger = logging.getLogger(logger)

ENV = os.getenv('ENVIRONMENT')
logger.debug("environment from db: %s", ENV)

#@dataclass(frozen=True) # make sure the instance attributes are immutable
class DBConnection:
    """ Singletom DataClass holding the database connection. """

    def __init__(self) -> None:
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.database = os.getenv('DB_DATABASE')


    def get_connection(self):
        """ returns a mysql connector object. """
    
        logger.debug("database used: %s", os.getenv('DB_DATABASE'))
        try:
            connection_config_dict = {
                'user': self.user,
                'password': self.password,
                'host': self.host,
                'port': self.port,
                'database': self.database,
                'raise_on_warnings': True,
                'use_pure': False,
                'autocommit': True,
                'pool_size': 5,
                'pool_name':'pynative_pool',
                'pool_reset_session':True
            }
            logger.debug("configs loaded: %s", connection_config_dict)

            connection_pool = pooling.MySQLConnectionPool(**connection_config_dict)

            logger.info("Printing connection pool properties ")
            logger.debug("Connection Pool Name - %s", connection_pool.pool_name)
            logger.debug("Connection Pool Size - %s", connection_pool.pool_size)

            # Get connection object from a pool
            connection = connection_pool.get_connection()

            # check if connction already exists
            if connection.is_connected():
                logger.debug("connection exist")
                db_Info = connection.get_server_info()
                now = datetime.now()
                msg = "Connected to MySQL Server Version {} on {}".format(db_Info, now)
                logger.debug("%s", msg)

                ########### testing connection only #########
                cursor = connection.cursor()

                # ## executing the statement using 'execute()' method
                cursor.execute("SHOW DATABASES")

                # ## 'fetchall()' method fetches all the rows from the last executed statement
                databases = cursor.fetchall() ## it returns a list of all databases present

                # ## printing the list of databases
                print(databases)
                ######################### ######################
                return connection
            else:
                logger.error("connection does not exist")
                raise("No DB Connection")
        except Error as e:
            logger.error("%s", str(e))
            exit("Error while connecting to MySQL", e)
