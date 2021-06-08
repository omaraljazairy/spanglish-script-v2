# from configs.db import db_conn
from models.modelinterface import ModelInterface
from dataclasses import dataclass
from typing import TypeVar, List
from datetime import datetime

Language = TypeVar('Language')
"""
This dataclass is responsible for the Language data model object and the
interaction with the Language table in the database.
"""
@dataclass
class Language(ModelInterface):
    """
    has two attributes, language and id. language is the only required
    attribute to be set when initializing the object.
    """

    name: str
    code: str
    id: int = None
    created: datetime = datetime.now()


    def save(self) -> Language:
        """ 
        takes the initialized language model and saves it and returns the Language 
        generated if successful, otherwise an exception will be raised.
        """

        return self

    
    @staticmethod
    def fetch(id: int) -> Language:
        """ 
        takes an int and returns the Language object if found, 
        otherwise it will return None. 
        """

        return Language(id=id, name='English', code='en', created=datetime.now())

    @staticmethod
    def fetch_all() -> List[Language]:
        """ 
        takes no argument and returns a list of all Language objects 
        if found, otherwise return an empty list. 
        """

        return [Language(id=id, name='English', code='en', created=datetime.now()),]

