from models.basemodel import BaseModel
from dataclasses import dataclass
from models.category import Category
from typing import TypeVar, List
from datetime import datetime
from models.word import Word

Verb = TypeVar('Verb')
"""
responsible for the verb data model object and the interaction with the 
verb table in the database.
"""


@dataclass
class Verb(BaseModel):

    word: Word
    yo: str = None
    tu: str = None
    usted: str = None
    nosotros: str = None
    vosotros: str = None
    ustedes: str = None
    id: int = None
    tense: str = 'present'
    created: datetime = datetime.now()


    def __post_init__(self):
        """This is only for dataclasses. It will be executed after the 
        automatic default init """
        super().__init__()


    def save(self) -> Verb:
        """ 
        takes the verb object returns the generated verb if successful, 
        otherwise None will be returned.
        """

        return self


    @staticmethod
    def fetch(id: int) -> Verb:
        """ 
        takes an int of the verbId and returns the verb object if found, otherwise None
        will be returned. 
        """

        return Verb(id=id, word=Word(id=2, word='ir', category=Category(category='verb', id=2, created=datetime.now()), created=datetime.now()), yo='voy', tu='vas', usted='va', nosotros='vamos', vosotros='vais', ustedes='van', tense='persent', created=datetime.now())


    @staticmethod
    def fetch_all() -> List[Verb]:
        """ 
        takes no arguments and returns a list of Verb objects or 
        empty list. 
        """

        return [Verb(id=id, word=Word(id=2, word='ir', category=Category(category='verb', id=2, created=datetime.now()), created=datetime.now()), yo='voy', tu='vas', usted='va', nosotros='vamos', vosotros='vais', ustedes='van', tense='persent', created=datetime.now()),]

