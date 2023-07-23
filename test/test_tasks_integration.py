import os
import unittest
from src.tasks import HabiticaTaskClient

class TestHabiticaTaskClient(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv('HABITICA_TEST_API_KEY')
        user_id = os.getenv('HABITICA_TEST_USER_ID')
        self.task_client = HabiticaTaskClient(user_id, api_key)
        self.dummy_task = self.task_client.create_user_task("Dummy Data", task_type="todo")

    def test_get_user_tasks(self):
        response = self.task_client.get_user_tasks()
        self.assertTrue(response, list)

    def test_create_user_task(self):
        daily_user_task = self.task_client.create_user_task("Example daily", task_type="todo")
        self.assertEqual(daily_user_task['text'],"Example daily")
        self.assertEqual(daily_user_task['type'],"todo")

    def test_add_checklist_item_and_score_update(self):
        checklist_item = self.task_client.add_checklist_item(task_id=self.dummy_task['id'], text="test checklist", completed="false")
        self.assertTrue(checklist_item['checklist'][0]['text'], "test checklist")
        score_checklist = self.task_client.score_checklist_item(task_id=self.dummy_task['id'], item_id=checklist_item['checklist'][0]['id'])
        self.assertIsInstance(score_checklist, dict)
        update_checklist_item = self.task_client.update_checklist_item(self.dummy_task['id'], checklist_item['checklist'][0]['id'], text="update", completed=False)
        self.assertEqual(update_checklist_item['checklist'][0]['text'], "update")
        print("test")
    def test_delete_task(self):
        task = self.task_client.create_user_task(text="task", task_type="todo")
        deleted = self.task_client.delete_task(task_id=task['id'])
        self.assertEqual(deleted, {})

    def test_update_task(self):
        updated = self.task_client.update_task(task_id=self.dummy_task['id'], text="new text")
        self.assertEqual(updated['text'], "new text")

    def test_score_task(self):
        scored = self.task_client.score_task(task_id=self.dummy_task['id'], direction="up")
        self.assertEqual(scored['class'], 'warrior')

    # def test_require_more_work_for_task(self):
    # Requires groups
    #     more_work = self.task_client.require_more_work_for_task(self.dummy_task['id'], )


    def test_move_task(self):
        move_task = self.task_client.move_task(task_id=self.dummy_task['id'], position=-1)
        self.assertEqual(move_task[-1], self.dummy_task['id'])
        move_task_again = self.task_client.move_task(task_id=self.dummy_task['id'], position=0)
        self.assertEqual(move_task_again[0], self.dummy_task['id'])
