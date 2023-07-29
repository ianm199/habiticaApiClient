import unittest
from unittest.mock import MagicMock
from src.members import HabiticaMemberClient

class TestHabiticaMemberClient(unittest.TestCase):
    def setUp(self):
        self.client = HabiticaMemberClient("user_id", "api_key")
        self.member_id = "member_id"
        self.group_id = "group_id"
        self.challenge_id = "challenge_id"
        self.interaction = "interaction"
        self.to_user_id = "to_user_id"
        self.message = "message"
        self.gem_amount = 10

    def test_get_member_profile(self):
        self.client.make_request = MagicMock(return_value={"name": "John Doe"})
        self.assertEqual(self.client.get_member_profile(self.member_id), {"name": "John Doe"})

    def test_get_member_achievements(self):
        self.client.make_request = MagicMock(return_value={"achievements": ["completed_task"]})
        self.assertEqual(self.client.get_member_achievements(self.member_id), {"achievements": ["completed_task"]})

    def test_get_group_members(self):
        self.client.make_request = MagicMock(return_value={"members": [{"name": "John Doe"}]})
        self.assertEqual(self.client.get_group_members(self.group_id), {"members": [{"name": "John Doe"}]})

    def test_get_group_invites(self):
        self.client.make_request = MagicMock(return_value={"invites": [{"name": "Invite"}]})
        self.assertEqual(self.client.get_group_invites(self.group_id), {"invites": [{"name": "Invite"}]})

    def test_get_challenge_members(self):
        self.client.make_request = MagicMock(return_value={"members": [{"name": "John Doe"}]})
        self.assertEqual(self.client.get_challenge_members(self.challenge_id), {"members": [{"name": "John Doe"}]})

    def test_get_challenge_member_progress(self):
        self.client.make_request = MagicMock(return_value={"progress": "50%"})
        self.assertEqual(self.client.get_challenge_member_progress(self.challenge_id, self.member_id), {"progress": "50%"})

    def test_get_objections_to_interaction(self):
        self.client.make_request = MagicMock(return_value={"objections": ["interaction1", "interaction2"]})
        self.assertEqual(self.client.get_objections_to_interaction(self.to_user_id, self.interaction), {"objections": ["interaction1", "interaction2"]})

    def test_send_private_message(self):
        self.client.make_request = MagicMock(return_value={"message": "Sent"})
        self.assertEqual(self.client.send_private_message(self.message, self.to_user_id), {"message": "Sent"})

    def test_transfer_gems(self):
        self.client.make_request = MagicMock(return_value={"status": "Success"})
        self.assertEqual(self.client.transfer_gems(self.message, self.to_user_id, self.gem_amount), {"status": "Success"})

if __name__ == "__main__":
    unittest.main()
