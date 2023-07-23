from src.client import HabiticaBaseClient
from typing import Dict, Any, List


class HabiticaGroupClient(HabiticaBaseClient):

    def create_group(self, name: str, group_type: str, privacy: str) -> Dict:
        """
        Create a new group

        :param name: The name of the new group
        :param group_type: The type of the group, either 'guild' or 'party'
        :param privacy: The privacy settings of the group, either 'private' or 'public'
                        (note: parties MUST be private)
        :return: The created group data
        """
        data = {
            "name": name,
            "type": group_type,
            "privacy": privacy
        }
        return self.make_request('POST', '/groups', data=data)

    def create_group_plan(self) -> Dict:
        """
        Create a new group and redirect to the correct payment
        :return: The created group data
        """
        return self.make_request('POST', '/groups/create-plan')

    def get_user_groups(self, group_type: str, paginate: str = None, page: int = None) -> Dict:
        """
        Get groups for a user

        :param group_type: The type of groups to retrieve, can be a string like 'tavern,party'
        :param paginate: When true guilds are returned in groups of 30
        :param page: Page number when pagination is enabled
        :return: The groups data
        """
        params = {"type": group_type}
        if paginate:
            params['paginate'] = paginate
        if page is not None:
            params['page'] = page

        return self.make_request('GET', '/groups', params=params)

    def get_group(self, group_id: str) -> Dict:
        """
        Get a group by its ID

        :param group_id: The ID of the group
        :return: The group data
        """
        return self.make_request('GET', f'/groups/{group_id}')

    def update_group(self, group_id: str, data: Dict[str, Any]) -> Dict:
        """
        Update a group with new data

        :param group_id: The ID of the group
        :param data: The data to update the group with
        :return: The updated group data
        """
        return self.make_request('PUT', f'/groups/{group_id}', data=data)

    def join_group(self, group_id: str) -> Dict:
        """
        Join a group

        :param group_id: The ID of the group
        :return: The group data after joining
        """
        return self.make_request('POST', f'/groups/{group_id}/join')

    def reject_group_invite(self, group_id: str) -> Dict:
        """
        Reject a group invitation

        :param group_id: The ID of the group
        :return: The group data after rejecting the invite
        """
        return self.make_request('POST', f'/groups/{group_id}/reject-invite')

    def leave_group(self, group_id: str, keep: str = None, keep_challenges: str = None) -> Dict:
        """
        Leave a group

        :param group_id: The ID of the group
        :param keep: Whether or not to keep challenge tasks belonging to the group being left
        :param keep_challenges: Whether or not to remain in the challenges of the group being left
        :return: The group data after leaving
        """
        data = {}
        if keep:
            data['keep'] = keep
        if keep_challenges:
            data['keepChallenges'] = keep_challenges
        return self.make_request('POST', f'/groups/{group_id}/leave', data=data)

    def remove_group_member(self, group_id: str, member_id: str, message: str = None) -> Dict:
        """
        Remove a member from a group

        :param group_id: The ID of the group
        :param member_id: The ID of the member to remove
        :param message: The message to send to the removed member
        :return: The group data after removing the member
        """
        params = {}
        if message:
            params['message'] = message
        return self.make_request('POST', f'/groups/{group_id}/removeMember/{member_id}', params=params)


    def invite_to_group(self, group_id: str, emails: List[Dict[str, str]] = None, uuids: List[str] = None) -> Dict:
        """
        Invite users to a group

        :param group_id: The ID of the group
        :param emails: A list of dicts, each representing an email address to invite
        :param uuids: A list of uuids to invite
        :return: The group data after the invitation
        """
        data = {}
        if emails:
            data['emails'] = emails
        if uuids:
            data['uuids'] = uuids
        return self.make_request('POST', f'/groups/{group_id}/invite', data=data)

    def add_group_manager(self, group_id: str) -> Dict:
        """
        Add a manager to a group

        :param group_id: The ID of the group
        :return: The group data after adding the manager
        """
        return self.make_request('POST', f'/groups/{group_id}/add-manager')

    def remove_group_manager(self, group_id: str) -> Dict:
        """
        Remove a manager from a group

        :param group_id: The ID of the group
        :return: The group data after removing the manager
        """
        return self.make_request('POST', f'/groups/{group_id}/remove-manager')

    def get_group_plans(self) -> List[Dict]:
        """
        Get group plans for a user

        :return: An array of the requested groups with a group plan
        """
        return self.make_request('GET', '/group-plans')

    def get_looking_for_party(self, page: int = None) -> List[Dict]:
        """
        Get users in search of parties

        :param page: Page number, defaults to 0
        :return: An array of users looking for a party
        """
        params = {}
        if page is not None:
            params['page'] = page
        return self.make_request('GET', '/looking-for-party', params=params)

