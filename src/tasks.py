import requests
from typing import List, Dict, Union
from client import HabiticaBaseClient


class HabiticaTaskClient(HabiticaBaseClient):
    def get_user_tasks(self, task_type: str = None, due_date: str = None) -> List[Dict]:
        params = {}
        if task_type:
            params['type'] = task_type
        if due_date:
            params['dueDate'] = due_date

        return self.make_request('GET', '/tasks/user', params=params)

    def add_tag_to_task(self, task_id: str, tag_id: str) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/tags/{tag_id}')

    def add_checklist_item(self, task_id: str, text: str, completed: bool = False) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/checklist', json={"text": text, "completed": completed})


class HabiticaChallengeClient(HabiticaBaseClient):
    def assign_task(self, task_id: str, user_ids: List[str]) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/assign', json={"assignedUserIds": user_ids})

    def create_challenge_task(self, challenge_id: str, task_details: Dict[str, Union[str, int, bool, List]]) -> Dict:
        return self.make_request('POST', f'/tasks/challenge/{challenge_id}', json=task_details)

if __name__ == '__main__':
    print("test!")