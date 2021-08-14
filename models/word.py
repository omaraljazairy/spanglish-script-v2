import logging
from models.basemodel import BaseModel
from models.dbmodel import DBModel
from models.category import Category
from models.language import Language
from exceptions.modelsexceptions import MissingArgs
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
    language: Language
    id: int = None
    created: datetime = datetime.now()
    dbmodel = DBModel()
    logger = logging.getLogger('models')


    def __post_init__(self):
        """This is only for dataclasses. It will be executed after the 
        automatic default init """
        super().__init__()


    @classmethod
    def save(cls, word:str, language_id:int, category_id:int) -> int:
        """ 
        takes a word, language_id and category_id and inserts them, returns 
        back the word_id.
        """

        query = """
        Insert IGNORE into {} (`word`, `language_id`, `category_id`) VALUES (%s, %s, %s)
        """.format(cls.tables.WORD)
        args = (word, language_id, category_id)
        result = cls.dbmodel.insert(sql=query, args=args)
        
        cls.logger.debug("word saved: %s", result)
       
        return result


    @classmethod
    def get_word_by_id(cls, id:int) -> Dict:
        """ 
        takes an int of the language_id and/or category_id returns the word dict if found, otherwise None
        will be returned. 
        """

        query = """
        SELECT w.id as id, word, w.created as created, 
        language_id, l.name as language_name, `iso-639-1`, l.created as language_created, 
        category_id, c.name as category_name, c.created as category_created 
        FROM {} AS w 
        JOIN {} AS c ON (w.category_id = c.id) 
        JOIN {} AS l ON (w.language_id = l.id) 
        WHERE w.id = %s;
        """.format(cls.tables.WORD, cls.tables.CATEGORY, cls.tables.LANGUAGE)

        args = (id,)

        word = cls.dbmodel.fetch(sql=query, args=args)
        
        return word


    @classmethod
    def get_words_by_category_language(cls, language_id:int=None, category_id:int = None) -> List[Dict]:
        """ 
        takes an int of the language_id and/or category_id returns a list of word dicts if found, otherwise None
        will be returned. 
        """

        query = """
        SELECT w.id as id, word, w.created as created, 
        language_id, l.name as language_name, `iso-639-1`, l.created as language_created, 
        category_id, c.name as category_name, c.created as category_created 
        FROM {} AS w 
        JOIN {} AS c ON (w.category_id = c.id) 
        JOIN {} AS l ON (w.language_id = l.id) 
        WHERE
        """.format(cls.tables.WORD, cls.tables.CATEGORY, cls.tables.LANGUAGE)
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

        word = cls.dbmodel.fetch_all(sql=query, args=args)
        
        return word
        

    @classmethod
    def update_word_by_id(cls, id:int, **kwargs) -> int:
        """ update a word by providing its id. the updated values can be the
        language_id and/or category_id. If non is provided, the update will 
        not be executed. """


        list_args = []
        set_query_clause = "" # create an empty string to start with. 

        expected_keys = {
            'word': " `word` = %s",
            'language_id': " `language_id` = %s",
            'category_id': " `category_id` = %s"
        }

        # loop through the expected keys in the kwargs. 
        # if the keys is found and has a value, use it's value to create
        # the set_query_clause by append the value to it.         
        for key in expected_keys:
            if key in kwargs.keys() and kwargs[key]:
                list_args.append(kwargs[key])
                set_query_clause = set_query_clause + expected_keys[key] if len(list_args) == 1 else set_query_clause + "," + expected_keys[key]

        # throw an exception if there no args. 
        if not list_args:
            raise MissingArgs(required_args=tuple(expected_keys.keys()))


        list_args.append(id) # add the id into the args list

        query = """
        UPDATE {} 
        SET {}
        WHERE id = %s;
        """.format(cls.tables.WORD, set_query_clause)

        args = tuple(list_args) # convert the list to a tuple
        cls.logger.debug("query: %s", query)
        cls.logger.debug("args: %s", args)

        word = cls.dbmodel.update(sql=query, args=args)
        
        return word


    @classmethod
    def convert_dict_to_object(cls, data: dict) -> Word:
        """ convert the database record as dict into a Word object. """

        word = data['word']
        id = data['id']
        created = datetime.strftime(data['created'], '%Y-%m-%d %H:%M:%S')

        category = data['category_name']
        category_id = data['category_id']
        category_created = datetime.strftime(data['category_created'], '%Y-%m-%d %H:%M:%S')

        language_id = data['language_id']
        language_name = data['language_name']
        language_code = data['iso-639-1']
        language_created = datetime.strftime(data['language_created'], '%Y-%m-%d %H:%M:%S')

        return cls(
            word=word, id=id, created=created, 
            category=Category(category=category, id=category_id, created=category_created),
            language=Language(name=language_name, code=language_code, id=language_id, created=language_created)
            )