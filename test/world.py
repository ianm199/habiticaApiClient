from client import HabiticaBaseClient
from typing import Dict

class HabiticaWorldStateClient(HabiticaBaseClient):
    def get_world_state(self) -> Dict:
        return self.make_request('GET', '/world-state')

import unittest
from unittest.mock import MagicMock
from src.client import HabiticaBaseClient
from src.world_state import HabiticaWorldStateClient

class TestHabiticaWorldStateClient(unittest.TestCase):
    
    def setUp(self):
        api_key = 'test_api_key'
        user_id = 'test_user_id'
        self.world_state_client = HabiticaWorldStateClient(user_id, api_key)
        
    def test_get_world_state(self):
        self.world_state_client.make_request = MagicMock()
        self.world_state_client.get_world_state()
        self.world_state_client.make_request.assert_called_once_with('GET', '/world-state')