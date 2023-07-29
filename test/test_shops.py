import unittest
from unittest.mock import Mock
from src.client import HabiticaBaseClient
from src.shops import HabiticaShopsClient

class TestHabiticaShopsClient(unittest.TestCase):

    def setUp(self):
        user_id = '123'
        api_key = '456'
        self.client = HabiticaShopsClient(user_id, api_key)
        self.client.make_request = Mock()
        self.client.make_request.return_value = {}  # Mock method will return a dict

    def test_get_market_items(self):
        response = self.client.get_market_items()
        self.client.make_request.assert_called_once_with('GET', '/shops/market')
        self.assertIsInstance(response, dict)

    def test_get_market_gear(self):
        response = self.client.get_market_gear()
        self.client.make_request.assert_called_once_with('GET', '/shops/market-gear')
        self.assertIsInstance(response, dict)

    def test_get_quest_shop_items(self):
        response = self.client.get_quest_shop_items()
        self.client.make_request.assert_called_once_with('GET', '/shops/quests')
        self.assertIsInstance(response, dict)

    def test_get_time_travelers_shop_items(self):
        response = self.client.get_time_travelers_shop_items()
        self.client.make_request.assert_called_once_with('GET', '/shops/time-travelers')
        self.assertIsInstance(response, dict)

    def test_get_seasonal_shop_items(self):
        response = self.client.get_seasonal_shop_items()
        self.client.make_request.assert_called_once_with('GET', '/shops/seasonal')
        self.assertIsInstance(response, dict)

    def test_get_backgrounds_shop_items(self):
        response = self.client.get_backgrounds_shop_items()
        self.client.make_request.assert_called_once_with('GET', '/shops/backgrounds')
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()
