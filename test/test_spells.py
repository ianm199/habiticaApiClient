import unittest
from unittest.mock import Mock
from src.client import HabiticaBaseClient
from src.spells import HabiticaSpellClient

class TestHabiticaUserClient(unittest.TestCase):

    def setUp(self):
        user_id = '123'
        api_key = '456'
        self.client = HabiticaSpellClient(user_id, api_key)
        self.client.make_request = Mock()
        self.client.make_request.return_value = {}

    def test_cast_spell_without_target(self):
        spell_id = 'some_spell_id'
        self.client.cast_spell(spell_id)
        self.client.make_request.assert_called_once_with('POST', f'/user/class/cast/{spell_id}', params={})

    def test_cast_spell_with_target(self):
        spell_id = 'some_spell_id'
        target_id = 'some_target_id'
        self.client.cast_spell(spell_id, target_id)
        self.client.make_request.assert_called_once_with('POST', f'/user/class/cast/{spell_id}', params={'targetId': target_id})

if __name__ == '__main__':
    unittest.main()
