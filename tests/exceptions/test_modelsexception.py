import unittest
import logging
from exceptions.modelsexceptions import MissingArgs


class ModelExceptionsTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """ setup data before tests. """
        
        cls.logger = logging.getLogger('test')
        cls.logger.info("Setup %s Model", cls.__name__)

    def test_missingargs_exception_message(self):
        """ Expect the exception to print the expected message with args. """

        required_args = (1,2,3)
        missingargs = MissingArgs(required_args=required_args)
        expected_msg = f"MISSING REQUIRED_ARGS. Required args: {required_args}"

        self.assertEqual(str(missingargs), str(expected_msg))


    @classmethod
    def teardown_class(cls):
        """ teardown all setup. """

        cls.logger.info("TearDown %s model", cls.__name__)

if __name__ == '__main__':
    unittest.main()
