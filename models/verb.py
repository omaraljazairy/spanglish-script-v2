from dataclasses import dataclass
from typing import TypeVar, List
from datetime import datetime

Verb = TypeVar('Verb')
"""
responsible for the verb data model object and the interaction with the 
verb table in the database.
"""


@dataclass
class Verb:

    word_id: int
    yo: str = None
    tu: str = None
    usted: str = None
    nosotros: str = None
    vosotros: str = None
    ustedes: str = None
    id: int = None
    tense: str = 'present'
    created: datetime = datetime.now()


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

        return Verb(id=id, word_id=2, yo='voy', tu='vas', usted='va', nosotros='vamos', vosotros='vais', ustedes='van', tense='persent', created=datetime.now())


    @staticmethod
    def fetch_all() -> List[Verb]:
        """ 
        takes no arguments and returns a list of Verb objects or 
        empty list. 
        """

        return [Verb(id=id, word_id=2, yo='voy', tu='vas', usted='va', nosotros='vamos', vosotros='vais', ustedes='van', tense='persent', created=datetime.now()),]

