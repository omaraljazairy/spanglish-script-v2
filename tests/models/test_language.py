import unittest
import logging
from datetime import datetime
from models.language import Language

class LanguageTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup data before tests. """
        
        cls.logger = logging.getLogger('test')
        cls.logger.info("Setup %s Model", cls.__name__)
        cls.language = Language(id=1, name='English', code='EN', created=datetime.now())


    def test_attributes(self):
        """ 
        expect the language model to have four instance attributes initialized
        when an instance is created.
        """

        language = self.language
        instance_attr = language.__dict__

        self.logger.debug("language: %s", language)
        self.logger.debug("instance_attr: %s", instance_attr)
        self.logger.debug("mro of the language class: %s", Language.__mro__)

        self.assertEqual(len(instance_attr), 5)

        self.assertTrue(language.id == 1)
        self.assertTrue(language.name == 'English')
        self.assertTrue(language.code == 'EN')

    
    def test_save_language(self):
        """ provide a language name iso-639-1 and expect the language_id to be returned. """

        de_language_name = 'Deutch'
        de_language_code = 'DE'
        saved_language = self.language.save(name=de_language_name, code=de_language_code)

        self.logger.debug("saved language: %s", saved_language)

        self.assertEqual(type(saved_language), int)
        self.assertGreater(saved_language, 0)


    def test_delete_language(self):
        """ provide a language id and expect an int to be returned. """

        deleted_language = Language.delete_language_by_id(id=4)

        self.logger.debug("deleted language: %s", deleted_language)

        self.assertEqual(type(deleted_language), int)


    def test_update_language_code_name(self):
        """ provide a language id with code and name and expect a boolean to
         be returned. """

        updated_language = Language.update_language_by_id(id=2, code='IT', name='Italian')

        self.logger.debug("updated_language: %s", updated_language)

        self.assertEqual(type(updated_language), bool)
        self.assertTrue(updated_language)

    
    def test_update_language_code_only(self):
        """ provide a language id with code only and expect a True value to
         be returned. """

        updated_language = Language.update_language_by_id(id=2, code='NO')

        self.logger.debug("updated_language: %s", updated_language)

        self.assertEqual(type(updated_language), bool)
        self.assertTrue(updated_language)

    def test_update_language_name_only(self):
        """ provide a language id with name only and expect a True value to
         be returned. """

        updated_language = Language.update_language_by_id(id=2, name='Swedish')

        self.logger.debug("updated_language: %s", updated_language)

        self.assertEqual(type(updated_language), bool)
        self.assertTrue(updated_language)


    def test_update_language_no_args_false(self):
        """ provide a language id with no name or code and expect a False value to
         be returned. """

        updated_language = Language.update_language_by_id(id=2)

        self.logger.debug("updated_language: %s", updated_language)

        self.assertEqual(type(updated_language), bool)
        self.assertFalse(updated_language)


    def test_get_language_by_id(self):
        """ 
        call the static fetch method and provide the id 1 as argument. expect
        to get back an Language object.
        """

        language = Language.get_language_by_id(id = 1)

        self.logger.debug("returned language: %s", language)

        self.assertIsInstance(language, dict)


    def test_get_all_languages(self):
        """ 
        call the static get_all method. expect to get back a list of 
        Language objects or an empty list.
        """

        language_list = Language.get_all()

        self.logger.debug("returned language list: %s", language_list)

        self.assertEqual(type(language_list), list)
        self.assertTrue(len(language_list) > 0)


    def test_convert_db_dict_to_object(self):
        """ provide a list of language dictionaries and expect to get back a 
        list of Language objects. 
        """

        data = [{
            'name': 'English',
            'id' : 1,
            'code': 'EN',
            'created': '2021-06-22 22:56:01'
        },
        {
            'name': 'Spanish',
            'id' : 2,
            'code': 'ES',
            'created': '2021-06-22 22:58:01'
        }]

        converted_languages = [Language.convert_dict_to_object(data=lan) for lan in data]
        self.logger.debug("converted_languages: %s", converted_languages)

        self.assertAlmostEqual(len(converted_languages), 2)
        self.assertIsInstance(converted_languages[0], Language)



    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)



if __name__ == '__main__':
    unittest.main()