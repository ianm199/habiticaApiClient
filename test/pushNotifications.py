from unittest.mock import MagicMock
import unittest
from src.pushNotifications import HabiticaPushNotifications

class TestHabiticaPushNotifications(unittest.TestCase):

    def setUp(self):
        self.push_notifications_client = HabiticaPushNotifications("USER_ID", "API_KEY")
        self.push_notifications_client.make_request = MagicMock()

    def test_add_push_device(self):
        regId = "REG_ID"
        type = "TYPE"
        self.push_notifications_client.make_request.return_value = {}
        response = self.push_notifications_client.add_push_device(regId, type)
        self.assertIsInstance(response, dict)
        self.push_notifications_client.make_request.assert_called_with('POST', '/user/push-devices', data={"regId": regId, "type": type})

    def test_remove_push_device(self):
        regId = "REG_ID"
        self.push_notifications_client.make_request.return_value = {}
        response = self.push_notifications_client.remove_push_device(regId)
        self.assertIsInstance(response, dict)
        self.push_notifications_client.make_request.assert_called_with('DELETE', f'/user/push-devices/{regId}')

if __name__ == '__main__':
    unittest.main()
