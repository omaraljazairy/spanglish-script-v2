import unittest
from exceptions.modelsexceptions import MissingArgs
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
                
        cls.sentence = Sentence(
            id=1, 
            sentence='Hola amigo', 
            category=Category(
                category='greeting', 
                id=1, 
                created=datetime.now()
            ), 
            created=datetime.now()
        )

        cls.language = Language(
            name='English', 
            code='EN', 
            id=1, 
            created=datetime.now()
        )
        
        cls.word = Word(
            id=1, 
            word='Hola', 
            category=Category(
                category='greeting', 
                id=1, 
                created=datetime.now()
            ), 
            created=datetime.now(),
            language=Language(
                name="Spanish",
                code="ES",
                id=1,
                created=datetime.now()
            )
        )


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

    
    def test_save_translated_word(self):
        """ provide a word_id with a language_id and a translation.
        expect a 1 to be returned. """

        saved_translation = Translation.save(
            word_id=4,
            language_id=1,
            translation='see'
            )

        self.logger.debug("saved translation: %s", saved_translation)

        self.assertEqual(saved_translation, 1)


    def test_save_translated_sentence(self):
        """ provide a sentence_id with a language_id and a translation.
        expect a 1 to be returned. """

        saved_translation = Translation.save(
            sentence_id=3,
            language_id=2,
            translation='what is your name ?'
            )

        self.logger.debug("saved translation: %s", saved_translation)

        self.assertEqual(saved_translation, 1)


    def test_save_translated_exception(self):
        """ provide no word_id and no sentence_id. Expect a MissingArgs 
        exception to be thrown. """

        with self.assertRaises(MissingArgs):
            saved_translation = Translation.save(
                language_id=2,
                translation='what is your name ?'
            )
            self.logger.debug("saved translation: %s", saved_translation)


    def test_get_translation_by_word_id(self):
        """ provide a word_id and expect back a translation dictionary. """

        translation = Translation.get_translation_by_id(word_id=1)

        self.logger.debug("returned translation: %s", translation)

        self.assertIsInstance(translation, dict)


    def test_get_translation_by_sentence_id(self):
        """ provide a sentence_id and expect back a translation dictionary. """

        translation = Translation.get_translation_by_id(sentence_id=1)

        self.logger.debug("returned translation: %s", translation)

        self.assertIsInstance(translation, dict)


    def test_get_translation_by_id_exception(self):
        """ provide no word_id and sentence_id and expect 
        back MissingArgs exception to be thrown. """

        with self.assertRaises(MissingArgs):
            Translation.get_translation_by_id()

    
    def test_update_translation_by_id(self):
        """update a word translation by providing the translation_id and translation. expect back
        1 to be returned.
        """

        translation = Translation.update_translation_by_id(id=1, translation='flo')

        self.logger.debug("returned translation: %s", translation)

        self.assertEqual(translation, 1)


    def test_update_translation_by_sentence_id(self):
        """update a word translation by providing the translation_id and translation. expect back
        1 to be returned.
        """

        translation = Translation.update_translation_by_id(id=1, translation='why amigo why ?')

        self.logger.debug("returned translation: %s", translation)

        self.assertEqual(translation, 1)


    def test_update_translation_exception(self):
        """provide translation_id without translation or language. 
        Expect a MissingArgs exception to be thrown.
        """

        with self.assertRaises(MissingArgs):
            Translation.update_translation_by_id(id=1)


    
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