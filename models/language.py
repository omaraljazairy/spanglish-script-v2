import logging
from models.basemodel import BaseModel
from models.dbmodel import DBModel
from exceptions.modelsexceptions import MissingArgs
from dataclasses import dataclass
from typing import TypeVar, List
from datetime import datetime

Language = TypeVar('Language')
"""
This dataclass is responsible for the Language data model object and the
interaction with the Language table in the database.
"""
@dataclass
class Language(BaseModel):
    """
    has four attributes, language name, id, code, and created. language name 
    and code are the only required attribute to be set when initializing the 
    object.
    """

    name: str
    code: str
    id: int
    created: datetime = datetime.now()
    dbmodel = DBModel()
    logger = logging.getLogger('models')
    

    def __post_init__(self):
        """ initialize the basemode class. """
        super().__init__()


    @classmethod
    def save(cls, name:str, code:str) -> bool:
        """ 
        takes the initialized language model and saves it and returns True if 
        the Language is inserted successfully, otherwise False.
        """

        query = """
        Insert IGNORE into {} (`name`, `iso-639-1`) VALUES (%s, %s)
        """.format(cls.tables.LANGUAGE)
        args = (name, code)
        result = cls.dbmodel.insert(sql=query, args=args)
       
        return result

    
    @classmethod
    def get_language_by_id(cls, id: int) -> Language:
        """ 
        takes an int and returns the Language dict if found, 
        otherwise it will return None. 
        """
        
        query = """
        Select * from {} where id = %s
        """.format(cls.tables.LANGUAGE)
        args = (id,)

        language = cls.dbmodel.fetch(sql=query, args=args)
        
        return language


    @classmethod
    def get_all(cls) -> List[Language]:
        """ 
        takes no argument and returns a list of all Language objects 
        if found, otherwise return an empty list. 
        """

        query = """
        Select * from {}
        """.format(cls.tables.LANGUAGE)
        args = ()

        language = cls.dbmodel.fetch_all(sql=query, args=args)
        
        return language

    
    @classmethod
    def delete_language_by_id(cls, id: int) -> int:
        """ 
        takes an id and returns an int of the effected rows. 
        """

        query = """
        Delete from {} where id = %s LIMIT 1;
        """.format(cls.tables.LANGUAGE)
        args = (id,)

        effected_rows = cls.dbmodel.delete(sql=query, args=args)
        
        return effected_rows

    @classmethod
    def update_language_by_id(cls, id:int, **kwargs) -> bool:
        """ take the language id with the code and/or the name params. 
        return True if an update took place, otherwise False. If non of the 
        code or name are provided, the function will return with False. """

        list_args = []
        set_query_clause = "" # create an empty string to start with. 

        expected_keys = {
            'code': " `iso-639-1` = %s",
            'name': " `name` = %s"
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
        """.format(cls.tables.LANGUAGE, set_query_clause)

        args = tuple(list_args) # convert the list to a tuple
        cls.logger.debug("query: %s", query)
        cls.logger.debug("args: %s", args)

        language = cls.dbmodel.update(sql=query, args=args)
        
        return language

        # # create the set code and name query clause
        # code_query = " `iso-639-1` = %s" if code else ""
        # name_query = " `name` = %s" if name else ""

        # set_query_clause = "" # create an empty string to start with. 
        # list_args = []
        # if code and name:
        #     # if code and name both provided, append them to the set_query string 
        #     set_query_clause = set_query_clause + code_query + "," + name_query
        #     list_args.append(code)
        #     list_args.append(name)
        # elif code:
        #     # if only the code is provided. 
        #     set_query_clause = set_query_clause + code_query
        #     list_args.append(code)
        # elif name:
        #     # if only the name is provided
        #     set_query_clause = set_query_clause + name_query
        #     list_args.append(name)
        # else:
        #     return False

        # query = """
        # UPDATE {} SET {} WHERE id = %s;
        # """.format(cls.tables.LANGUAGE, set_query_clause)
        # list_args.append(id) # add the id to the end of the list.
        # args = tuple(list_args)

        # effected_rows = cls.dbmodel.update(sql=query, args=args)
        
        # return bool(effected_rows)


    @classmethod
    def convert_dict_to_object(cls, data: dict) -> List:
        """ convert the database record as dict into a Language object. """

        name = data['name']
        id = data['id']
        code = data['iso-639-1']
        created = datetime.strftime(data['created'], '%Y-%m-%d %H:%M:%S')

        language = cls(name=name, code=code, id=id, created=created)

        return language
    