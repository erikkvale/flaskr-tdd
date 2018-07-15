import unittest
import os
import tempfile
import app


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """
        Initial test, ensures Flask was setup properly
        """
        tester = app.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        """
        Initial test, ensures the database was setup
        """
        tester = os.path.exists('flaskr.db')
        self.assertTrue(tester)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up a blank temp database before each test
        """
        self.db_file_desc, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        app.init_db()

    def tearDown(self):
        """
        Destroy blank temp database after each test
        """
        os.close(self.db_file_desc)
        os.unlink(app.app.config['DATABASE'])

    def login(self, username, password):
        """
        Login helper function
        """
        return self.app.post(
            '/login',
            data=dict(
                username=username,
                password=password
            ),
            follow_redirects=True
        )

    def logout(self):
        """
        Logout helper function
        """
        return self.app.get('/logout', follow_redirects=True)

    #=======================
    # Test methods
    #=======================
    def test_empty_db(self):
        """
        Ensure database is blank
        """
        pass

    def test_login_logout(self):
        """
        Test login and logout with helper functions
        """
        pass

    def test_messages(self):
        """
        Test user can post messges
        """
        pass




if __name__=='__main__':
    unittest.main()
