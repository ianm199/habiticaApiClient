import unittest
from typing import Dict
from src.client import HabiticaBaseClient

class TestHabiticaShopsClient(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv('HABITICA_TEST_API_KEY')
        user_id = os.getenv('HABITICA_TEST_USER_ID')
        self.shops_client = HabiticaShopsClient(user_id, api_key)

    def test_get_market_items(self):
        response = self.shops_client.get_market_items()
        self.assertTrue(isinstance(response, Dict))

    def test_get_market_gear(self):
        response = self.shops_client.get_market_gear()
        self.assertTrue(isinstance(response, Dict))

    def test_get_quest_shop_items(self):
        response = self.shops_client.get_quest_shop_items()
        self.assertTrue(isinstance(response, Dict))

    def test_get_time_travelers_shop_items(self):
        response = self.shops_client.get_time_travelers_shop_items()
        self.assertTrue(isinstance(response, Dict))

    def test_get_seasonal_shop_items(self):
        response = self.shops_client.get_seasonal_shop_items()
        self.assertTrue(isinstance(response, Dict))

    def test_get_backgrounds_shop_items(self):
        response = self.shops_client.get_backgrounds_shop_items()
        self.assertTrue(isinstance(response, Dict))