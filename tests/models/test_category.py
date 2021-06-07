import unittest
import logging
from datetime import datetime
from models.category import Category

class CategoryTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup data before tests. """
        
        cls.logger = logging.getLogger('test')
        cls.logger.info("Setup %s Model", cls.__name__)


    def test_attributes(self):
        """ 
        expect the category model to have three instance attributes initialized
        when an instance is created.
        """

        category = Category('Day')
        total_instance_attr = category.__dict__

        self.logger.debug("category: %s", category)
        self.logger.debug("total_instance_attr: %s", total_instance_attr)
        self.logger.debug("mro of the category class: %s", Category.__mro__)

        self.assertEqual(len(total_instance_attr), 3)

        self.assertTrue(category.id == None)
        self.assertTrue(category.category == 'Day')

    
    def test_save(self):
        """ provide a category name and expect a Category object to be returned. """

        category = Category('Day')
        saved_category = category.save()

        self.logger.debug("saved category: %s", saved_category)

        self.assertIsInstance(saved_category, Category)


    def test_fetch_category(self):
        """ 
        call the static fetch method and provide the id 1 as argument. expect
        to get back an Category object.
        """

        category = Category.fetch(id = 1)

        self.logger.debug("returned category: %s", category)

        self.assertIsInstance(category, Category)


    def test_fetch_all(self):
        """ 
        call the static fetch_all method. expect to get back a list of 
        Category objects or an empty list.
        """

        category_list = Category.fetch_all()

        self.logger.debug("returned category list: %s", category_list)

        self.assertEqual(type(category_list), list)
        self.assertTrue(len(category_list) > 0)



    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)




if __name__ == '__main__':
    unittest.main()