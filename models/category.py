from models.basemodel import BaseModel
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
    

    def __post_init__(self):
        super().__init__()


    def save(self) -> Category:
        """ 
        takes the initialized category model and saves it and returns the Category 
        generated if successful, otherwise an exception will be raised.
        """

        return self

    
    @staticmethod
    def fetch(id: int) -> Dict:
        """ 
        takes an int and returns the Category object if found, 
        otherwise it will return None. 
        """

        data = {
            'category': 'foo',
            'id' : id,
            'created': '2021-06-22 22:56:01'
        }

        return data

    @staticmethod
    def fetch_all() -> List[Dict]:
        """ 
        takes no argument and returns a list of all Category objects 
        if found, otherwise return an empty list. 
        """

        data = [{
            'category': 'foo',
            'id' : 1,
            'created': '2021-06-22 22:56:01'
        },
        {
            'category': 'bar',
            'id' : 2,
            'created': '2021-06-22 22:58:01'
        }]

        return data


    @staticmethod
    def convert_dict_to_object(data: dict) -> Category:
        """ convert the database dict record into a Category object. """

        category = data['category']
        id = data['id']
        created = datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')
        return Category(category=category, id=id, created=created)
