import logging
from enums.dbenums import VerbTense
from exceptions.modelsexceptions import MissingArgs
from models.basemodel import BaseModel
from models.dbmodel import DBModel
from dataclasses import dataclass
from typing import Dict, TypeVar, List
from datetime import datetime
from models.word import Word
from models.category import Category
from models.language import Language

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
    tense: str = VerbTense.PRESENT_PERFECT
    created: datetime = datetime.now()
    dbmodel = DBModel()
    logger = logging.getLogger('models')


    def __post_init__(self):
        """This is only for dataclasses. It will be executed after the 
        automatic default init """
        super().__init__()


    @classmethod
    def save(
        cls, 
        word_id:int, 
        yo:str=None, 
        tu:str=None, 
        usted:str=None, 
        nosotros:str=None, 
        vosotros:str=None, 
        ustedes:str=None, 
        tense:str=VerbTense.PRESENT_PERFECT.value) -> int:
        """ 
        takes the verb object returns the generated verb if successful, 
        otherwise None will be returned.
        """

        query = """
        INSERT INTO {} 
        (
            `word_id`, `yo`, `tu`, `usted`, `nosotros`, `vosotros`, `ustedes`, `tense`
        ) 
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s
        )
        """.format(cls.tables.VERB)
        
        args = (word_id, yo, tu, usted, nosotros, vosotros, ustedes, tense)
        result = cls.dbmodel.insert(sql=query, args=args)
        
        cls.logger.debug("verb saved: %s", result)
       
        return result



    @classmethod
    def get_verb_by_id(cls, verb_id: int = None, word_id:int = None) -> Dict:
        """ 
        takes an int of the verbId or the wordId and fetchs the verb by calling the 
        method with a query and one argument, verb_id or word_id. 
        It will returns the verb object as a dict type if found, otherwise None
        will be returned. 
        If no verb_id or word_id were provided, a MissingArgs exception will be raised.
        """

        if not verb_id and not word_id:
            raise MissingArgs(required_args=('verb_id', 'word_id'))

        where_clause = 'v.id = %s' if verb_id else 'v.word_id = %s'
        args = (verb_id,) if verb_id else (word_id,)

        query = """
        SELECT * FROM {} as v 
        JOIN {} as w on (v.word_id = w.id) 
        JOIN {} as c on (w.category_id = c.id) 
        JOIN {} as l on (w.language_id = l.id) 
        WHERE  """.format(
            cls.tables.VERB, 
            cls.tables.WORD, 
            cls.tables.CATEGORY, 
            cls.tables.LANGUAGE
        )
        
        query += where_clause

        verb = cls.dbmodel.fetch(sql=query, args=args)
        cls.logger.debug("verb returend: %s", verb)

        return verb

    
    @classmethod
    def get_all_verbs_by_word_or_all(cls, word:str=None) -> List[dict]:
        """ take a word that will have the Like in it's where clause. So the 
        word can be '%foo', '%foo%' or 'foo%'. The where clause will search 
        using LIKE in the where clause. If the word is not provided, all 
        verbs will be returned. The returned object will be a list of 
        dictionaries. """

        where_clause = 'w.word like %s' if word else '%s'
        args = (word,) if word else (1,)

        query = """
        SELECT * FROM {} as v 
        JOIN {} as w on (v.word_id = w.id) 
        JOIN {} as c on (w.category_id = c.id) 
        JOIN {} as l on (w.language_id = l.id) 
        WHERE  """.format(
            cls.tables.VERB, 
            cls.tables.WORD, 
            cls.tables.CATEGORY, 
            cls.tables.LANGUAGE
        )
        
        query += where_clause

        verb = cls.dbmodel.fetch_all(sql=query, args=args)
        cls.logger.debug("verbs returend: %s", verb)

        return verb


    @classmethod
    def update_verb_by_word_id(cls, word_id:int, **kwargs) -> int:
        """ update a verb by providing the word_id. the updated values 
        can be yo,tu,usted,nosotros,vosotros,ustedes,tense. If non is provided, 
        the update will not be executed. 
        """


        list_args = []
        set_query_clause = "" # create an empty string to start with. 

        possible_keys = {
            'yo': " `yo` = %s",
            'tu': " `tu` = %s",
            'usted': " `usted` = %s",
            'nosotros': "`nosotros` = %s",
            'vosotros': "`vosotros` = %s",
            'ustedes': "`ustedes` = %s",
            'tense': "`tense` = %s"
        }

        # loop through the expected keys in the kwargs. 
        # if the keys is found and has a value, use it's value to create
        # the set_query_clause by append the value to it.         
        for key in possible_keys:
            if key in kwargs.keys() and kwargs[key]:
                list_args.append(kwargs[key])
                set_query_clause = set_query_clause + possible_keys[key] if len(list_args) == 1 else set_query_clause + "," + possible_keys[key]

        # throw an exception if there no args. 
        if not list_args:
            raise MissingArgs(required_args=tuple(possible_keys.keys()))


        list_args.append(word_id) # add the id into the args list

        query = """
        UPDATE {} 
        SET {}
        WHERE word_id = %s;
        """.format(cls.tables.VERB, set_query_clause)

        args = tuple(list_args) # convert the list to a tuple
        cls.logger.debug("query: %s", query)
        cls.logger.debug("args: %s", args)

        result = cls.dbmodel.update(sql=query, args=args)
        
        return result


    @staticmethod
    def convert_dict_to_object(data: dict) -> Word:
        """ convert a dictionary into a Verb object. """

        id = data.get('id', None)
        yo = data.get('yo', None)
        tu = data.get('tu', None)
        usted = data.get('usted', None)
        nosotros = data.get('nosotros', None)
        vosotros = data.get('vosotros', None)
        ustedes = data.get('ustedes', None)
        tense = data.get('tense', 'present')
        created = datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')

        word = data['word']['word']
        word_id = data['word']['id']
        word_created = datetime.strptime(data['word']['created'], '%Y-%m-%d %H:%M:%S')
        word_category = data['word']['category']['category']
        word_language_id = data['word']['language']['id']
        word_language_name = data['word']['language']['name']
        word_language_code = data['word']['language']['code']
        word_language_created = datetime.strptime(data['word']['language']['created'], '%Y-%m-%d %H:%M:%S')
        word_category_id = data['word']['category']['id']
        word_category_created = datetime.strptime(data['word']['category']['created'], '%Y-%m-%d %H:%M:%S')

        word_obj = Word(
            word=word, 
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
                created=word_language_created)
            )
        
        return Verb(
            word=word_obj,
            yo=yo,
            tu=tu,
            usted=usted,
            nosotros=nosotros,
            vosotros=vosotros,
            ustedes=ustedes,
            id=id,
            tense=tense,
            created=created
        )