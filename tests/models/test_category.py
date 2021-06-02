import unittest
from models.category import CategoryModel


class CategoryModelTest(unittest.TestCase):

    def test_attributes(self):
        """ 
        expect the category model to have three instance attributes initialized
        when an instance is created.
        """

        category = CategoryModel(1, 'Day')
        total_instance_attr = category.__dict__

        self.assertEqual(len(total_instance_attr), 2)

        self.assertTrue(category.id == 1)
        self.assertTrue(category.category == 'Day')

if __name__ == '__main__':
    unittest.main()