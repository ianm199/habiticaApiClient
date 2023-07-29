import unittest
from unittest.mock import Mock
from src.inbox import HabiticaInboxClient


class TestHabiticaInboxClient(unittest.TestCase):

    def setUp(self):
        self.client = HabiticaInboxClient("user", "pass")

    def test_get_inbox_messages_without_params(self):
        mock_response = Mock()
        mock_response.return_value = {'messages': []}
        self.client.make_request = mock_response

        result = self.client.get_inbox_messages()

        self.assertEqual(result, {'messages': []})
        self.client.make_request.assert_called_once_with('GET', '/inbox/messages', params={})

    def test_get_inbox_messages_with_page(self):
        mock_response = Mock()
        mock_response.return_value = {'messages': []}
        self.client.make_request = mock_response

        result = self.client.get_inbox_messages(page=1)

        self.assertEqual(result, {'messages': []})
        self.client.make_request.assert_called_once_with('GET', '/inbox/messages', params={'page': 1})

    def test_get_inbox_messages_with_conversation(self):
        mock_response = Mock()
        mock_response.return_value = {'messages': []}
        self.client.make_request = mock_response

        result = self.client.get_inbox_messages(conversation='conversation_id')

        self.assertEqual(result, {'messages': []})
        self.client.make_request.assert_called_once_with('GET', '/inbox/messages', params={'conversation': 'conversation_id'})

    def test_get_inbox_messages_with_page_and_conversation(self):
        mock_response = Mock()
        mock_response.return_value = {'messages': []}
        self.client.make_request = mock_response

        result = self.client.get_inbox_messages(page=1, conversation='conversation_id')

        self.assertEqual(result, {'messages': []})
        self.client.make_request.assert_called_once_with('GET', '/inbox/messages', params={'page': 1, 'conversation': 'conversation_id'})