from typing import Dict, Optional
import requests
from src.client import HabiticaBaseClient

class HabiticaQuestClient(HabiticaBaseClient):
    def invite_users_to_quest(self, groupId: str, questKey: str) -> Dict:
        return self.make_request("POST", f"/groups/{groupId}/quests/invite/{questKey}")
    
    def accept_quest(self, groupId: str) -> Dict:
        return self.make_request("POST", f"/groups/{groupId}/quests/accept")
    
    def reject_quest(self, groupId: str) -> Dict:
        return self.make_request("POST", f"/groups/{groupId}/quests/reject")

    def force_start_quest(self, groupId: str) -> Dict:
        return self.make_request("POST", f"/groups/{groupId}/quests/force-start")

    def cancel_quest(self, groupId: str) -> Dict:
        return self.make_request("POST", f"/groups/{groupId}/quests/cancel")

    def abort_quest(self, groupId: str) -> Dict:
        return self.make_request("POST", f"/groups/{groupId}/quests/abort")
    
    def leave_quest(self, groupId: str) -> Dict:
        return self.make_request("POST", f"/groups/{groupId}/quests/leave")