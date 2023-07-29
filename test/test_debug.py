from unittest.mock import MagicMock
import unittest
from src.debug import HabiticaDevelopmentClient

class TestHabiticaDevelopmentClient(unittest.TestCase):

    def setUp(self):
        self.client = HabiticaDevelopmentClient("user_id", "api_key")

    def test_add_ten_gems(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.add_ten_gems()
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with('POST', '/debug/add-ten-gems')

    def test_add_hourglass(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.add_hourglass()
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with('POST', '/debug/add-hourglass')

    def test_set_cron(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.set_cron()
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with('POST', '/debug/set-cron')

    def test_make_admin(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.make_admin()
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with('POST', '/debug/make-admin')

    def test_modify_inventory(self):
        gear_data = {"item1": {"name": "item1", "value": 10}}
        special_data = {"special1": {"name": "special1", "value": 5}}
        pets_data = {"pet1": {"name": "pet1", "value": 3}}
        mounts_data = {"mount1": {"name": "mount1", "value": 2}}
        eggs_data = {"egg1": {"name": "egg1", "value": 1}}
        hatchingPotions_data = {"potion1": {"name": "potion1", "value": 1}}
        food_data = {"food1": {"name": "food1", "value": 1}}
        quests_data = {"quest1": {"name": "quest1", "value": 5}}
        expected_data = {
            "gear": gear_data,
            "special": special_data,
            "pets": pets_data,
            "mounts": mounts_data,
            "eggs": eggs_data,
            "hatchingPotions": hatchingPotions_data,
            "food": food_data,
            "quests": quests_data
        }
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.modify_inventory(
            gear_data, special_data, pets_data,
            mounts_data, eggs_data, hatchingPotions_data,
            food_data, quests_data
        )
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with('POST', '/debug/modify-inventory', data=expected_data)

    def test_quest_progress(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.quest_progress()
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with('POST', '/debug/quest-progress')

if __name__ == '__main__':
    unittest.main()