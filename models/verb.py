# from configs.db import db_conn
from typing import TypeVar
from datetime import datetime
from .word import WordModel

VerbModel = TypeVar('VerbModel')
"""
responsible for the verb data model object and the interaction with the 
verb table in the database.
"""



class VerbModel(WordModel):

    def __init__(
        self, 
        word: WordModel, 
        yo: str = None, 
        tu: str = None,
        usted: str = None,
        nosotros: str = None,
        vosotros: str = None,
        ustedes: str = None,
        id: int = None,
        tense: str = 'present'
        ) -> None:
        """
        set eight attributes, word, yo, tu, useted, nosotros, vosotros, usetedes should be initialized.
        the conn attribute will be automatically initialized and available for
        all functions. 
        """
        
        self.id = id
        self.word = word
        self.yo = yo
        self.tu = tu
        self.usted = usted
        self.nosotros = nosotros
        self.vosotros = vosotros
        self.ustedes = ustedes
        self.tense = tense
        # self.dbconn = db_conn()


    def set_verb(self) -> int:
        """ 
        takes the verbmodel object as arguments and returns the id after inserting it
        if successful, otherwise an exception will be raised.
        """

        return 1

    @staticmethod
    def get_verb(verb_id: int = None, word_id = None) -> VerbModel:
        """ takes the verb id or word id as int and returns the VerbModel object if found, otherwise """

        return True

