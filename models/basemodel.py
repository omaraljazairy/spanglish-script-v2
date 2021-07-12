from abc import ABC, abstractmethod, abstractstaticmethod
import logging
from typing import List
from services.dbconnection import DBConnection
from dataclasses import dataclass

@dataclass
class BaseModel(ABC):
    """ this is the base model that all models will inherit from. """

    def __init__(self) -> None:
        self.dbconn: DBConnection = DBConnection() # initialize db instance.
        self.logger = logging.getLogger('models')


    @abstractmethod
    def save(self) -> object:
        ''' save an initialized object to the database and return the object created. '''

    @abstractstaticmethod
    def fetch(id: int) -> object:
        ''' static method that returns a model instance or None. '''

    @abstractstaticmethod
    def fetch_all() -> List:
        ''' returns a list of the object model or empty model if not found '''

    # @abstractmethod
    def convert_db_to_object(self, data) -> object:
        ''' convert the records fetched from the database to a class object. '''

