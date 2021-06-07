# from configs.db import db_conn
from models.modelinterface import ModelInterface
from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar, List

Category = TypeVar('Category')
"""
This dataclass is responsible for the Category data model object and the
interaction with the Category table in the database.
"""
@dataclass
class Category(ModelInterface):
    """
    has three attributes, category, id and created. category is the only required
    attribute to be set when initializing the object.
    """

    category: str
    id: int = None
    created: datetime = datetime.now() # default value is now

    # def __init__(self, category: str, id: int = None, created: datetime = None, ) -> None:
    #     """
    #     has three attributes, category, id and created. category is the only required
    #     attribute to be set when initializing the object.
    #     """
        
    #     self.id = id
    #     self.category = category
    #     self.created = created


    def save(self) -> Category:
        """ 
        takes the initialized category model and saves it and returns the Category 
        generated if successful, otherwise an exception will be raised.
        """

        return self

    
    @staticmethod
    def fetch(id: int) -> Category:
        """ 
        takes an int and returns the Category object if found, 
        otherwise it will return None. 
        """

        return Category(id, 'Verb', datetime.now())

    @staticmethod
    def fetch_all() -> List[Category]:
        """ 
        takes no argument and returns a list of all Category objects 
        if found, otherwise return an empty list. 
        """

        return [Category(id, 'Verb', datetime.now())]

