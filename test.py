from factories import create_app
import json
import unittest


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.assertTrue(self.app is not None)

    def tearDown(self):
        pass

    def test_user_api_fields(self):
        response = self.app.get('/api/users')
        json_response = json.loads(response.data)
        users = json_response["users"]
        self.assertTrue(users is not None)
        self.assertTrue(len(users) > 0)
        self.assertTrue(users[0]["id"] is not None)
        self.assertTrue(users[0]["name"] is not None)


if __name__ == '__main__':
    unittest.main()