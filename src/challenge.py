from client import HabiticaBaseClient
from typing import List, Dict
from typing import Union

class HabiticaChallengeClient(HabiticaBaseClient):
    def assign_task(self, task_id: str, user_ids: List[str]) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/assign', json={"assignedUserIds": user_ids})

    def create_challenge_task(self, challenge_id: str, task_details: Dict[str, Union[str, int, bool, List]]) -> Dict:
        return self.make_request('POST', f'/tasks/challenge/{challenge_id}', json=task_details)