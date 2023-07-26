import unittest
from unittest.mock import MagicMock
from src.client import HabiticaBaseClient
from src.hall import HabiticaHallClient

class TestHabiticaHallClient(unittest.TestCase):

    def setUp(self):
        self.base_client = HabiticaBaseClient("user_id", "api_key")
        self.hall_client = HabiticaHallClient("user_id", "api_key")

    def test_get_all_patrons(self):
        self.base_client.make_request = MagicMock(return_value={"valid": True})
        result = self.hall_client.get_all_patrons()
        self.assertEqual(result, {"valid": True})

    def test_get_all_heroes(self):
        self.base_client.make_request = MagicMock(return_value={"valid": True})
        result = self.hall_client.get_all_heroes()
        self.assertEqual(result, {"valid": True})

    def test_get_hero(self):
        self.base_client.make_request = MagicMock(return_value={"valid": True})
        result = self.hall_client.get_hero("hero_id")
        self.assertEqual(result, {"valid": True})

    def test_update_hero(self):
        self.base_client.make_request = MagicMock(return_value={"valid": True})
        result = self.hall_client.update_hero("hero_id", {"data": "test"})
        self.assertEqual(result, {"valid": True})

    def test_get_hero_party(self):
        self.base_client.make_request = MagicMock(return_value={"valid": True})
        result = self.hall_client.get_hero_party("group_id")
        self.assertEqual(result, {"valid": True})