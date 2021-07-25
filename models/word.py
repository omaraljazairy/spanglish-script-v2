from models.basemodel import BaseModel
from models.category import Category
from models.language import Language
from dataclasses import dataclass
from typing import Dict, TypeVar, List
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
    language: Language = None
    id: int = None
    created: datetime = datetime.now()


    def __post_init__(self):
        """This is only for dataclasses. It will be executed after the 
        automatic default init """
        super().__init__()


    def save(self) -> int:
        """ 
        takes the word object returns the generated word id if successful, 
        otherwise None will be returned.
        """

        return self


    @staticmethod
    def fetch(id: int) -> Dict:
        """ 
        takes an int of the wordId and returns the word object if found, otherwise None
        will be returned. 
        """

        word = {
            'word': 'Hola',
            'id': 1,
            'created': '2021-06-22 22:56:01',
            'category': {
                'category': 'foo',
                'id' : 1,
                'created': '2021-06-22 22:56:01'
            },
            'language': {
                'name': 'Spanish',
                'id' : 2,
                'code': 'ES',
                'created': '2021-06-22 22:58:01'
            }
        }

        return word


    @staticmethod
    def fetch_all() -> List[Dict]:
        """ 
        takes no arguments and returns a list of Word dict objects or 
        empty list. 
        """

        words =  [
            {
                'word': 'Hola',
                'id': 1,
                'created': '2021-06-22 22:56:01',
                'category': {
                    'category': 'foo',
                    'id' : 1,
                    'created': '2021-06-22 22:56:01'
                },
                'language': {
                    'name': 'Spanish',
                    'id' : 2,
                    'code': 'ES',
                    'created': '2021-06-22 22:58:01'
                }
            },
            {
                'word': 'dia',
                'id': 2,
                'created': '2021-06-22 22:57:01',
                'category': {
                    'category': 'bar',
                    'id' : 2,
                    'created': '2021-06-22 22:58:01'
                },
                'language': {
                    'name': 'English',
                    'id' : 1,
                    'code': 'EN',
                    'created': '2021-06-22 22:56:01'
                }
            }]


        return words


    @staticmethod
    def convert_dict_to_object(data: dict) -> Word:
        """ convert the database record as dict into a Word object. """

        word = data['word']
        id = data['id']
        created = datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')
        category = data['category']['category']
        language_id = data['language']['id']
        language_name = data['language']['name']
        language_code = data['language']['code']
        language_created = datetime.strptime(data['language']['created'], '%Y-%m-%d %H:%M:%S')
        category_id = data['category']['id']
        category_created = datetime.strptime(data['category']['created'], '%Y-%m-%d %H:%M:%S')

        return Word(
            word=word, id=id, created=created, 
            category=Category(category=category, id=category_id, created=category_created),
            language=Language(name=language_name, code=language_code, id=language_id, created=language_created)
            )