import logging
from typing import Dict, List
from services.dbconnection import DBConnection
from dataclasses import dataclass
from warnings import filterwarnings




@dataclass
class DBModel:
    """ this is the main model that interacts with the database. This is the database layer that will be
    used by other models to get and save data. """


    def __init__(self) -> None:
        self.dbconn: DBConnection = DBConnection() # initialize db instance.
        self.logger = logging.getLogger('dbmodels')



    def insert(self, sql:str, args: tuple) -> int:
        ''' take a query string with args and executes an insert query. 
        It will return the last inserted_id if successfully '''

        self.logger.debug("query received: %s", sql)
        self.logger.debug("args received: %s", args)
        
        conn = self.dbconn.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(sql, args)
            result = cursor.lastrowid
            self.logger.debug("data returned: %s", result)
            return result
        except Exception as e:
            self.logger.error("%s", str(e))
            conn.rollback()
        finally:
            cursor.close()
            self.logger.debug("cursur closed")
        


    def update(self, sql:str, args: tuple) -> int:
        ''' take a query string with args and executes an insert query. 
        It will return the number of effected numbers '''

        self.logger.debug("query received: %s", sql)
        self.logger.debug("args received: %s", args)
        
        conn = self.dbconn.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(sql, args)
            result = cursor.rowcount
            self.logger.debug("data returned: %s", result)
            return result
        except Exception as e:
            self.logger.error("%s", str(e))
            conn.rollback()
        finally:
            cursor.close()
            self.logger.debug("cursur closed")



    def fetch(self, sql:str, args: tuple) -> Dict:
        ''' takes a query string with a tuple of args, returns a dictionary '''

        self.logger.debug("query received: %s", sql)
        self.logger.debug("args received: %s", args)
        
        conn = self.dbconn.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(sql, args)
            data = cursor.fetchone()
            self.logger.debug("data returned: %s", data)
            return data
        except Exception as e:
            self.logger.error("%s", str(e))
        finally:
            cursor.close()
            self.logger.debug("cursur closed")


    def fetch_all(self, sql:str, args: tuple) -> List[Dict]:
        ''' takes a query string with a list of args, returns a list of dictionary '''

        self.logger.debug("query received: %s", sql)
        self.logger.debug("args received: %s", args)
        
        conn = self.dbconn.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(sql, args)
            data = cursor.fetchall()
            self.logger.debug("data returned: %s", data)
            return data
        except Exception as e:
            self.logger.error("%s", str(e))
        finally:
            cursor.close()
            self.logger.debug("cursur closed")


    def delete(self, sql:str, args:tuple) -> int:
        """ delete records from the database baseon the sql and args 
        provided. it will return the number of effected rows."""

        self.logger.debug("query received: %s", sql)
        self.logger.debug("args received: %s", args)
        
        conn = self.dbconn.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(sql, args)
            result = cursor.rowcount
            self.logger.debug("data returned: %s", result)
            return result
        except Exception as e:
            self.logger.error("%s", str(e))
            conn.rollback()
        finally:
            cursor.close()
            self.logger.debug("cursur closed")
