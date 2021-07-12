from models.basemodel import BaseModel
from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar, List, Optional


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
    def fetch(id: int) -> Category:
        """ 
        takes an int and returns the Category object if found, 
        otherwise it will return None. 
        """

        return Category(id, 'Verb', datetime.now())

    @staticmethod
    def fetch_all() -> List[Category]:
        """ 
        takes no argument and returns a list of all Category objects 
        if found, otherwise return an empty list. 
        """

        return [Category(id, 'Verb', datetime.now())]

    @staticmethod
    def convert_dict_to_object(category_list: list) -> List:
        """ convert the database record into a Category object. """

        converted_category_list = [] # save the converted categories
        for data in category_list:
            category = data['category']
            id = data['id']
            created = datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')
            converted_category_list.append(
                Category(category=category, id=id, created=created)
            )

        return converted_category_list
