from models.basemodel import BaseModel
from models.category import Category
from dataclasses import dataclass
from typing import TypeVar, List
from datetime import datetime

Word = TypeVar('Word')
"""
responsible for the word data model object and the interaction with the 
word table in the database.
"""
@dataclass
class Word(BaseModel):

    word: str
    category: Category
    id: int = None
    created: datetime = datetime.now()


    def __post_init__(self):
        """This is only for dataclasses. It will be executed after the 
        automatic default init """
        super().__init__()


    def save(self) -> Word:
        """ 
        takes the word object returns the generated word if successful, 
        otherwise None will be returned.
        """

        return self


    @staticmethod
    def fetch(id: int) -> Word:
        """ 
        takes an int of the wordId and returns the word object if found, otherwise None
        will be returned. 
        """

        return Word(id=id, word='Hola', category=Category(category='greeting', id=1, created=datetime.now()), created=datetime.now())


    @staticmethod
    def fetch_all() -> List[Word]:
        """ 
        takes no arguments and returns a list of Word objects or 
        empty list. 
        """

        return [Word(id=id, word='Hola', category=Category(category='greeting', id=1, created=datetime.now()), created=datetime.now()),]

