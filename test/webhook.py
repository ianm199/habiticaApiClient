import unittest
from unittest.mock import patch, MagicMock
from src.webhook import HabiticaWebhookClient

class TestHabiticaWebhookClient(unittest.TestCase):

    def setUp(self):
        self.client = HabiticaWebhookClient("test", "apikey")

    def test_create_webhook(self):
        with patch.object(self.client, 'make_request') as mock_make_request:
            mock_make_request.return_value = {}

            response = self.client.create_webhook(url="https://example.com")

            mock_make_request.assert_called_once_with('POST', '/user/webhook', data={"url": "https://example.com"})
            self.assertEqual(response, {})

    def test_get_webhooks(self):
        with patch.object(self.client, 'make_request') as mock_make_request:
            mock_make_request.return_value = {}

            response = self.client.get_webhooks()

            mock_make_request.assert_called_once_with('GET', '/user/webhook')
            self.assertEqual(response, {})

    def test_edit_webhook(self):
        with patch.object(self.client, 'make_request') as mock_make_request:
            mock_make_request.return_value = {}

            response = self.client.edit_webhook(id="webhook_id", url="https://example.com")

            mock_make_request.assert_called_once_with('PUT', '/user/webhook/webhook_id', data={"url": "https://example.com"})
            self.assertEqual(response, {})

    def test_delete_webhook(self):
        with patch.object(self.client, 'make_request') as mock_make_request:
            mock_make_request.return_value = {}

            response = self.client.delete_webhook(id="webhook_id")

            mock_make_request.assert_called_once_with('DELETE', '/user/webhook/webhook_id')
            self.assertEqual(response, {})