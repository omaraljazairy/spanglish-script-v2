# from configs.db import db_conn
from typing import TypeVar
from datetime import datetime

Word = TypeVar('Word')
"""
responsible for the word data model object and the interaction with the 
word table in the database.
"""



class WordModel:

    def __init__(self, id: int, word: str, category_id: int) -> None:
        """
        set three attributes, id, word and category_id to should be initialized.
        the conn attribute and the created will be automatically initialized and available for
        all functions. 
        """
        
        self.id = id
        self.word = word
        self.category_id = category_id
        self.created = datetime.now()
        # self.dbconn = db_conn()


    def set_word(word:str, category_id:str) -> int:
        """ 
        takes the word name and the category_id as arguments and returns the id 
        generated if successful, otherwise an exception will be raised.
        """

        return 1

    @staticmethod
    def get_word(id: int) -> Word:
        """ takes an int and returns the word object if found, otherwise """

        return Word(id, 'Verb')

