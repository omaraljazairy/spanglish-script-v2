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
        cls.language = Language(name='English', code='EN', created=datetime.now())


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

        self.assertEqual(len(instance_attr), 6)

        self.assertTrue(language.id == None)
        self.assertTrue(language.name == 'English')
        self.assertTrue(language.code == 'EN')

    
    def test_save(self):
        """ provide a language name and expect a Language object to be returned. """

        saved_language = self.language.save()

        self.logger.debug("saved language: %s", saved_language)

        self.assertIsInstance(saved_language, Language)


    def test_fetch_language(self):
        """ 
        call the static fetch method and provide the id 1 as argument. expect
        to get back an Language object.
        """

        language = Language.fetch(id = 1)

        self.logger.debug("returned language: %s", language)

        self.assertIsInstance(language, Language)


    def test_fetch_all(self):
        """ 
        call the static fetch_all method. expect to get back a list of 
        Language objects or an empty list.
        """

        language_list = Language.fetch_all()

        self.logger.debug("returned language list: %s", language_list)

        self.assertEqual(type(language_list), list)
        self.assertTrue(len(language_list) > 0)



    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)




if __name__ == '__main__':
    unittest.main()