import unittest
import logging
from models.sentence import Sentence
from models.category import Category
from datetime import datetime

class SentenceModelTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup data before tests. """
        
        cls.logger = logging.getLogger('test')
        cls.category = Category(category='greeting', id=1, created=datetime.now())
        cls.logger.info("Setup %s Model", cls.__name__)
        

    def test_attributes(self):
        """ 
        expect the sentence model to have four instance attributes initialized
        when an instance is created.
        """

        sentence = Sentence(sentence='Hola amiga', category=self.category)
        total_instance_attr = sentence.__dict__

        self.logger.debug("category: %s", sentence)
        self.logger.debug("total_instance_attr: %s", total_instance_attr)
        self.logger.debug("mro of the category class: %s", Sentence.__mro__)
        
        self.assertEqual(len(total_instance_attr), 4)
        self.assertTrue(sentence.id == None)
        self.assertTrue(sentence.sentence == 'Hola amiga')
        self.assertTrue(sentence.category.id == 1)
        self.assertEqual(type(sentence.created), datetime)

    
    def test_save(self):
        """ provide a sentence name and expect a Sentence object to be returned. """

        sentence = Sentence(sentence='que dia es hoy', category=self.category)
        saved_sentence = sentence.save()

        self.logger.debug("saved sentence: %s", saved_sentence)

        self.assertIsInstance(saved_sentence, Sentence)


    def test_fetch_sentence(self):
        """ 
        call the static fetch method and provide the id 1 as argument. expect
        to get back an Sentence object.
        """

        sentence = Sentence.fetch(id = 1)

        self.logger.debug("returned sentence: %s", sentence)

        self.assertIsInstance(sentence, Sentence)
        self.assertIsInstance(sentence.category, Category)


    def test_fetch_all(self):
        """ 
        call the static fetch_all method. expect to get back a list of 
        Sentence objects or an empty list.
        """

        sentence_list = Sentence.fetch_all()

        self.logger.debug("returned sentence list: %s", sentence_list)

        self.assertEqual(type(sentence_list), list)
        self.assertTrue(len(sentence_list) > 0)


    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)


if __name__ == '__main__':
    unittest.main()