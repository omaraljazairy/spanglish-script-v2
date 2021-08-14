import unittest
import logging
from models.word import Word
from models.category import Category
from models.language import Language
from exceptions.modelsexceptions import MissingArgs
from datetime import datetime


class WordModelTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup data before tests. """
        
        cls.logger = logging.getLogger('test')
        cls.category = Category(category='greeting', id=1, created=datetime.now())
        cls.language = Language(name='Spanish', code='ES', id=1, created=datetime.now())
        cls.logger.info("Setup %s Model", cls.__name__)


    def test_attributes(self):
        """ 
        expect the word model to have four instance attributes initialized
        when an instance is created.
        """

        word = Word(id=1, word='Hola', category=self.category, language=self.language)
        instance_attr = word.__dict__

        self.assertEqual(len(instance_attr), 6)

        self.assertTrue(word.id == 1)
        self.assertTrue(word.word == 'Hola')
        self.assertTrue(word.category.id == 1)
        self.assertEqual(type(word.created), datetime)

    def test_save(self):
        """ 
        provide a word with a category_id and language_id and expect a Word id to 
        be returned. 
        """

        word_id = Word.save(word='martes', language_id=2, category_id=2)

        self.logger.debug("saved word_id: %s", word_id)

        self.assertIsInstance(word_id, int)
        self.assertGreater(word_id, 0)


    def test_get_word_by_id(self):
        """ 
        call the static fetch method and provide the id 1 as argument. expect
        to get back an Word object.
        """

        word = Word.get_word_by_id(id=1)

        self.logger.debug("returned word: %s", word)

        self.assertIsInstance(word, dict)
        self.assertGreater(len(word.values()), 0)


    def test_get_words_by_category(self):
        """ 
        call the static fetch method and provide the category_id 1 as argument. expect
        to get back a list of dicts.
        """

        word = Word.get_words_by_category_language(category_id=1)

        self.logger.debug("returned word: %s", word)

        self.assertGreater(len(word), 0)


    def test_get_words_by_language(self):
        """ 
        call the static fetch method and provide the language_id 1 as argument. expect
        to get back a list of dicts.
        """

        word = Word.get_words_by_category_language(language_id=2)

        self.logger.debug("returned word: %s", word)

        self.assertGreater(len(word), 0)


    def test_get_words_by_language_category(self):
        """ 
        call the static fetch method and provide the language_id and category_id as arguments. expect
        to get back a list of dicts.
        """

        word = Word.get_words_by_category_language(language_id=2, category_id=1)

        self.logger.debug("returned word: %s", word)

        self.assertGreater(len(word), 0)


    def test_get_words_by_no_language_category(self):
        """ 
        call the static fetch method and do not provide the language_id and category_id as arguments. expect
        to get back error string.
        """

        word = Word.get_words_by_category_language()

        self.logger.debug("returned word: %s", word)

        self.assertEqual(word, "No language or category provided")


    def test_convert_db_dict_to_object(self):
        """ provide a list of words dictionaries and expect to get back a 
        list of Word objects. 
        """

        data = [
            {
                'id': 1, 
                'word': 'Ir', 
                'created': datetime(2021, 7, 27, 7, 28, 17), 
                'language_id': 2, 
                'language_name': 'Swedish', 
                'iso-639-1': 'NO', 
                'language_created': datetime(2021, 7, 27, 7, 28, 17), 
                'category_id': 1, 
                'category_name': 'Verb', 
                'category_created': datetime(2021, 7, 27, 7, 28, 17)
            },
            {
                'id': 2, 
                'word': 'Lunes', 
                'created': datetime(2021, 7, 27, 7, 28, 17), 
                'language_id': 2, 
                'language_name': 'Spanish', 
                'iso-639-1': 'ES', 
                'language_created': datetime(2021, 7, 27, 7, 28, 17), 
                'category_id': 2, 
                'category_name': 'Day', 
                'category_created': datetime(2021, 7, 27, 7, 28, 17)
            }
        ]

        converted_words = [Word.convert_dict_to_object(data=word) for word in data]
        self.logger.debug("converted_words: %s", converted_words)

        self.assertAlmostEqual(len(converted_words), 2)
        self.assertIsInstance(converted_words[0], Word)

    
    def test_update_word_by_id_language_category(self):
        """ provide a language_id and category_id to the word with id 3, 
        expect it to be changed. 
        """

        word = 'Miercoles'
        language_id = 1
        category_id = 2
        word_id = 3

        updated_word = Word.update_word_by_id(
            id=word_id, 
            word=word,
            language_id=language_id, 
            category_id=category_id
        )

        self.logger.debug("upated_word: %s", updated_word)

        self.assertGreater(updated_word, 0)


    def test_update_word_by_id_language_only(self):
        """ provide a language_id only to the word with id 2, 
        expect it to be changed. 
        """

        language_id = 1
        word_id = 2

        updated_word = Word.update_word_by_id(
            id=word_id, 
            language_id=language_id
        )

        self.logger.debug("upated_word: %s", updated_word)

        self.assertGreater(updated_word, 0)


    def test_update_word_by_id_catgory_only(self):
        """ provide a category_id only to the word with id 2, 
        expect it to be changed. 
        """

        category_id = 1
        word_id = 2

        updated_word = Word.update_word_by_id(
            id=word_id, 
            category_id=category_id
        )

        self.logger.debug("upated_word: %s", updated_word)

        self.assertGreater(updated_word, 0)


    def test_update_word_by_missing_kwargs_exception(self):
        """ call the update word without providing any kwargs. 
        """

        with self.assertRaises(MissingArgs):
            Word.update_word_by_id(id=3)


    def test_convert_db_dict_to_object_from_db(self):
        """ provide a words from the database and expect to get back a 
        list of Word objects. 
        """

        word = Word.get_word_by_id(id=1)

        self.logger.debug("returned word: %s", word)

        converted_word = Word.convert_dict_to_object(data=word)
        self.logger.debug("converted_word: %s", converted_word)

        self.assertIsInstance(converted_word, Word)


    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)


if __name__ == '__main__':
    unittest.main()
