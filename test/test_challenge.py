import unittest
from unittest.mock import Mock
from src.challenge import HabiticaChallengeClient

class TestHabiticaChallengeClient(unittest.TestCase):

    def setUp(self):
        user_id = "test_user_id"
        api_key = "test_api_key"
        self.client = HabiticaChallengeClient(user_id, api_key)

    def test_assign_task(self):
        task_id = "test_task_id"
        user_ids = ["user1", "user2"]
        expected_response = {"success": True}
        
        self.client.make_request = Mock(return_value=expected_response)
        
        response = self.client.assign_task(task_id, user_ids)
        
        self.assertEqual(response, expected_response)
        self.client.make_request.assert_called_once_with('POST', f'/tasks/{task_id}/assign', json={"assignedUserIds": user_ids})

    def test_create_challenge_task(self):
        challenge_id = "test_challenge_id"
        task_details = {
            "text": "Test task",
            "type": "todo",
            "notes": "Test notes"
        }
        expected_response = {"success": True}
        
        self.client.make_request = Mock(return_value=expected_response)
        
        response = self.client.create_challenge_task(challenge_id, task_details)
        
        self.assertEqual(response, expected_response)
        self.client.make_request.assert_called_once_with('POST', f'/tasks/challenge/{challenge_id}', json=task_details)
        
if __name__ == '__main__':
    unittest.main()