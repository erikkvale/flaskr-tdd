import unittest
import os
from app import app


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """
        Initial test, ensures Flask was setup properly
        """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        """
        Initial test, ensures the database was setup
        """
        tester = os.path.exists('flaskr.db')
        self.assertTrue(tester)

if __name__=='__main__':
    unittest.main()
