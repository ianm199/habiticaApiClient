import unittest
from src.client import HabiticaBaseClient
from src.tags import HabiticaTagClient

class TestHabiticaTagClient(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv('HABITICA_TEST_API_KEY')
        user_id = os.getenv('HABITICA_TEST_USER_ID')
        self.tag_client = HabiticaTagClient(user_id, api_key)

    def test_create_tag(self):
        response = self.tag_client.create_tag("Example Tag")
        self.assertEqual(response['name'], "Example Tag")

    def test_get_user_tags(self):
        response = self.tag_client.get_user_tags()
        self.assertTrue(response, list)

    def test_get_a_tag(self):
        # Replace <tag_id> with an actual tag ID from the user's account
        tag_id = "<tag_id>"
        response = self.tag_client.get_a_tag(tag_id)
        self.assertEqual(response['id'], tag_id)

    def test_update_a_tag(self):
        # Replace <tag_id> with an actual tag ID from the user's account
        tag_id = "<tag_id>"
        response = self.tag_client.update_a_tag(tag_id, "Updated Tag Name")
        self.assertEqual(response['name'], "Updated Tag Name")

    def test_reorder_tags(self):
        # Replace <tag_id> with an actual tag ID from the user's account
        tag_id = "<tag_id>"
        response = self.tag_client.reorder_tags(tag_id, 2)
        self.assertTrue(response, dict)

    def test_delete_a_tag(self):
        # Replace <tag_id> with an actual tag ID from the user's account
        tag_id = "<tag_id>"
        response = self.tag_client.delete_a_tag(tag_id)
        self.assertEqual(response['success'], True)