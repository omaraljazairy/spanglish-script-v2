from abc import ABC, abstractmethod, abstractstaticmethod

class ModelInterface(ABC):

    @abstractmethod
    def save(self):
        ''' save an initialized object to the database and return the object created. '''

    @abstractstaticmethod
    def fetch(id: int):
        ''' static method that returns a model instance or None. '''

    @abstractstaticmethod
    def fetch_all():
        ''' returns a list of the object model or empty model if not found '''