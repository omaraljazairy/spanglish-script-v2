import unittest
import logging
from models.word import Word
from datetime import datetime


class WordModelTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup data before tests. """
        
        cls.logger = logging.getLogger('test')
        cls.logger.info("Setup %s Model", cls.__name__)


    def test_attributes(self):
        """ 
        expect the word model to have four instance attributes initialized
        when an instance is created.
        """

        word = Word(id=1, word='Hola', category_id=1)
        total_instance_attr = word.__dict__

        self.assertEqual(len(total_instance_attr), 4)

        self.assertTrue(word.id == 1)
        self.assertTrue(word.word == 'Hola')
        self.assertTrue(word.category_id == 1)
        self.assertEqual(type(word.created), datetime)

    def test_save(self):
        """ 
        provide a word and a category and expect a Word object to 
        be created and returned. 
        """

        word = Word(word='llamar', category_id=2)
        saved_word = word.save()

        self.logger.debug("saved word: %s", saved_word)

        self.assertIsInstance(saved_word, Word)


    def test_fetch_word(self):
        """ 
        call the static fetch method and provide the id 1 as argument. expect
        to get back an Word object.
        """

        word = Word.fetch(id = 1)

        self.logger.debug("returned word: %s", word)

        self.assertIsInstance(word, Word)


    def test_fetch_all(self):
        """ 
        call the static fetch_all method. expect to get back a list of 
        Word objects or an empty list.
        """

        word_list = Word.fetch_all()

        self.logger.debug("returned word list: %s", word_list)

        self.assertEqual(type(word_list), list)
        self.assertTrue(len(word_list) > 0)


    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)


if __name__ == '__main__':
    unittest.main()