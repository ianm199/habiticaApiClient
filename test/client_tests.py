import os
import unittest
import requests_mock
from src.client import HabiticaBaseClient

class TestHabiticaBaseClient(unittest.TestCase):
    def setUp(self):
        self.api_user = os.environ['HABITICA_API_KEY']
        self.api_key = os.environ['HABITICA_USER_ID']
        self.base_url = 'https://habitica.com/api/v3'
        self.client = HabiticaBaseClient(self.api_user, self.api_key, self.base_url)

    def test_status_live(self):
        status = self.client.status()
        self.assertEqual(status['data']['status'], 'up')

    @requests_mock.Mocker()
    def test_status_mock(self, m):
        m.get(self.base_url + '/status', json={'status': 'up'})
        status = self.client.status()
        self.assertEqual(status['status'], 'up')


if __name__ == '__main__':
    unittest.main()
