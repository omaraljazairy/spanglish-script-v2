import unittest
from models.verb import VerbModel
from models.word import WordModel
from datetime import datetime


class VerbModelTest(unittest.TestCase):

    def test_attributes(self):
        """ 
        expect the verb model to have four instance attributes initialized
        when an instance is created.
        """

        word = WordModel(1, 'ir', 1)
        verb = VerbModel(word, 'voy', 'vas', 'va', 'vamos', 'vais', 'van', 'present')
        total_instance_attr = verb.__dict__

        self.assertEqual(len(total_instance_attr), 9)

        self.assertFalse(verb.id == False)
        self.assertEqual(verb.word.id, 1)
        self.assertTrue(verb.yo == 'voy')
        self.assertTrue(verb.tu == 'vas')
        self.assertEqual(verb.usted, 'va')
        self.assertEqual(verb.nosotros, 'vamos')
        self.assertEqual(verb.vosotros, 'vais')
        self.assertEqual(verb.ustedes, 'van')

if __name__ == '__main__':
    unittest.main()