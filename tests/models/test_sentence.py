import unittest
from models.sentence import SentenceModel
from datetime import datetime


class SentenceModelTest(unittest.TestCase):

    def test_attributes(self):
        """ 
        expect the sentence model to have four instance attributes initialized
        when an instance is created.
        """

        sentence = SentenceModel(1, 'Hola', 1)
        total_instance_attr = sentence.__dict__

        self.assertEqual(len(total_instance_attr), 4)

        self.assertTrue(sentence.id == 1)
        self.assertTrue(sentence.sentence == 'Hola')
        self.assertTrue(sentence.category_id == 1)
        self.assertEqual(type(sentence.created), datetime)

if __name__ == '__main__':
    unittest.main()