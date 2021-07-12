from datetime import datetime
import unittest
import logging
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
        instance_attr = category.__dict__

        self.logger.debug("category: %s", category)
        self.logger.debug("instance_attr: %s", instance_attr)
        self.logger.debug("mro of the category class: %s", Category.__mro__)

        self.assertEqual(len(instance_attr), 5)

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


    def test_convert_db_to_object(self):
        """ provide a list of category and expect to get back a Category object. """

        data = [{
            'category': 'foo',
            'id' : 1,
            'created': '2021-06-22 22:56:01'
        },
        {
            'category': 'bar',
            'id' : 2,
            'created': '2021-06-22 22:58:01'
        }]

        converted_categories = Category.convert_dict_to_object(category_list=data)
        

        self.logger.debug("converted_categories: %s", converted_categories)

        self.assertAlmostEqual(len(converted_categories), 2)


        
        




    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)




if __name__ == '__main__':
    unittest.main()