from models.basemodel import BaseModel
from models.category import Category
from models.word import Word
from models.sentence import Sentence
from models.language import Language
from dataclasses import dataclass
from typing import TypeVar, List, Dict
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


    def save(self) -> int:
        """ 
        takes the translation object and returns the generated id if successful, 
        otherwise None will be returned.
        """

        return 1


    @staticmethod
    def fetch(id: int) -> Dict:
        """ 
        takes an int of the translationId and returns the translation dict object if found, otherwise None
        will be returned. 
        """

        translation = {
            'translation': 'Hello',
            'created': '2021-06-22 22:58:01',
            'id': id,
            'word': {
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
            'language': {
                'name': 'English',
                'id' : 1,
                'code': 'EN',
                'created': '2021-06-22 22:58:01'
            }
        }

        return translation


    @staticmethod
    def fetch_all() -> List[Dict]:
        """ 
        takes no arguments and returns a list of translation dict objects or 
        empty list. 
        """

        translations = [
            {
                'translation': 'Hello',
                'created': '2021-06-22 22:58:01',
                'id': 1,
                'word': {
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
                'language': {
                    'name': 'English',
                    'id' : 1,
                    'code': 'EN',
                    'created': '2021-06-22 22:58:01'
                }
            },
            {
                'translation': 'Hello Friend',
                'created': '2021-06-22 22:58:01',
                'id': 2,
                'sentence': {
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
                'language': {
                    'name': 'English',
                    'id' : 1,
                    'code': 'EN',
                    'created': '2021-06-22 22:58:01'
                }
            }
        ]

        return translations



    @staticmethod
    def convert_dict_to_object(data: dict) -> Translation:
        """ convert the dict object into a Translation object. """

        translation = data['translation']
        id = data['id']
        created = datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')
        word = data.get('word', None)
        if word:
            word_word = data['word']['word']
            word_id = data['word']['id']
            word_created = datetime.strptime(data['word']['created'], '%Y-%m-%d %H:%M:%S')
            word_category = data['word']['category']['category']
            word_language_id = data['word']['language']['id']
            word_language_name = data['word']['language']['name']
            word_language_code = data['word']['language']['code']
            word_language_created = datetime.strptime(data['word']['language']['created'], '%Y-%m-%d %H:%M:%S')
            word_category_id = data['word']['category']['id']
            word_category_created = datetime.strptime(data['word']['category']['created'], '%Y-%m-%d %H:%M:%S')
        else:
            sentence_sentence = data['sentence']['sentence']
            sentence_id = data['sentence']['id']
            sentence_created = datetime.strptime(data['sentence']['created'], '%Y-%m-%d %H:%M:%S')
            sentence_category = data['sentence']['category']['category']
            sentence_language_id = data['sentence']['language']['id']
            sentence_language_name = data['sentence']['language']['name']
            sentence_language_code = data['sentence']['language']['code']
            sentence_language_created = datetime.strptime(data['sentence']['language']['created'], '%Y-%m-%d %H:%M:%S')
            sentence_category_id = data['sentence']['category']['id']
            sentence_category_created = datetime.strptime(data['sentence']['category']['created'], '%Y-%m-%d %H:%M:%S')

        language_id = data['language']['id']
        language_name = data['language']['name']
        language_code = data['language']['code']
        language_created = datetime.strptime(data['language']['created'], '%Y-%m-%d %H:%M:%S')

        language_obj = Language(
            name=language_name,
            code=language_code,
            id=language_id,
            created=language_created
        )

        word_obj = None if not word else Word(
            word=word_word,
            id=word_id,
            created=word_created,
            category=Category(
                category=word_category,
                id=word_category_id,
                created=word_category_created
            ),
            language=Language(
                name=word_language_name,
                code=word_language_code,
                id=word_language_id,
                created=word_language_created
            )
        )

        sentence_obj = None if word else Sentence(
            sentence=sentence_sentence,
            id=sentence_id,
            created=sentence_created,
            category=Category(
                category=sentence_category,
                id=sentence_category_id,
                created=sentence_category_created
            ),
            language=Language(
                name=sentence_language_name,
                code=sentence_language_code,
                id=sentence_language_id,
                created=sentence_language_created
            )
        )

        translation = Translation(
            translation=translation,
            language=language_obj,
            word=word_obj,
            sentence=sentence_obj,
            id=id,
            created=created
            )

        return translation

