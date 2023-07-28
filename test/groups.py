import unittest
from src.groups import HabiticaGroupClient
from typing import Dict, Any, List
from unittest.mock import MagicMock, patch

class TestHabiticaGroupClient(unittest.TestCase):

    def setUp(self):
        api_key = "test_api_key"
        user_id = "test_user_id"
        self.group_client = HabiticaGroupClient(user_id, api_key)
    
    @patch('src.client.HabiticaBaseClient.make_request')
    def test_create_group(self, mock_make_request):
        mock_make_request.return_value = {"data": {"id": "test_group_id"}}
        response = self.group_client.create_group("Test Group", "guild", "private")
        self.assertEqual(response, {"data": {"id": "test_group_id"}})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_create_group_plan(self, mock_make_request):
        mock_make_request.return_value = {"data": {"id": "test_group_id"}}
        response = self.group_client.create_group_plan()
        self.assertEqual(response, {"data": {"id": "test_group_id"}})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_get_user_groups(self, mock_make_request):
        mock_make_request.return_value = {"data": [{"id": "test_group_id", "name": "Test Group"}]}
        response = self.group_client.get_user_groups("guild")
        self.assertEqual(response, {"data": [{"id": "test_group_id", "name": "Test Group"}]})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_get_group(self, mock_make_request):
        mock_make_request.return_value = {"data": {"id": "test_group_id", "name": "Test Group"}}
        response = self.group_client.get_group("test_group_id")
        self.assertEqual(response, {"data": {"id": "test_group_id", "name": "Test Group"}})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_update_group(self, mock_make_request):
        mock_make_request.return_value = {"data": {"id": "test_group_id", "name": "Updated Group"}}
        response = self.group_client.update_group("test_group_id", {"name": "Updated Group"})
        self.assertEqual(response, {"data": {"id": "test_group_id", "name": "Updated Group"}})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_join_group(self, mock_make_request):
        mock_make_request.return_value = {"success": True}
        response = self.group_client.join_group("test_group_id")
        self.assertEqual(response, {"success": True})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_reject_group_invite(self, mock_make_request):
        mock_make_request.return_value = {"success": True}
        response = self.group_client.reject_group_invite("test_group_id")
        self.assertEqual(response, {"success": True})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_leave_group(self, mock_make_request):
        mock_make_request.return_value = {"success": True}
        response = self.group_client.leave_group("test_group_id")
        self.assertEqual(response, {"success": True})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_remove_group_member(self, mock_make_request):
        mock_make_request.return_value = {"success": True}
        response = self.group_client.remove_group_member("test_group_id", "test_member_id")
        self.assertEqual(response, {"success": True})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_invite_to_group(self, mock_make_request):
        mock_make_request.return_value = {"success": True}
        response = self.group_client.invite_to_group("test_group_id")
        self.assertEqual(response, {"success": True})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_add_group_manager(self, mock_make_request):
        mock_make_request.return_value = {"success": True}
        response = self.group_client.add_group_manager("test_group_id")
        self.assertEqual(response, {"success": True})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_remove_group_manager(self, mock_make_request):
        mock_make_request.return_value = {"success": True}
        response = self.group_client.remove_group_manager("test_group_id")
        self.assertEqual(response, {"success": True})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_get_group_plans(self, mock_make_request):
        mock_make_request.return_value = {"data": [{"id": "test_group_plan_id", "name": "Test Plan"}]}
        response = self.group_client.get_group_plans()
        self.assertEqual(response, {"data": [{"id": "test_group_plan_id", "name": "Test Plan"}]})

    @patch('src.client.HabiticaBaseClient.make_request')
    def test_get_looking_for_party(self, mock_make_request):
        mock_make_request.return_value = {"data": [{"id": "test_user_id", "name": "Test User"}]}
        response = self.group_client.get_looking_for_party()
        self.assertEqual(response, {"data": [{"id": "test_user_id", "name": "Test User"}]})