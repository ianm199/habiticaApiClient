import unittest
from unittest.mock import Mock
from src.client import HabiticaBaseClient
from src.tags import HabiticaTagClient

class TestHabiticaTagClient(unittest.TestCase):

    def setUp(self):
        user_id = '123'
        api_key = '456'
        self.client = HabiticaTagClient(user_id, api_key)
        self.client.make_request = Mock()
        self.client.make_request.return_value = {}

    def test_create_tag(self):
        tag_name = 'some_tag_name'
        self.client.create_tag(tag_name)
        self.client.make_request.assert_called_once_with('POST', '/tags', data={'name': tag_name})

    def test_get_user_tags(self):
        self.client.get_user_tags()
        self.client.make_request.assert_called_once_with('GET', '/tags')

    def test_get_a_tag(self):
        tag_id = 'some_tag_id'
        self.client.get_a_tag(tag_id)
        self.client.make_request.assert_called_once_with('GET', f'/tags/{tag_id}')

    def test_update_a_tag(self):
        tag_id = 'some_tag_id'
        tag_name = 'some_tag_name'
        self.client.update_a_tag(tag_id, tag_name)
        self.client.make_request.assert_called_once_with('PUT', f'/tags/{tag_id}', data={'name': tag_name})

    def test_reorder_tags(self):
        tag_id = 'some_tag_id'
        position = 3
        self.client.reorder_tags(tag_id, position)
        self.client.make_request.assert_called_once_with('POST', '/reorder-tags', data={'tagId': tag_id, 'to': position})

    def test_delete_a_tag(self):
        tag_id = 'some_tag_id'
        self.client.delete_a_tag(tag_id)
        self.client.make_request.assert_called_once_with('DELETE', f'/tags/{tag_id}')

if __name__ == '__main__':
    unittest.main()
