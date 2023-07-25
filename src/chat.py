from typing import Optional, Dict
import requests
from client import HabiticaBaseClient

class HabiticaChatClient(HabiticaBaseClient):
    def get_group_chat_messages(self, groupId: str) -> Dict:
        return self.make_request('GET', f'/groups/{groupId}/chat')

    def post_chat_message_to_group(self, groupId: str, message: str, previousMsg: Optional[str] = None) -> Dict:
        data = {"message": message}
        if previousMsg:
            data["previousMsg"] = previousMsg
        return self.make_request('POST', f'/groups/{groupId}/chat', data=data)

    def like_group_chat_message(self, groupId: str, chatId: str) -> Dict:
        return self.make_request('POST', f'/groups/{groupId}/chat/{chatId}/like')

    def flag_group_chat_message(self, groupId: str, chatId: str, comment: Optional[str] = None) -> Dict:
        data = {}
        if comment:
            data["comment"] = comment
        return self.make_request('POST', f'/groups/{groupId}/chat/{chatId}/flag', data=data)

    def clear_flags_group_chat_message(self, groupId: str, chatId: str) -> Dict:
        return self.make_request('POST', f'/groups/{groupId}/chat/{chatId}/clearflags')

    def mark_group_messages_as_read(self, groupId: str) -> Dict:
        return self.make_request('POST', f'/groups/{groupId}/chat/seen')

    def delete_group_chat_message(self, groupId: str, chatId: str, previousMsg: Optional[str] = None) -> Dict:
        data = {}
        if previousMsg:
            data["previousMsg"] = previousMsg
        return self.make_request('DELETE', f'/groups/{groupId}/chat/{chatId}', data=data)