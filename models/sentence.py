# from configs.db import db_conn
from typing import TypeVar
from datetime import datetime

Sentence = TypeVar('Sentence')
"""
responsible for the sentence data model object and the interaction with the 
sentence table in the database.
"""



class SentenceModel:

    def __init__(self, id: int, sentence: str, category_id: int) -> None:
        """
        set three attributes, id, sentence and category_id to should be initialized.
        the conn attribute and the created will be automatically initialized and available for
        all functions. 
        """
        
        self.id = id
        self.sentence = sentence
        self.category_id = category_id
        self.created = datetime.now()
        # self.dbconn = db_conn()


    def set_sentence(sentence:str, category_id:str) -> int:
        """ 
        takes the sentence name and the category_id as arguments and returns the id 
        generated if successful, otherwise an exception will be raised.
        """

        return 1

    @staticmethod
    def get_sentence(id: int) -> Sentence:
        """ takes an int and returns the sentence object if found, otherwise """

        return Sentence(id, 'Verb')

