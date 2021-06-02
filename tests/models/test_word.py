import unittest
from models.word import WordModel
from datetime import datetime


class WordModelTest(unittest.TestCase):

    def test_attributes(self):
        """ 
        expect the word model to have four instance attributes initialized
        when an instance is created.
        """

        word = WordModel(1, 'Hola', 1)
        total_instance_attr = word.__dict__

        self.assertEqual(len(total_instance_attr), 4)

        self.assertTrue(word.id == 1)
        self.assertTrue(word.word == 'Hola')
        self.assertTrue(word.category_id == 1)
        self.assertEqual(type(word.created), datetime)

if __name__ == '__main__':
    unittest.main()