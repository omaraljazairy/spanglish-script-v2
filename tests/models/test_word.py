import unittest
import logging
from models.word import Word
from models.category import Category
from datetime import datetime


class WordModelTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup data before tests. """
        
        cls.logger = logging.getLogger('test')
        cls.category = Category(category='greeting', id=1, created=datetime.now())
        cls.logger.info("Setup %s Model", cls.__name__)


    def test_attributes(self):
        """ 
        expect the word model to have four instance attributes initialized
        when an instance is created.
        """

        word = Word(id=1, word='Hola', category=self.category)
        instance_attr = word.__dict__

        self.assertEqual(len(instance_attr), 6)

        self.assertTrue(word.id == 1)
        self.assertTrue(word.word == 'Hola')
        self.assertTrue(word.category.id == 1)
        self.assertEqual(type(word.created), datetime)

    def test_save(self):
        """ 
        provide a word and a category and expect a Word object to 
        be created and returned. 
        """

        word = Word(word='llamar', category=self.category)
        saved_word = word.save()

        self.logger.debug("saved word: %s", saved_word)

        self.assertIsInstance(saved_word, Word)
        self.assertIsInstance(saved_word.category, Category)


    def test_fetch_word(self):
        """ 
        call the static fetch method and provide the id 1 as argument. expect
        to get back an Word object.
        """

        word = Word.fetch(id = 1)

        self.logger.debug("returned word: %s", word)

        self.assertIsInstance(word, dict)


    def test_fetch_all(self):
        """ 
        call the static fetch_all method. expect to get back a list of 
        Word objects or an empty list.
        """

        word_list = Word.fetch_all()

        self.logger.debug("returned word list: %s", word_list)

        self.assertEqual(type(word_list), list)
        self.assertTrue(len(word_list) > 0)


    def test_convert_db_dict_to_object(self):
        """ provide a list of words dictionaries and expect to get back a 
        list of Word objects. 
        """

        data = [
            {
                'word': 'Hola',
                'id': 1,
                'created': '2021-06-22 22:56:01',
                'category': {
                    'category': 'foo',
                    'id' : 1,
                    'created': '2021-06-22 22:56:01'
                },
                'language': {
                    'name': 'Spanish',
                    'id' : 2,
                    'code': 'ES',
                    'created': '2021-06-22 22:58:01'
                }
            },
            {
                'word': 'dia',
                'id': 2,
                'created': '2021-06-22 22:57:01',
                'category': {
                    'category': 'bar',
                    'id' : 2,
                    'created': '2021-06-22 22:58:01'
                },
                'language': {
                    'name': 'English',
                    'id' : 1,
                    'code': 'EN',
                    'created': '2021-06-22 22:56:01'
                }
            }]

        converted_words = [Word.convert_dict_to_object(data=word) for word in data]
        self.logger.debug("converted_words: %s", converted_words)

        self.assertAlmostEqual(len(converted_words), 2)
        self.assertIsInstance(converted_words[0], Word)


    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)


if __name__ == '__main__':
    unittest.main()
