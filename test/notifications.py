from unittest.mock import MagicMock
import unittest
from src.notifications import HabiticaNotificationClient

class TestHabiticaNotificationClient(unittest.TestCase):

    def setUp(self):
        self.notification_client = HabiticaNotificationClient("USER_ID", "API_KEY")
        self.notification_client.make_request = MagicMock()

    def test_mark_notification_as_read(self):
        notification_id = "NOTIFICATION_ID"
        self.notification_client.make_request.return_value = {}
        response = self.notification_client.mark_notification_as_read(notification_id)
        self.assertIsInstance(response, dict)
        self.notification_client.make_request.assert_called_with('POST', f'/notifications/{notification_id}/read')

    def test_mark_multiple_notifications_as_read(self):
        self.notification_client.make_request.return_value = {}
        response = self.notification_client.mark_multiple_notifications_as_read()
        self.assertIsInstance(response, dict)
        self.notification_client.make_request.assert_called_with('POST', '/notifications/read')

    def test_mark_notification_as_seen(self):
        notification_id = "NOTIFICATION_ID"
        self.notification_client.make_request.return_value = {}
        response = self.notification_client.mark_notification_as_seen(notification_id)
        self.assertIsInstance(response, dict)
        self.notification_client.make_request.assert_called_with('POST', f'/notifications/{notification_id}/see')

    def test_mark_multiple_notifications_as_seen(self):
        self.notification_client.make_request.return_value = {}
        response = self.notification_client.mark_multiple_notifications_as_seen()
        self.assertIsInstance(response, dict)
        self.notification_client.make_request.assert_called_with('POST', '/notifications/see')

if __name__ == '__main__':
    unittest.main()
