from models.basemodel import BaseModel
from models.dbmodel import DBModel
from dataclasses import dataclass
from typing import TypeVar, List
from datetime import datetime
from warnings import filterwarnings
filterwarnings("ignore")

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
    

    def __post_init__(self):
        """ initialize the basemode class. """
        super().__init__()

    @staticmethod
    def save(name:str, code:str) -> bool:
        """ 
        takes the initialized language model and saves it and returns True if 
        the Language is inserted successfully, otherwise False.
        """

        query = """
        Insert IGNORE into {} (`name`, `iso-639-1`) VALUES (%s, %s)
        """.format(Language.tables.LANGUAGE)
        args = (name, code)
        result = Language.dbmodel.insert(sql=query, args=args)
       
        return result

    
    @staticmethod
    def get_language_by_id(id: int) -> Language:
        """ 
        takes an int and returns the Language dict if found, 
        otherwise it will return None. 
        """
        
        query = """
        Select * from {} where id = %s
        """.format(Language.tables.LANGUAGE)
        args = (id,)

        language = Language.dbmodel.fetch(sql=query, args=args)
        
        return language


    @staticmethod
    def get_all() -> List[Language]:
        """ 
        takes no argument and returns a list of all Language objects 
        if found, otherwise return an empty list. 
        """

        query = """
        Select * from {}
        """.format(Language.tables.LANGUAGE)
        args = ()

        language = Language.dbmodel.fetch_all(sql=query, args=args)
        
        return language

    
    @staticmethod
    def delete_language_by_id(id: int) -> int:
        """ 
        takes an id and returns an int of the effected rows. 
        """

        query = """
        Delete from {} where id = %s LIMIT 1;
        """.format(Language.tables.LANGUAGE)
        args = (id,)

        effected_rows = Language.dbmodel.delete(sql=query, args=args)
        
        return effected_rows

    @staticmethod
    def update_language_by_id(id:int, code:str = None, name:str = None) -> bool:
        """ take the language id with the code and/or the name params. 
        return True if an update took place, otherwise False. If non of the 
        code or name are provided, the function will return with False. """

        # create the set code and name query clause
        code_query = " `iso-639-1` = %s" if code else ""
        name_query = " `name` = %s" if name else ""

        set_query_clause = "" # create an empty string to start with. 
        list_args = []
        if code and name:
            # if code and name both provided, append them to the set_query string 
            set_query_clause = set_query_clause + code_query + "," + name_query
            list_args.append(code)
            list_args.append(name)
        elif code:
            # if only the code is provided. 
            set_query_clause = set_query_clause + code_query
            list_args.append(code)
        elif name:
            # if only the name is provided
            set_query_clause = set_query_clause + name_query
            list_args.append(name)
        else:
            return False

        query = """
        UPDATE {} SET {} WHERE id = %s;
        """.format(Language.tables.LANGUAGE, set_query_clause)
        list_args.append(id) # add the id to the end of the list.
        args = tuple(list_args)

        effected_rows = Language.dbmodel.update(sql=query, args=args)
        
        return bool(effected_rows)


    @staticmethod
    def convert_dict_to_object(data: dict) -> List:
        """ convert the database record as dict into a Language object. """

        name = data['name']
        id = data['id']
        code = data['code']
        created = datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')

        language = Language(name=name, code=code, id=id, created=created)

        return language
    