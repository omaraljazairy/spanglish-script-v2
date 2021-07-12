from models.basemodel import BaseModel
from models.category import Category
from models.word import Word
from models.sentence import Sentence
from models.language import Language
from dataclasses import dataclass
from typing import TypeVar, List
from datetime import datetime

Translation = TypeVar('Translation')
"""
responsible for the word data model object and the interaction with the 
word table in the database.
"""
@dataclass
class Translation(BaseModel):

    language: Language
    translation: str
    word: Word = None
    sentence: Sentence = None
    id: int = None
    created: datetime = datetime.now()


    def __post_init__(self):
        super().__init__()


    def save(self) -> Translation:
        """ 
        takes the word object returns the generated word if successful, 
        otherwise None will be returned.
        """

        return self


    @staticmethod
    def fetch(id: int) -> Translation:
        """ 
        takes an int of the wordId and returns the word object if found, otherwise None
        will be returned. 
        """

        word = Word(id=1, word='Hola', category=Category(category='greeting', id=1, created=datetime.now()), created=datetime.now())

        language = Language(name='English', code='EN', id=1, created=datetime.now())

        return Translation(id=id, translation='Hello', language=language, word=word, created=datetime.now())


    @staticmethod
    def fetch_all() -> List[Translation]:
        """ 
        takes no arguments and returns a list of Word objects or 
        empty list. 
        """

        word = Word(id=1, word='Hola', category=Category(category='greeting', id=1, created=datetime.now()), created=datetime.now())

        sentence = Sentence(id=1, sentence='Hola amigo', category=Category(category='greeting', id=1, created=datetime.now()), created=datetime.now())

        language = Language(name='English', code='EN', id=1, created=datetime.now())

        return [
            Translation(id=1, translation='Hello', language=language, word=word, created=datetime.now()),
            Translation(id=2, translation='Hello friend', language=language, sentence=sentence, created=datetime.now())    
        ]

