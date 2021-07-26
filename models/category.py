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


    @staticmethod
    def save(category:str) -> bool:
        """ 
        take the category name and saves it and returns True 
        if successfully added, otherwise False.
        """

        query = """
        INSERT IGNORE INTO {} (`name`) VALUES (%s)
        """.format(Category.tables.CATEGORY)
        args = (category,)
        result = Category.dbmodel.insert(sql=query, args=args)
       
        return result


    
    @staticmethod
    def get_category_by_id(id: int) -> Dict:
        """ 
        takes an int and returns the Category dict if found, 
        otherwise it will return None. 
        """

        query = """ 
        SELECT * FROM {} WHERE id = %s;
        """.format(Category.tables.CATEGORY)

        args = (id,)
        data = Category.dbmodel.fetch(sql=query, args=args)

        return data

    @staticmethod
    def get_all_categories() -> List[Dict]:
        """ 
        takes no argument and returns a list of all Category dicts 
        if found, otherwise return an empty list. 
        """

        query = """ 
        SELECT * FROM {} WHERE 1;
        """.format(Category.tables.CATEGORY)

        args = ()
        data = Category.dbmodel.fetch_all(sql=query, args=args)

        return data


    @staticmethod
    def convert_dict_to_object(data: dict) -> Category:
        """ convert the database dict record into a Category object. """

        category = data['category']
        id = data['id']
        created = datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')
        return Category(category=category, id=id, created=created)
