from abc import ABC, abstractclassmethod, abstractstaticmethod
import logging
from typing import Dict
from dataclasses import dataclass
import configs.dbtables as tables

@dataclass
class BaseModel(ABC):
    """ this is the base model that all models will inherit from. """

    tables = tables

    def __init__(self) -> None:
        self.logger = logging.getLogger('models')


    @abstractclassmethod
    def convert_dict_to_object(cls, data:Dict) -> object:
        ''' convert the records fetched from the database to a class object. '''

        return cls

