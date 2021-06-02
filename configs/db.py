import logging
import mysql.connector
from mysql.connector import Error, pooling
from datetime import datetime
import os

#logging.config.dictConfig(LOGGING)
logger = 'database' if os.getenv('ENVIRONMENT') != 'TEST' else 'test'
logger = logging.getLogger(logger)

# logger = logging.getLogger('database')

ENV = os.getenv('ENVIRONMENT')
logger.debug("environment from db: %s", ENV)

def db_conn():
    

    logger.debug("database used: %s", os.getenv('DB_DATABASE'))

    try:
        connection_config_dict = {
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': 3306,
            'database': os.getenv('DB_DATABASE'),
            'raise_on_warnings': True,
            'use_pure': False,
            'autocommit': True,
            'pool_size': 5,
            'pool_name':'pynative_pool',
            'pool_reset_session':True
        }
        # logger.debug("configs loaded: %s", connection_config_dict)

        # # check if connction already exists
        # print("Checking if connection already exists")
        # exists = mysql.connector.is_connected()
        # print("exists returns: ", exists)

        #connection = mysql.connector.connect(**connection_config_dict)
        connection_pool = mysql.connector.pooling.MySQLConnectionPool(**connection_config_dict)

        logger.info("Printing connection pool properties ")
        logger.debug("Connection Pool Name - %s", connection_pool.pool_name)
        logger.debug("Connection Pool Size - %s", connection_pool.pool_size)

        # Get connection object from a pool
        connection = connection_pool.get_connection()

        if connection.is_connected():
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
    except Error as e:
        logger.error("%s", str(e))
        exit("Error while connecting to MySQL", e)