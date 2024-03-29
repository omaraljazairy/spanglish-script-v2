from models.basemodel import BaseModel
from models.dbmodel import DBModel
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, TypeVar, List, Optional


Category = TypeVar('Category')
"""
This dataclass is responsible for the Category data model object and the
interaction with the Category table in the database.
"""
@dataclass(init=True)
class Category(BaseModel):
    """
    has three attributes, category, id and created. category is the only required
    attribute to be set when initializing the object.
    """

    category: str
    id: Optional[int] = None
    created: datetime = datetime.now() # default value is now
    dbmodel = DBModel()

    def __post_init__(self):
        super().__init__()


    @classmethod
    def save(cls, category:str) -> bool:
        """ 
        take the category name and saves it and returns True 
        if successfully added, otherwise False.
        """

        query = """
        INSERT IGNORE INTO {} (`name`) VALUES (%s)
        """.format(cls.tables.CATEGORY)
        args = (category,)
        result = cls.dbmodel.insert(sql=query, args=args)
       
        return result


    
    @classmethod
    def get_category_by_id(cls, id: int) -> Dict:
        """ 
        takes an int and returns the Category dict if found, 
        otherwise it will return None. 
        """

        query = """ 
        SELECT * FROM {} WHERE id = %s;
        """.format(cls.tables.CATEGORY)

        args = (id,)
        data = cls.dbmodel.fetch(sql=query, args=args)

        return data


    @classmethod
    def get_all_categories(cls) -> List[Dict]:
        """ 
        takes no argument and returns a list of all Category dicts 
        if found, otherwise return an empty list. 
        """

        query = """ 
        SELECT * FROM {} WHERE 1;
        """.format(cls.tables.CATEGORY)

        args = ()
        data = cls.dbmodel.fetch_all(sql=query, args=args)

        return data


    @classmethod
    def convert_dict_to_object(cls, data: dict) -> Category:
        """ convert the database dict record into a Category object. """

        category = data['name']
        id = data['id']
        created = datetime.strftime(data['created'], '%Y-%m-%d %H:%M:%S')
        
        return cls(category=category, id=id, created=created)
