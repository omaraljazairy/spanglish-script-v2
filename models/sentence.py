from models.language import Language
from models.basemodel import BaseModel
from dataclasses import dataclass
from models.category import Category
from models.language import Language
from typing import Dict, TypeVar, List
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
    language: Language = None
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
    def fetch(id: int) -> Dict:
        """ 
        takes an int and returns the sentence dict if found, otherwise None
        will be returned. 
        """

        sentence =  {
                'sentence': 'Hola amigo',
                'id': id,
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

        return sentence


    @staticmethod
    def fetch_all() -> List[Dict]:
        """ 
        takes no arguments and returns a list of Sentence dicts or 
        empty list. 
        """

        sentences = [
            {
                'sentence': 'Hola amigo',
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
                'sentence': 'Buenos dias',
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

        return sentences


    @staticmethod
    def convert_dict_to_object(data: dict) -> Sentence:
        """ convert the database record as dict into a Sentence object. """

        sentence = data['sentence']
        id = data['id']
        created = datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')
        category = data['category']['category']
        language_id = data['language']['id']
        language_name = data['language']['name']
        language_code = data['language']['code']
        language_created = datetime.strptime(data['language']['created'], '%Y-%m-%d %H:%M:%S')
        category_id = data['category']['id']
        category_created = datetime.strptime(data['category']['created'], '%Y-%m-%d %H:%M:%S')

        return Sentence(
            sentence=sentence, id=id, created=created, 
            category=Category(category=category, id=category_id, created=category_created),
            language=Language(name=language_name, code=language_code, id=language_id, created=language_created)
            )

