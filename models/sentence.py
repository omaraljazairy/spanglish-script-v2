import logging
from exceptions.modelsexceptions import MissingArgs
from models.dbmodel import DBModel
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
    language: Language = Language(
        name='Spanish', 
        code='ES', 
        id=1, 
        created=datetime.now()
    )
    id: int = None
    created: datetime = datetime.now() # default value is now
    logger = logging.getLogger('models')
    dbmodel = DBModel()


    def __post_init__(self):
        super().__init__()


    @classmethod
    def save(cls, sentence:str, category_id:int, language_id:int) -> int:
        """ 
        takes the sentence string, category_id and languag_id returns the 1 if successful, 
        otherwise 0 will be returned.
        """

        query = """
        Insert IGNORE INTO {} (`sentence`, `language_id`, `category_id`) VALUES (%s, %s, %s)
        """.format(cls.tables.SENTENCE)
        args = (sentence, language_id, category_id)
        result = cls.dbmodel.insert(sql=query, args=args)
        
        cls.logger.info("sentence %s saved: %s", sentence, result)
       
        return result


    @classmethod
    def get_sentence_by_id(cls, id: int) -> Dict:
        """ 
        takes an int and returns the sentence dict if found, otherwise None
        will be returned. 
        """

        query = """
        SELECT s.id as id, sentence, s.created as created, 
        language_id, l.name as language_name, `iso-639-1`, l.created as language_created, 
        category_id, c.name as category_name, c.created as category_created 
        FROM {} AS s 
        JOIN {} AS c ON (s.category_id = c.id) 
        JOIN {} AS l ON (s.language_id = l.id) 
        WHERE s.id = %s;
        """.format(cls.tables.SENTENCE, cls.tables.CATEGORY, cls.tables.LANGUAGE)

        args = (id,)

        cls.logger.debug("query: %s", query)

        sentence = cls.dbmodel.fetch(sql=query, args=args)
        
        return sentence


    @classmethod
    def get_sentence_by_category_language(cls, language_id:int = None, category_id:int = None) -> List[Dict]:
        """ 
        takes no arguments and returns a list of Sentence dicts or 
        empty list. 
        """

        query = """
        SELECT s.id as id, sentence, s.created as created, s.language_id,
        l.name as language_name, `iso-639-1`, l.created as language_created,
        s.category_id, c.name as category_name, c.created as category_created
        FROM {} AS s
        JOIN {} AS c ON (s.category_id = c.id)
        JOIN {} AS l ON (s.language_id = l.id)
        WHERE """.format(cls.tables.SENTENCE, cls.tables.CATEGORY, cls.tables.LANGUAGE)

        where_clause = ""
        args = []

        cls.logger.debug("query at the begining: %s", query)
        # if both language and category are true
        if language_id and category_id:
            where_clause += " s.language_id = %s and s.category_id = %s "
            args = (language_id, category_id)

        # if only the category
        elif category_id:
            where_clause += " s.category_id = %s "
            args = (category_id,)

        # if only the language_id
        elif language_id:
            where_clause += " s.language_id = %s "
            args = (language_id,)

        # set the where to be 1 means return all records
        else:
            where_clause += "1"
            args = ()

        cls.logger.debug("query before where: %s", query)
        query = query + where_clause
        sentence = cls.dbmodel.fetch_all(sql=query, args=args)
        
        cls.logger.debug("query: %s", query)
        cls.logger.debug("args: %s", args)
        cls.logger.debug("sentence: %s", sentence)

        return sentence


    @classmethod
    def update_sentence_by_id(cls, id:int, **kwargs) -> int:
        """ update a sentence by providing its id. the updated values can be the
        language_id and/or category_id. If non is provided, the update will 
        not be executed. """


        list_args = []
        set_query_clause = "" # create an empty string to start with. 

        expected_keys = {
            'sentence': " `sentence` = %s",
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
        """.format(cls.tables.SENTENCE, set_query_clause)

        args = tuple(list_args) # convert the list to a tuple
        cls.logger.debug("query: %s", query)
        cls.logger.debug("args: %s", args)

        sentence = cls.dbmodel.update(sql=query, args=args)
        
        return sentence



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

