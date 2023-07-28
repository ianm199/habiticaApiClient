import unittest
from unittest.mock import Mock
from src.cron import HabiticaCronClient

class TestHabiticaCronClient(unittest.TestCase):

    def setUp(self):
        self.cron_client = HabiticaCronClient("user", "apikey")
        self.mock_make_request = Mock()
        self.cron_client.make_request = self.mock_make_request

    def test_run_cron(self):
        data = {'key': 'value'}
        expected_response = {'response': 'data'}
        self.mock_make_request.return_value = expected_response
        
        response = self.cron_client.run_cron(data)
        
        self.assertEqual(response, expected_response)
        self.mock_make_request.assert_called_once_with('POST', '/cron', data=data)


if __name__ == '__main__':
    unittest.main()