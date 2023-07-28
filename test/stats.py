from unittest.mock import Mock, patch
import unittest
from src.stats import HabiticaStatsClient


class TestHabiticaUserClient(unittest.TestCase):
    def setUp(self):
        self.user_client = HabiticaStatsClient('test_user', api_key='test_key')

    def test_user_allocate(self):
        expected_response = {'stat': 'str'}
        self.user_client.make_request = Mock(return_value=expected_response)

        response = self.user_client.user_allocate(stat='str')

        self.assertEqual(response, expected_response)
        self.user_client.make_request.assert_called_once_with('POST', '/api/v3/user/allocate', params={'stat': 'str'})

    def test_user_allocate_bulk(self):
        expected_response = {'stats': {'str': 10, 'con': 5}}
        self.user_client.make_request = Mock(return_value=expected_response)

        response = self.user_client.user_allocate_bulk(stats={'str': 10, 'con': 5})

        self.assertEqual(response, expected_response)
        self.user_client.make_request.assert_called_once_with('POST', '/api/v3/user/allocate-bulk', data={'stats': {'str': 10, 'con': 5}})

    def test_user_allocate_now(self):
        expected_response = {}
        self.user_client.make_request = Mock(return_value=expected_response)

        response = self.user_client.user_allocate_now()

        self.assertEqual(response, expected_response)
        self.user_client.make_request.assert_called_once_with('POST', '/api/v3/user/allocate-now')