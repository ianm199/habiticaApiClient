from client import HabiticaBaseClient

class HabiticaInboxClient(HabiticaBaseClient):
    def get_inbox_messages(self, page: int = None, conversation: str = None) -> dict:
        params = {}
        if page:
            params['page'] = page
        if conversation:
            params['conversation'] = conversation

        return self.make_request('GET', '/inbox/messages', params=params)