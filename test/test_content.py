import unittest
from unittest import mock
from requests.models import PreparedRequest
from typing import Dict
from src.content import HabiticaContentClient

class TestHabiticaContentClient(unittest.TestCase):

    def setUp(self):
        self.client = HabiticaContentClient("test_user", "test_api_key")

    def test_get_all_available_content_objects(self):
        mock_response = {
            "items": [
                {"name": "Sword", "type": "weapon"},
                {"name": "Potion", "type": "consumable"}
            ],
            "quests": [
                {"name": "Main Quest", "type": "main"},
                {"name": "Side Quest", "type": "side"}
            ]
        }
        with mock.patch.object(self.client, 'make_request') as mock_make_request:
            mock_make_request.return_value = mock_response

            response = self.client.get_all_available_content_objects(language='en')

            self.assertIsInstance(response, Dict)
            self.assertEqual(response['items'][0]['name'], 'Sword')
            self.assertEqual(response['quests'][1]['type'], 'side')

if __name__ == '__main__':
    unittest.main()
