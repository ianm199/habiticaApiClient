from unittest.mock import MagicMock
from src.world import HabiticaWorldStateClient
import unittest

class TestHabiticaWorldStateClient(unittest.TestCase):
    def setUp(self):
        api_key = 'test_api_key'
        user_id = 'test_user_id'
        self.client = HabiticaWorldStateClient(user_id, api_key)

    def test_get_world_state(self):
        expected_result = {'key': 'value'}
        self.client.make_request = MagicMock(return_value=expected_result)
        result = self.client.get_world_state()
        self.assertEqual(result, expected_result)