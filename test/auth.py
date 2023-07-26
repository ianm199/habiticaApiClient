import unittest
from src.client import HabiticaBaseClient
from src.user import HabiticaUserClient

class TestHabiticaUserClient(unittest.TestCase):

    def setUp(self):
        self.user_client = HabiticaUserClient("12345", "test_api_key")

    def test_register_local(self):
        response = self.user_client.register_local("test_user", "test@example.com", "password", "password")
        self.assertEqual(response.status_code, 200)

    def test_login_local(self):
        response = self.user_client.login_local("test_user", "password")
        self.assertEqual(response.status_code, 200)

    def test_update_username(self):
        response = self.user_client.update_username("new_username", "password")
        self.assertEqual(response.status_code, 200)

    def test_update_password(self):
        response = self.user_client.update_password("current_password", "new_password", "new_password")
        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        response = self.user_client.reset_password("test@example.com")
        self.assertEqual(response.status_code, 200)

    def test_update_email(self):
        response = self.user_client.update_email("new_email@example.com", "password")
        self.assertEqual(response.status_code, 200)

    def test_reset_password_set_new_one(self):
        response = self.user_client.reset_password_set_new_one("new_password", "new_password")
        self.assertEqual(response.status_code, 200)

    def test_delete_social(self):
        response = self.user_client.delete_social("example_social")
        self.assertEqual(response.status_code, 200)