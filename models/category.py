# from configs.db import db_conn
from typing import TypeVar

Category = TypeVar('Category')
"""
responsible for the Category data model object and the interaction with the 
Category table in the database.
"""



class CategoryModel:

    def __init__(self, id: int, category: str) -> None:
        """
        set two attributes, id and category, both should be initialized.
        the conn attribute will be automatically initialized and available for
        all functions. 
        """
        
        self.id = id
        self.category = category
        # self.dbconn = db_conn()


    def set_category(category:str) -> int:
        """ 
        takes the category name string as an argument and returns the id 
        generated if successful, otherwise an exception will be raised.
        """

        return 1

    @staticmethod
    def get_category(id: int) -> Category:
        """ takes an int and returns the Category object if found, otherwise """

        return Category(id, 'Verb')

