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
    tense: str = 'present'
    created: datetime = datetime.now()


    def __post_init__(self):
        """This is only for dataclasses. It will be executed after the 
        automatic default init """
        super().__init__()
        self.dbase = DBModel()

    
    def save(self) -> int:
        """ 
        takes the verb object returns the generated verb if successful, 
        otherwise None will be returned.
        """

        return self


    @staticmethod
    def fetch(id: int) -> Dict:
        """ 
        takes an int of the verbId and calls create an query with one argument,
        verb_id. It will returns the verb object as a dict type if found, otherwise None
        will be returned. 
        """

        query = """select * from Verb as v join Word as w on (v.word_id = w.id) join Category as c on (w.category_id = c.id) join Language as l on (w.language_id = l.id) where v.id = ?"""
        args = [id]

        # data = Verb.dbase.fetch()


        return Verb(id=id, word=Word(id=2, word='ir', category=Category(category='verb', id=2, created=datetime.now()), created=datetime.now()), yo='voy', tu='vas', usted='va', nosotros='vamos', vosotros='vais', ustedes='van', tense='persent', created=datetime.now())


    @staticmethod
    def fetch_all() -> List[Dict]:
        """ 
        takes no arguments and returns a list of Verb objects or 
        empty list. 
        """

        return [Verb(id=id, word=Word(id=2, word='ir', category=Category(category='verb', id=2, created=datetime.now()), created=datetime.now()), yo='voy', tu='vas', usted='va', nosotros='vamos', vosotros='vais', ustedes='van', tense='persent', created=datetime.now()),]


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