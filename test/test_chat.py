import os
import unittest
from unittest.mock import Mock, patch
from src.chat import HabiticaChatClient, HabiticaBaseClient

class TestHabiticaChatClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = HabiticaChatClient(os.environ.get('HABITICA_TEST_USER_ID'), os.environ.get('HABITICA_TEST_API_KEY'))

    @patch.object(HabiticaBaseClient, 'make_request', return_value={"messages": []})
    def test_get_group_chat_messages(self, mock_make_request):
        response = self.client.get_group_chat_messages("123")
        self.assertEqual(response, {"messages": []})

    @patch.object(HabiticaBaseClient, 'make_request', return_value={"message": "Test Message"})
    def test_post_chat_message_to_group(self, mock_make_request):
        response = self.client.post_chat_message_to_group("123", "Test Message")
        self.assertEqual(response, {"message": "Test Message"})

    @patch.object(HabiticaBaseClient, 'make_request', return_value={"success": True})
    def test_like_group_chat_message(self, mock_make_request):
        response = self.client.like_group_chat_message("123", "456")
        self.assertEqual(response, {"success": True})

    @patch.object(HabiticaBaseClient, 'make_request', return_value={"success": True})
    def test_flag_group_chat_message(self, mock_make_request):
        response = self.client.flag_group_chat_message("123", "456", "Flag Comment")
        self.assertEqual(response, {"success": True})

    @patch.object(HabiticaBaseClient, 'make_request', return_value={"success": True})
    def test_clear_flags_group_chat_message(self, mock_make_request):
        response = self.client.clear_flags_group_chat_message("123", "456")
        self.assertEqual(response, {"success": True})

    @patch.object(HabiticaBaseClient, 'make_request', return_value={"success": True})
    def test_mark_group_messages_as_read(self, mock_make_request):
        response = self.client.mark_group_messages_as_read("123")
        self.assertEqual(response, {"success": True})

    @patch.object(HabiticaBaseClient, 'make_request', return_value={"success": True})
    def test_delete_group_chat_message(self, mock_make_request):
        response = self.client.delete_group_chat_message("123", "456", "Previous Message")
        self.assertEqual(response, {"success": True})

if __name__ == '__main__':
    unittest.main()
