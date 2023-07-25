from typing import Optional, Dict
from client import HabiticaBaseClient
import requests

class HabiticaMemberClient(HabiticaBaseClient):
    def get_member_profile(self, member_id: str) -> Dict:
        return self.make_request('GET', f'/members/{member_id}')

    def get_member_achievements(self, member_id: str) -> Dict:
        return self.make_request('GET', f'/members/{member_id}/achievements')

    def get_group_members(self, group_id: str, lastId: Optional[str] = None, limit: Optional[int] = None, includeAllPublicFields: Optional[bool] = None, includeTasks: Optional[bool] = None) -> Dict:
        params = {"lastId": lastId, "limit": limit, "includeAllPublicFields": includeAllPublicFields, "includeTasks": includeTasks}
        return self.make_request('GET', f'/groups/{group_id}/members', params=params)

    def get_group_invites(self, group_id: str, lastId: Optional[str] = None, limit: Optional[int] = None, includeAllPublicFields: Optional[bool] = None) -> Dict:
        params = {"lastId": lastId, "limit": limit, "includeAllPublicFields": includeAllPublicFields}
        return self.make_request('GET', f"/groups/{group_id}/invites", params=params)

    def get_challenge_members(self, challenge_id: str, lastId: Optional[str] = None, limit: Optional[int] = None, includeTasks: Optional[bool] = None, includeAllPublicFields: Optional[bool] = None) -> Dict:
        params = {"lastId": lastId, "limit": limit, "includeTasks": includeTasks, "includeAllPublicFields": includeAllPublicFields}
        return self.make_request('GET', f'/challenges/{challenge_id}/members', params=params)

    def get_challenge_member_progress(self, challenge_id: str, member_id: str) -> Dict:
        return self.make_request('GET', f'/challenges/{challenge_id}/members/{member_id}')

    def get_objections_to_interaction(self, to_user_id: str, interaction: str) -> Dict:
        return self.make_request('GET', f'/members/{to_user_id}/objections/{interaction}')

    def send_private_message(self, message: str, to_user_id: str) -> Dict:
        return self.make_request('POST', '/members/send-private-message', data={"message": message, "toUserId": to_user_id})

    def transfer_gems(self, message: str, to_user_id: str, gem_amount: int) -> Dict:
        return self.make_request('POST', '/members/transfer-gems', data={"message": message, "toUserId": to_user_id, "gemAmount": gem_amount})