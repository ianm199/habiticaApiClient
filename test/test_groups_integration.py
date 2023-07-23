import os
import unittest
from dotenv import load_dotenv
from src.groups import HabiticaGroupClient

load_dotenv(".env")
class TestHabiticaGroupClient(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv('HABITICA_TEST_API_KEY')
        user_id = os.getenv('HABITICA_TEST_USER_ID')
        self.group_client = HabiticaGroupClient(user_id, api_key)
        # self.dummy_group = self.group_client.create_group("Dummy Group", group_type="guild", privacy="public")

    @unittest.skipIf(True, reason="Not enough gems to run posts for this")
    def test_create_group(self):
        response = self.group_client.create_group("Test Group", group_type="guild", privacy="public")
        self.assertTrue(response)
        self.assertEqual(response['name'], "Test Group")
        self.assertEqual(response['type'], "guild")
        self.assertEqual(response['privacy'], "private")

    # @unittest.skipIf(True, reason="Not enough gems to run posts for this")
    def test_get_groups(self):
        response = self.group_client.get_user_groups(group_type="tavern")
        self.assertIsInstance(response, list)

    def test_get_group(self):
        tavern_id = "00000000-0000-4000-A000-000000000000"
        response = self.group_client.get_group(tavern_id)
        self.assertTrue(response)
        self.assertEqual(response['id'], tavern_id)

    @unittest.skipIf(True, reason="Not enough gems to run posts for this")
    def test_update_group(self):
        updated_group_name = "Updated Dummy Group"
        self.group_client.update_group(self.dummy_group['id'], data={"name": updated_group_name})
        updated_group = self.group_client.get_group(self.dummy_group['id'])
        self.assertEqual(updated_group['name'], updated_group_name)

    def test_join_group(self):
        party_wanted_group = "f2db2a7f-13c5-454d-b3ee-ea1f5089e601"
        self.group_client.join_group(party_wanted_group)
        self.group_client.leave_group(party_wanted_group, keep="keep-all", keep_challenges="leave-challenges")

    @unittest.skipIf(True, reason="Not enough gems to run posts for this")
    def test_reject_group_invite(self):
        self.group_client.reject_group_invite(self.dummy_group['id'])
        # similarly, there's no direct way to test this, so just ensure the API call doesn't raise an error

    @unittest.skipIf(True, reason="Not enough gems to run posts for this")
    def test_remove_group_member(self):
        # Here, you'll need to create a new user, add it to the group, and then remove it
        # This may be complicated as you'll need a separate user to test with
        # In absence of a separate user, you can just ensure the API call doesn't raise an error
        self.group_client.remove_group_member(self.dummy_group['id'], "dummy_member_id")

    @unittest.skipIf(True, reason="Not enough gems to run posts for this")
    def test_invite_to_group(self):
        emails = [{"email": "testemail@example.com", "name": "Test User"}]
        uuids = ["dummy_user_uuid"]
        response = self.group_client.invite_to_group(self.dummy_group['id'], emails, uuids)
        self.assertTrue(response)

    @unittest.skipIf(True, reason="Not enough gems to run posts for this")
    def test_add_group_manager(self):
        # Note: You can't actually add yourself as a manager to a group via the API
        # So, just ensure the API call doesn't raise an error
        self.group_client.add_group_manager(self.dummy_group['id'])

    @unittest.skipIf(True, reason="Not enough gems to run posts for this")
    def test_remove_group_manager(self):
        # Note: You can't actually remove yourself as a manager from a group via the API
        # So, just ensure the API call doesn't raise an error
        self.group_client.remove_group_manager(self.dummy_group['id'])

    @unittest.skipIf(True, reason="Not enough gems to run posts for this")
    def test_get_group_plans(self):
        response = self.group_client.get_group_plans()
        self.assertIsInstance(response, list)

    @unittest.skipIf(True, reason="Need to be a leader of a party")
    def test_get_looking_for_party(self):
        response = self.group_client.get_looking_for_party(page=0)
        self.assertIsInstance(response, list)
