from models.basemodel import BaseModel
from dataclasses import dataclass
from models.category import Category
from typing import TypeVar, List
from datetime import datetime

Sentence = TypeVar('Sentence')
"""
responsible for the sentence data model object and the interaction with the 
sentence table in the database.
"""


@dataclass
class Sentence(BaseModel):

    sentence: str
    category: Category
    id: int = None
    created: datetime = datetime.now() # default value is now


    def __post_init__(self):
        super().__init__()


    def save(self) -> Sentence:
        """ 
        takes the sentence object returns the generated sentence if successful, 
        otherwise None will be returned.
        """

        return self


    @staticmethod
    def fetch(id: int) -> Sentence:
        """ 
        takes an int and returns the sentence object if found, otherwise None
        will be returned. 
        """

        return Sentence(id=id, sentence='Hola amigo', category=Category(category='greeting', id=1, created=datetime.now()), created=datetime.now())


    @staticmethod
    def fetch_all() -> List[Sentence]:
        """ 
        takes no arguments and returns a list of Sentence objects or 
        empty list. 
        """

        return [Sentence(id=id, sentence='Hola amigo', category=Category(category='greeting', id=1, created=datetime.now()), created=datetime.now()),]

