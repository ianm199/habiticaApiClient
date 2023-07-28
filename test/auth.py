import os
import unittest
from unittest.mock import Mock
from src.client import HabiticaBaseClient
from src.auth import HabiticaUserClient


class TestHabiticaUserClient(unittest.TestCase):

    def setUp(self):
        user_id = os.environ.get("HABITICA_TEST_USER_ID")
        api_key = os.environ.get("HABITIICA_TEST_API_KEY")
        self.user_client = HabiticaUserClient(user_id, api_key)
        self.mock_make_request = Mock()
        self.user_client.make_request = self.mock_make_request

    def test_register_local(self):
        username = "testuser"
        email = "test@test.com"
        password = "testpass"
        confirmPassword = "testpass"
        expected_data = {"username": username, "email": email, "password": password, "confirmPassword": confirmPassword}

        self.user_client.register_local(username, email, password, confirmPassword)

        self.mock_make_request.assert_called_once_with('POST', '/user/auth/local/register', data=expected_data)

    def test_login_local(self):
        username = "testuser"
        password = "testpass"
        expected_data = {"username": username, "password": password}

        self.user_client.login_local(username, password)

        self.mock_make_request.assert_called_once_with('POST', '/user/auth/local/login', data=expected_data)

    def test_update_username(self):
        username = "newusername"
        password = "testpass"
        expected_data = {"username": username, "password": password}

        self.user_client.update_username(username, password)

        self.mock_make_request.assert_called_once_with('PUT', '/user/auth/update-username', data=expected_data)

    def test_update_password(self):
        password = "testpass"
        newPassword = "newpass"
        confirmPassword = "newpass"
        expected_data = {"password": password, "newPassword": newPassword, "confirmPassword": confirmPassword}

        self.user_client.update_password(password, newPassword, confirmPassword)

        self.mock_make_request.assert_called_once_with('PUT', '/user/auth/update-password', data=expected_data)

    def test_reset_password(self):
        email = "test@test.com"
        expected_data = {"email": email}

        self.user_client.reset_password(email)

        self.mock_make_request.assert_called_once_with('POST', '/user/reset-password', data=expected_data)

    def test_update_email(self):
        newEmail = "new@test.com"
        password = "testpass"
        expected_data = {"newEmail": newEmail, "password": password}

        self.user_client.update_email(newEmail, password)

        self.mock_make_request.assert_called_once_with('PUT', '/user/auth/update-email', data=expected_data)

    def test_reset_password_set_new_one(self):
        newPassword = "newpass"
        confirmPassword = "newpass"
        expected_data = {"newPassword": newPassword, "confirmPassword": confirmPassword}

        self.user_client.reset_password_set_new_one(newPassword, confirmPassword)

        self.mock_make_request.assert_called_once_with('POST', '/user/auth/reset-password-set-new-one', data=expected_data)

    def test_delete_social(self):
        network = "twitter"
        expected_path = f'/user/auth/social/{network}'

        self.user_client.delete_social(network)

        self.mock_make_request.assert_called_once_with('DELETE', expected_path)