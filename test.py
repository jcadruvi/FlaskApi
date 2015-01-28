import FlaskApi
import json
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = FlaskApi.app.test_client()
        self.assertTrue(FlaskApi.app is not None)
        self.assertTrue(self.app is not None)

    def tearDown(self):
        pass

    def test_user_api(self):
        response = self.app.get('/api/users')
        jsonResponse = json.loads(response.data)
        print jsonResponse


if __name__ == '__main__':
    unittest.main()