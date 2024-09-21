import unittest
import requests


class TestPublicationApi(unittest.TestCase):
    def setUp(self) -> None:
        payload = {
            'title': 'foo',
            "body": "bar",
            "userId": 1
        }
        headers = {"Content-Type": 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=payload,
            headers=headers
        )
        data = response.json()
        print(f'Created publication with ID {data["id"]}')
        # self.publication_id = data['id']
        self.publication_id = 42
        return data['id']

    def tearDown(self) -> None:
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.publication_id}')
        print(f'Post {self.publication_id} deleted')

    @staticmethod
    def prep_data():
        return 'TEXT'

    def test_update_with_put(self):
        payload = {
            'title': 'fooUPD',
            "body": "barUPD",
            "userId": 1
        }
        headers = {"Content-Type": 'application/json'}
        response = requests.put(
            f'https://jsonplaceholder.typicode.com/posts/{self.publication_id}',
            json=payload,
            headers=headers
        )
        print(response.status_code)
        data = response.json()
        self.assertEqual(data['title'], payload['title'])
        self.assertEqual(data['body'], payload['body'])


class TestNoPrep(unittest.TestCase):
    def test_get_all(self):
        expected = 100
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        data = response.json()
        self.assertEqual(len(data), expected)
