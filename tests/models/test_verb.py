import unittest
from models.verb import Verb
from models.word import Word
from models.category import Category
import logging
from datetime import datetime


class VerbModelTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup data before tests. """
        
        cls.logger = logging.getLogger('test')
        cls.word = Word(word='ir', category=Category(category='verb', id=2, created=datetime.now()), created=datetime.now(), id=2)
        cls.logger.info("Setup %s Model", cls.__name__)


    def test_attributes(self):
        """ 
        expect the verb model to have four instance attributes initialized
        when an instance is created.
        """

        verb = Verb(
            id=None,
            word=self.word, 
            yo='voy', 
            tu='vas', 
            usted='va',
            nosotros='vamos', 
            vosotros='vais', 
            ustedes='van',
            tense='present',
            created=datetime.now()
            )
        
        total_instance_attr = verb.__dict__

        self.assertEqual(len(total_instance_attr), 10)

        self.assertFalse(verb.id == False)
        self.assertEqual(verb.word.id, 2)
        self.assertTrue(verb.yo == 'voy')
        self.assertTrue(verb.tu == 'vas')
        self.assertEqual(verb.usted, 'va')
        self.assertEqual(verb.nosotros, 'vamos')
        self.assertEqual(verb.vosotros, 'vais')
        self.assertEqual(verb.ustedes, 'van')

    def test_save(self):
        """ 
        provide a verb and a category and expect a Verb object to 
        be created and returned. 
        """

        verb = Verb(id=1, word=self.word, yo='voy', tu='vas', usted='va', nosotros='vamos', vosotros='vais', ustedes='van', tense='persent', created=datetime.now())
        saved_verb = verb.save()

        self.logger.debug("saved verb: %s", saved_verb)

        self.assertIsInstance(saved_verb, Verb)


    def test_fetch_verb(self):
        """ 
        call the static fetch method and provide the id 1 as argument. expect
        to get back an Verb object.
        """

        verb = Verb.fetch(id = 1)

        self.logger.debug("returned verb: %s", verb)

        self.assertIsInstance(verb, Verb)
        self.assertIsInstance(verb.word, Word)


    def test_fetch_all(self):
        """ 
        call the static fetch_all method. expect to get back a list of 
        Verb objects or an empty list.
        """

        verb_list = Verb.fetch_all()

        self.logger.debug("returned verb list: %s", verb_list)

        self.assertEqual(type(verb_list), list)
        self.assertTrue(len(verb_list) > 0)


if __name__ == '__main__':
    unittest.main()