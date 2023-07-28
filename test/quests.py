import unittest
from unittest.mock import Mock
from src.quests import HabiticaQuestClient

class TestHabiticaQuestClient(unittest.TestCase):

    def setUp(self):
        self.quest_client = HabiticaQuestClient("dummy_token", "dummy_user_id")

    def test_invite_users_to_quest(self):
        self.quest_client.make_request = Mock(return_value={"success": True})
        response = self.quest_client.invite_users_to_quest("dummy_group_id", "dummy_quest_key")
        self.assertEqual(response, {"success": True})
        self.quest_client.make_request.assert_called_once_with("POST", "/groups/dummy_group_id/quests/invite/dummy_quest_key")

    def test_accept_quest(self):
        self.quest_client.make_request = Mock(return_value={"success": True})
        response = self.quest_client.accept_quest("dummy_group_id")
        self.assertEqual(response, {"success": True})
        self.quest_client.make_request.assert_called_once_with("POST", "/groups/dummy_group_id/quests/accept")

    def test_reject_quest(self):
        self.quest_client.make_request = Mock(return_value={"success": True})
        response = self.quest_client.reject_quest("dummy_group_id")
        self.assertEqual(response, {"success": True})
        self.quest_client.make_request.assert_called_once_with("POST", "/groups/dummy_group_id/quests/reject")

    def test_force_start_quest(self):
        self.quest_client.make_request = Mock(return_value={"success": True})
        response = self.quest_client.force_start_quest("dummy_group_id")
        self.assertEqual(response, {"success": True})
        self.quest_client.make_request.assert_called_once_with("POST", "/groups/dummy_group_id/quests/force-start")

    def test_cancel_quest(self):
        self.quest_client.make_request = Mock(return_value={"success": True})
        response = self.quest_client.cancel_quest("dummy_group_id")
        self.assertEqual(response, {"success": True})
        self.quest_client.make_request.assert_called_once_with("POST", "/groups/dummy_group_id/quests/cancel")

    def test_abort_quest(self):
        self.quest_client.make_request = Mock(return_value={"success": True})
        response = self.quest_client.abort_quest("dummy_group_id")
        self.assertEqual(response, {"success": True})
        self.quest_client.make_request.assert_called_once_with("POST", "/groups/dummy_group_id/quests/abort")

    def test_leave_quest(self):
        self.quest_client.make_request = Mock(return_value={"success": True})
        response = self.quest_client.leave_quest("dummy_group_id")
        self.assertEqual(response, {"success": True})
        self.quest_client.make_request.assert_called_once_with("POST", "/groups/dummy_group_id/quests/leave")