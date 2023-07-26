import unittest
from src.client import HabiticaMemberClient

class TestHabiticaMemberClient(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv('HABITICA_TEST_API_KEY')
        user_id = os.getenv('HABITICA_TEST_USER_ID')
        self.member_client = HabiticaMemberClient(user_id, api_key)
    
    def test_get_member_profile(self):
        member_profile = self.member_client.get_member_profile(member_id="test_member_id")
        self.assertIsInstance(member_profile, dict)
    
    def test_get_member_achievements(self):
        member_achievements = self.member_client.get_member_achievements(member_id="test_member_id")
        self.assertIsInstance(member_achievements, dict)

    def test_get_group_members(self):
        group_members = self.member_client.get_group_members(group_id="test_group_id")
        self.assertIsInstance(group_members, dict)

    def test_get_group_invites(self):
        group_invites = self.member_client.get_group_invites(group_id="test_group_id")
        self.assertIsInstance(group_invites, dict)

    def test_get_challenge_members(self):
        challenge_members = self.member_client.get_challenge_members(challenge_id="test_challenge_id")
        self.assertIsInstance(challenge_members, dict)

    def test_get_challenge_member_progress(self):
        challenge_member_progress = self.member_client.get_challenge_member_progress(challenge_id="test_challenge_id", member_id="test_member_id")
        self.assertIsInstance(challenge_member_progress, dict)

    def test_get_objections_to_interaction(self):
        objections_to_interaction = self.member_client.get_objections_to_interaction(to_user_id="test_user_id", interaction="test_interaction")
        self.assertIsInstance(objections_to_interaction, dict)

    def test_send_private_message(self):
        private_message = self.member_client.send_private_message(message="test_message", to_user_id="test_user_id")
        self.assertIsInstance(private_message, dict)

    def test_transfer_gems(self):
        transfer_gems = self.member_client.transfer_gems(message="test_message", to_user_id="test_user_id", gem_amount=10)
        self.assertIsInstance(transfer_gems, dict)