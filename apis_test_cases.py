import unittest
import apis
from apis import app
import json

class TestAPIs(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_get_all_items(self):
        response = self.client.get('/api/all_items')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        # Add more assertions based on your specific data

    def test_get_song_attributes(self):
        response = self.client.get('/api/song_attributes?title=3AM')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        # Add more assertions based on your specific data

    def test_rate_song(self):
        response = self.client.post('/api/rate_song', json={'title': '3AM', 'rating': 4.5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(apis.normalized_data.loc[apis.normalized_data['title'] == '3AM', 'star_rating'].values[0], 4.5)

if __name__ == '__main__':
    unittest.main()