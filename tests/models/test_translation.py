import unittest
import logging
from datetime import datetime
from models.translation import Category
from models.word import Word
from models.sentence import Sentence
from models.language import Language
from models.translation import Translation

class TranslationTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup data before tests. """
        
        cls.logger = logging.getLogger('test')
        cls.logger.info("Setup %s Model", cls.__name__)
                
        cls.word = Word(id=1, word='Hola', category=Category(category='greeting', id=1, created=datetime.now()), created=datetime.now())

        cls.sentence = Sentence(id=1, sentence='Hola amigo', category=Category(category='greeting', id=1, created=datetime.now()), created=datetime.now())

        cls.language = Language(name='English', code='EN', id=1, created=datetime.now())


        cls.translation_word = Translation(id=1, translation='Hello', language=cls.language, word=cls.word, created=datetime.now())
            
        cls.translation_sentence = Translation(id=2, translation='Hello friend', language=cls.language, sentence=cls.sentence, created=datetime.now())


    def test_attributes(self):
        """ 
        expect the translation model to have six instance attributes initialized
        when an instance is created.
        """

        tranlsation = self.translation_word
        instance_attr = tranlsation.__dict__

        self.logger.debug("translation: %s", tranlsation)
        self.logger.debug("instance_attr: %s", instance_attr)
        self.logger.debug("mro of the translation class: %s", Translation.__mro__)

        self.assertEqual(len(instance_attr), 7)

        self.assertTrue(tranlsation.id == 1)
        self.assertTrue(tranlsation.word.id == 1)

    
    def test_save(self):
        """ provide a translation name and expect a Translation object to be returned. """

        translation = self.translation_sentence
        saved_translation = translation.save()

        self.logger.debug("saved translation: %s", saved_translation)

        self.assertIsInstance(saved_translation, int)


    def test_fetch_translation(self):
        """ 
        call the static fetch method and provide the id 1 as argument. expect
        to get back an Translation object.
        """

        translation = Translation.fetch(id = 1)

        self.logger.debug("returned translation: %s", translation)

        self.assertIsInstance(translation, dict)


    def test_fetch_all(self):
        """ 
        call the static fetch_all method. expect to get back a list of 
        Translation objects or an empty list.
        """

        translation_list = Translation.fetch_all()

        self.logger.debug("returned translation list: %s", translation_list)

        self.assertEqual(type(translation_list), list)
        self.assertTrue(len(translation_list) > 0)

    
    def test_convert_db_dict_to_object(self):
        """ provide a list of translation dictionaries and expect to get back a 
        list of translation objects. 
        """

        data = [
            {
                'translation': 'Hello',
                'created': '2021-06-22 22:58:01',
                'id': 1,
                'word': {
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
                'language': {
                    'name': 'English',
                    'id' : 1,
                    'code': 'EN',
                    'created': '2021-06-22 22:58:01'
                }
            },
            {
                'translation': 'Hello Friend',
                'created': '2021-06-22 22:58:01',
                'id': 2,
                'sentence': {
                    'sentence': 'Hola amigo',
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
                'language': {
                    'name': 'English',
                    'id' : 1,
                    'code': 'EN',
                    'created': '2021-06-22 22:58:01'
                }
            }
        ]

        converted_translations = [Translation.convert_dict_to_object(data=tra) for tra in data]
        self.logger.debug("converted_translations: %s", converted_translations)

        self.assertAlmostEqual(len(converted_translations), 2)
        self.assertIsInstance(converted_translations[0], Translation)





    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)




if __name__ == '__main__':
    unittest.main()