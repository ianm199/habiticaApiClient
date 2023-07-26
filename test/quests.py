import unittest
from unittest.mock import MagicMock
from src.client import HabiticaBaseClient
from src.quest import HabiticaQuestClient

class TestHabiticaQuestClient(unittest.TestCase):

    def setUp(self):
        self.client = HabiticaQuestClient("user_id", "api_key")
    
    def test_invite_users_to_quest(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.invite_users_to_quest("group_id", "quest_key")
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with("POST", "/groups/group_id/quests/invite/quest_key")
    
    def test_accept_quest(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.accept_quest("group_id")
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with("POST", "/groups/group_id/quests/accept")

    def test_reject_quest(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.reject_quest("group_id")
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with("POST", "/groups/group_id/quests/reject")

    def test_force_start_quest(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.force_start_quest("group_id")
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with("POST", "/groups/group_id/quests/force-start")

    def test_cancel_quest(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.cancel_quest("group_id")
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with("POST", "/groups/group_id/quests/cancel")

    def test_abort_quest(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.abort_quest("group_id")
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with("POST", "/groups/group_id/quests/abort")
    
    def test_leave_quest(self):
        self.client.make_request = MagicMock(return_value={"success": True})
        response = self.client.leave_quest("group_id")
        self.assertEqual(response, {"success": True})
        self.client.make_request.assert_called_once_with("POST", "/groups/group_id/quests/leave")

if __name__ == "__main__":
    unittest.main()