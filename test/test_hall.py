from unittest.mock import Mock
import unittest
from src.hall import HabiticaHallClient


class TestHabiticaHallClient(unittest.TestCase):

    def setUp(self):
        self.hall_client = HabiticaHallClient("user", "api_key")

    def test_get_all_patrons(self):
        mock_make_request = Mock(return_value={"status": "success", "data": []})
        self.hall_client.make_request = mock_make_request

        response = self.hall_client.get_all_patrons(page=0)

        self.assertEqual(response, {"status": "success", "data": []})
        mock_make_request.assert_called_once_with('GET', '/hall/patrons', params={'page': 0})

    def test_get_all_heroes(self):
        mock_make_request = Mock(return_value={"status": "success", "data": []})
        self.hall_client.make_request = mock_make_request

        response = self.hall_client.get_all_heroes()

        self.assertEqual(response, {"status": "success", "data": []})
        mock_make_request.assert_called_once_with('GET', '/hall/heroes')

    def test_get_hero(self):
        hero_id = "12345"
        mock_make_request = Mock(return_value={"status": "success", "data": {"id": hero_id}})
        self.hall_client.make_request = mock_make_request

        response = self.hall_client.get_hero(heroId=hero_id)

        self.assertEqual(response, {"status": "success", "data": {"id": hero_id}})
        mock_make_request.assert_called_once_with('GET', f'/hall/heroes/{hero_id}')

    def test_update_hero(self):
        hero_id = "12345"
        data = {"name": "John Doe", "level": 50}
        mock_make_request = Mock(return_value={"status": "success", "data": {"id": hero_id}})
        self.hall_client.make_request = mock_make_request

        response = self.hall_client.update_hero(heroId=hero_id, data=data)

        self.assertEqual(response, {"status": "success", "data": {"id": hero_id}})
        mock_make_request.assert_called_once_with('PUT', f'/hall/heroes/{hero_id}', data=data)

    def test_get_hero_party(self):
        group_id = "abcde"
        mock_make_request = Mock(return_value={"status": "success", "data": {"id": group_id}})
        self.hall_client.make_request = mock_make_request

        response = self.hall_client.get_hero_party(groupId=group_id)

        self.assertEqual(response, {"status": "success", "data": {"id": group_id}})
        mock_make_request.assert_called_once_with('GET', f'/hall/heroes/party/{group_id}')