import unittest
import FlaskApi

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = FlaskApi.app.test_client()
        self.assertTrue(FlaskApi.app is not None)
        self.assertTrue(self.app is not None)

    def tearDown(self):
        pass

    def test_user_api(self):
        json = self.app.get('/api/users')
        print json.data


if __name__ == '__main__':
#    app = create_app()
#    print 'before app.run'
#    app.run()
#    print 'after app.run'
    unittest.main()
#    print 'after unittest.main'