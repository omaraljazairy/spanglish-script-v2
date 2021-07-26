import logging
from models.basemodel import BaseModel
from models.dbmodel import DBModel
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
    dbmodel = DBModel()


    def __post_init__(self):
        """This is only for dataclasses. It will be executed after the 
        automatic default init """
        super().__init__()


    @staticmethod
    def save(word:str, language_id:int, category_id:int) -> int:
        """ 
        takes a word, language_id and category_id and inserts them, returns 
        back the word_id.
        """

        query = """
        Insert IGNORE into {} (`word`, `language_id`, `category_id`) VALUES (%s, %s, %s)
        """.format(Word.tables.WORD)
        args = (word, language_id, category_id)
        result = Word.dbmodel.insert(sql=query, args=args)
       
        return result


    @staticmethod
    def get_word_by_id(id:int) -> Dict:
        """ 
        takes an int of the language_id and/or category_id returns the word dict if found, otherwise None
        will be returned. 
        """

        query = """
        SELECT w.id as id, word, w.created as created, 
        language_id, l.name as language_name, `iso-639-1`, l.created as language_created, 
        category_id, c.name as category_name, c.created as category_created 
        FROM Word AS w 
        JOIN Category AS c ON (w.category_id = c.id) 
        JOIN Language AS l ON (w.language_id = l.id) 
        WHERE w.id = %s;
        """.format(Word.tables.WORD, Word.tables.CATEGORY, Word.tables.LANGUAGE)

        args = (id,)

        word = Language.dbmodel.fetch(sql=query, args=args)
        
        return word


    @staticmethod
    def get_words_by_category_language(language_id:int=None, category_id:int = None) -> List[Dict]:
        """ 
        takes an int of the language_id and/or category_id returns a list of word dicts if found, otherwise None
        will be returned. 
        """

        query = """
        SELECT w.id as id, word, w.created as created, 
        language_id, l.name as language_name, `iso-639-1`, l.created as language_created, 
        category_id, c.name as category_name, c.created as category_created 
        FROM Word AS w 
        JOIN Category AS c ON (w.category_id = c.id) 
        JOIN Language AS l ON (w.language_id = l.id) 
        WHERE
        """.format(Word.tables.WORD, Word.tables.CATEGORY, Word.tables.LANGUAGE)
        where_clause = ""
        args = []
        if language_id and category_id:
            where_clause += " w.language_id = %s and w.category_id = %s "
            args = (language_id, category_id)

        elif category_id:
            where_clause += " w.category_id = %s "
            args = (category_id,)

        elif language_id:
            where_clause += " w.language_id = %s "
            args = (language_id,)

        else:
            return "No language or category provided"

        query = query + where_clause
        # args = tuple(args)

        word = Language.dbmodel.fetch_all(sql=query, args=args)
        
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