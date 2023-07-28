import unittest
from unittest.mock import Mock
from src.client import HabiticaBaseClient
from src.tasks import HabiticaTaskClient

class TestHabiticaTaskClient(unittest.TestCase):
    def setUp(self):
        self.client = HabiticaTaskClient('user_id', 'api_key')
        self.client.make_request = Mock()

    def test_get_user_tasks(self):
        self.client.get_user_tasks('daily', '2023-07-27')
        self.client.make_request.assert_called_once_with(
            'GET', '/tasks/user', params={'type': 'daily', 'dueDate': '2023-07-27'})

    def test_add_tag_to_task(self):
        self.client.add_tag_to_task('task_id', 'tag_id')
        self.client.make_request.assert_called_once_with(
            'POST', '/tasks/task_id/tags/tag_id')

    def test_add_checklist_item(self):
        self.client.add_checklist_item('task_id', 'Buy milk', True)
        self.client.make_request.assert_called_once_with(
            'POST', '/tasks/task_id/checklist', data={"text": 'Buy milk', "completed": True})

    # Similar tests for other methods...

    def test_delete_task(self):
        self.client.delete_task('task_id')
        self.client.make_request.assert_called_once_with(
            'DELETE', '/tasks/task_id')

    def test_score_task(self):
        self.client.score_task('task_id', 'up')
        self.client.make_request.assert_called_once_with(
            'POST', '/tasks/task_id/score/up')

        # Continue from previous test suite

    def test_move_task(self):
        self.client.move_task('task_id', 1)
        self.client.make_request.assert_called_once_with(
            'POST', '/tasks/task_id/move/to/1')

    def test_require_more_work_for_task(self):
        self.client.require_more_work_for_task('task_id', 'user_id')
        self.client.make_request.assert_called_once_with(
            'POST', '/tasks/task_id/needs-work/user_id')

    def test_score_checklist_item(self):
        self.client.score_checklist_item('task_id', 'item_id')
        self.client.make_request.assert_called_once_with(
            'POST', '/tasks/task_id/checklist/item_id/score')

    def test_unassign_user_from_task(self):
        self.client.unassign_user_from_task('task_id', 'assigned_user_id')
        self.client.make_request.assert_called_once_with(
            'POST', '/tasks/task_id/unassign/assigned_user_id')

    def test_unlink_challenge_task(self):
        self.client.unlink_challenge_task('task_id', 'keep')
        self.client.make_request.assert_called_once_with(
            'POST', '/tasks/unlink-one/task_id', query_params={"keep": 'keep'})

    def test_unlink_all_tasks_from_challenge(self):
        self.client.unlink_all_tasks_from_challenge('challenge_id', 'keep')
        self.client.make_request.assert_called_once_with(
            'POST', '/tasks/unlink-all/challenge_id', query_params={"keep": 'keep'})

    def test_update_checklist_item(self):
        self.client.update_checklist_item('task_id', 'item_id', 'Buy milk', True)
        self.client.make_request.assert_called_once_with(
            'PUT', '/tasks/task_id/checklist/item_id', data={"text": 'Buy milk', "completed": True})


    def test_update_task_all_params(self):
        self.client.update_task(
            'task_id', 'text', 'notes', '2023-07-27', 2.0, 'attribute', ['tag1', 'tag2'], True,
            [{'id': 'reminder1', 'time': '2023-07-27T10:00:00'}], 'weekly', 3, 5,
            [1, 15], [2, 4], '2023-07-01', True, False, 1.5)

        expected_body = {
            "text": 'text',
            "notes": 'notes',
            "date": '2023-07-27',
            "priority": 2.0,
            "attribute": 'attribute',
            "tags": ['tag1', 'tag2'],
            "collapseChecklist": True,
            "reminders": [{'id': 'reminder1', 'time': '2023-07-27T10:00:00'}],
            "frequency": 'weekly',
            "everyX": 3,
            "streak": 5,
            "daysOfMonth": [1, 15],
            "weeksOfMonth": [2, 4],
            "startDate": '2023-07-01',
            "up": True,
            "down": False,
            "value": 1.5
        }
        self.client.make_request.assert_called_once_with(
            'PUT', '/tasks/task_id', data=expected_body)

    def test_update_task_partial_params(self):
        self.client.update_task('task_id', 'text', 'notes', '2023-07-27')

        expected_body = {
            "text": 'text',
            "notes": 'notes',
            "date": '2023-07-27',
            "priority": None,
            "attribute": None,
            "tags": None,
            "collapseChecklist": None,
            "reminders": None,
            "frequency": None,
            "everyX": None,
            "streak": None,
            "daysOfMonth": None,
            "weeksOfMonth": None,
            "startDate": None,
            "up": None,
            "down": None,
            "value": None
        }
        self.client.make_request.assert_called_once_with(
            'PUT', '/tasks/task_id', data=expected_body)

    # end of test suite


if __name__ == '__main__':
    unittest.main()
