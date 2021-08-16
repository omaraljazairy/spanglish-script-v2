from enums.dbenums import VerbTense
from exceptions.modelsexceptions import MissingArgs
import unittest
from models.language import Language
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
        cls.word = Word(
            word='ir', 
            category=Category(
                category='verb', 
                id=2, 
                created=datetime.now()
            ), 
            created=datetime.now(), id=2,
            language=Language(
                name="Spanish",
                code="ES",
                id=1,
                created=datetime.now()
            )
        )
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
            tense=VerbTense.PRESENT_PERFECT,
            created=datetime.now()
            )
        
        instance_attr = verb.__dict__

        self.assertEqual(len(instance_attr), 11)

        self.assertFalse(verb.id == False)
        self.assertEqual(verb.word.id, 2)
        self.assertTrue(verb.yo == 'voy')
        self.assertTrue(verb.tu == 'vas')
        self.assertEqual(verb.usted, 'va')
        self.assertEqual(verb.nosotros, 'vamos')
        self.assertEqual(verb.vosotros, 'vais')
        self.assertEqual(verb.ustedes, 'van')
        self.assertEqual(verb.tense, VerbTense.PRESENT_PERFECT)

    def test_save(self):
        """ 
        provide a verb and a category and expect a Verb to 
        be created and an int to be returned. 
        """

        saved_verb = Verb.save(
            word_id=5, 
            yo='se', 
            tu='sabes', 
            usted='sabe', 
            nosotros='sabemos', 
            vosotros='sabeis', 
            ustedes='saben', 
            tense=VerbTense.PRESENT_PERFECT.value)

        self.logger.debug("saved verb: %s", saved_verb)

        self.assertGreater(saved_verb, 0)


    def test_get_verb_by_verb_id(self):
        """ 
        call the classmethod fetch_verb_by_id and provide the id 1 as argument. expect
        to get back an Verb dict.
        """

        verb = Verb.get_verb_by_id(verb_id = 1)

        self.logger.debug("returned verb: %s", verb)

        self.assertIsInstance(verb, dict)
        self.assertTrue(verb)


    def test_get_verb_by_word_id(self):
        """ 
        call the classmethod get_verb_by_id  and provide the word_id 1 as argument. expect
        to get back an Verb dict.
        """

        verb = Verb.get_verb_by_id(word_id= 1)

        self.logger.debug("returned verb: %s", verb)

        self.assertIsInstance(verb, dict)
        self.assertTrue(verb)


    def test_get_verb_by_id_exception(self):
        """ 
        call the classmethod get_verb_by_id without an verb_id or word_id. 
        expect an exception to be thrown.
        """

        with self.assertRaises(MissingArgs):
            Verb.get_verb_by_id()


    def test_get_all_verbs_by_word_or_all(self):
        """ 
        call the classmethod get_all_verbs_by_word_or_all method by providing a word string. expect to get back a list of 
        Verbs dict.
        """

        verb_list = Verb.get_all_verbs_by_word_or_all(word='%er')

        self.logger.debug("returned verb list: %s", verb_list)

        self.assertEqual(type(verb_list), list)
        self.assertTrue(len(verb_list) > 0)


    def test_get_all_verbs_by_word_or_all(self):
        """ 
        call the classmethod get_all_verbs_by_word_or_all method by not providing anything args. expect to get back a list of 
        all Verbs as dicts.
        """

        verb_list = Verb.get_all_verbs_by_word_or_all()

        self.logger.debug("returned verb list: %s", verb_list)

        self.assertEqual(type(verb_list), list)
        self.assertTrue(len(verb_list) > 1)


    def test_update_verb_success(self):
        """provide a word_id and the verb attr and expect to get back the result 1.
        """

        word_id = 3
        yo = 'voy'
        nosotros = 'vemos'
        
        updated_verb = Verb.update_verb_by_word_id(
            word_id=word_id,
            yo=yo,
            nosotros=nosotros
        )

        self.logger.debug("updated_verb = %s", updated_verb)

        self.assertGreater(updated_verb, 0)


    def test_update_verb_exception(self):
        """provide a word_id only and expect the exception MissingArgs to be raised. """
        
        with self.assertRaises(MissingArgs):
            Verb.update_verb_by_word_id(word_id=3)


    def test_convert_db_dict_to_object(self):
        """ provide a list of verb dictionaries and expect to get back a 
        list of Verb objects. 
        """

        data = [
            {
                'id': 1,
                'yo': 'voy',
                'tu': 'vas',
                'usted': 'va',
                'nosotros': 'vamos',
                'vosotros': 'vais',
                'ustedes': 'van',
                'created': '2021-06-22 22:58:01',
                'word': {
                    'word': 'ir',
                    'id': 1,
                    'created': '2021-06-22 22:56:01',
                    'category': {
                        'category': 'verb',
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
            },
            {
                'id': 2,
                'yo': 'veo',
                'tu': 'ves',
                'usted': 've',
                'nosotros': 'vemos',
                'vosotros': 'veis',
                'ustedes': 'ven',
                'created': '2021-06-22 22:58:01',
                'word': {
                    'word': 'ver',
                    'id': 3,
                    'created': '2021-06-22 22:56:01',
                    'category': {
                        'category': 'verb',
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
            }
        ]

        converted_verb = [Verb.convert_dict_to_object(data=verb) for verb in data]
        self.logger.debug("converted_verb: %s", converted_verb)

        self.assertAlmostEqual(len(converted_verb), 2)
        self.assertIsInstance(converted_verb[0], Verb)



if __name__ == '__main__':
    unittest.main()