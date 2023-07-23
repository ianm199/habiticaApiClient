import unittest
from unittest.mock import Mock
from src.tasks import HabiticaTaskClient

class TestHabiticaTaskClient(unittest.TestCase):
    def setUp(self):
        self.task_client = HabiticaTaskClient("test", "test")
        self.task_client.make_request = Mock()

    def test_get_user_tasks(self):
        self.task_client.get_user_tasks('todo', '2023-07-18')
        self.task_client.make_request.assert_called_with('GET', '/tasks/user', params={'type': 'todo', 'dueDate': '2023-07-18'})

    def test_add_tag_to_task(self):
        self.task_client.add_tag_to_task('task_id', 'tag_id')
        self.task_client.make_request.assert_called_with('POST', '/tasks/task_id/tags/tag_id')

    def test_add_checklist_item(self):
        self.task_client.add_checklist_item('task_id', 'text', False)
        self.task_client.make_request.assert_called_with('POST', '/tasks/task_id/checklist', json={"text": "text", "completed": False})

    def test_create_challenge_task(self):
        self.task_client.create_challenge_task('challenge_id', 'text', 'todo')
        self.task_client.make_request.assert_called_with('POST', '/tasks/challenge/challenge_id', json={"text": "text", "type": "todo", "attribute": None, "collapseChecklist": None, "notes": None, "date": None, "priority": None, "reminders": None, "frequency": None, "repeat": None, "everyX": None, "streak": None, "daysOfMonth": None, "weeksOfMonth": None, "startDate": None, "up": None, "down": None, "value": None})


    def test_delete_task(self):
        self.task_client.delete_task('task_id')
        self.task_client.make_request.assert_called_with('DELETE', '/tasks/task_id')

    def test_update_task(self):
        self.task_client.update_task('task_id', 'text')
        self.task_client.make_request.assert_called_with('PUT', '/tasks/task_id', json={"text": "text", "notes": None, "date": None, "priority": None, "attribute": None, "tags": None, "collapseChecklist": None, "reminders": None, "frequency": None, "everyX": None, "streak": None, "daysOfMonth": None, "weeksOfMonth": None, "startDate": None, "up": None, "down": None, "value": None})

    def test_score_task(self):
        self.task_client.score_task('task_id', 'up')

    def test_move_group_task(self):
        self.task_client.move_group_task('group_id', 'task_id', 1)
        self.task_client.make_request.assert_called_with('POST', '/group/group_id/tasks/task_id/move/to/1')

    def test_move_task(self):
        self.task_client.move_task('task_id', 1)
        self.task_client.make_request.assert_called_with('POST', '/tasks/task_id/move/to/1')

    def test_require_more_work_for_task(self):
        self.task_client.require_more_work_for_task('task_id', 'user_id')
        self.task_client.make_request.assert_called_with('POST', '/tasks/task_id/needs-work/user_id')

    def test_score_checklist_item(self):
        self.task_client.score_checklist_item('task_id', 'item_id')
        self.task_client.make_request.assert_called_with('POST', '/tasks/task_id/checklist/item_id/score')

    def test_unassign_user_from_task(self):
        self.task_client.unassign_user_from_task('task_id', 'user_id')
        self.task_client.make_request.assert_called_with('POST', '/tasks/task_id/unassign/user_id')

    def test_unlink_challenge_task(self):
        self.task_client.unlink_challenge_task('task_id', 'keep')
        self.task_client.make_request.assert_called_with('POST', '/tasks/unlink-one/task_id',
                                                         query_params={"keep": 'keep'})

    def test_unlink_all_tasks_from_challenge(self):
        self.task_client.unlink_all_tasks_from_challenge('challenge_id', 'keep')
        self.task_client.make_request.assert_called_with('POST', '/tasks/unlink-all/challenge_id',
                                                         query_params={"keep": 'keep'})

    def test_update_checklist_item(self):
        self.task_client.update_checklist_item('task_id', 'item_id', 'text', False)
        self.task_client.make_request.assert_called_with('PUT', '/tasks/task_id/checklist/item_id',
                                                         body={"text": 'text', "completed": False})

if __name__ == '__main__':
    unittest.main()