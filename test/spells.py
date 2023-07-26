import unittest
from client import HabiticaUserClient

class TestHabiticaUserClient(unittest.TestCase):

    def setUp(self):
        self.api_key = "YOUR_API_KEY"
        self.user_id = "YOUR_USER_ID"
        self.user_client = HabiticaUserClient(self.user_id, self.api_key)

    def test_cast_spell_with_target(self):
        spell_id = "SPELL_ID"
        target_id = "TARGET_ID"

        response = self.user_client.cast_spell(spell_id, target_id)
        self.assertIsInstance(response, dict)
        # Add additional assertions as needed

    def test_cast_spell_without_target(self):
        spell_id = "SPELL_ID"

        response = self.user_client.cast_spell(spell_id)
        self.assertIsInstance(response, dict)
        # Add additional assertions as needed

if __name__ == '__main__':
    unittest.main()