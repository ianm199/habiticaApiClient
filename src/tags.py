from client import HabiticaBaseClient
from typing import Dict

class HabiticaTagClient(HabiticaBaseClient):
    def create_tag(self, name: str) -> Dict:
        return self.make_request('POST', '/tags', data={'name': name})

    def get_user_tags(self) -> Dict:
        return self.make_request('GET', '/tags')

    def get_a_tag(self, tag_id: str) -> Dict:
        return self.make_request('GET', f'/tags/{tag_id}')

    def update_a_tag(self, tag_id: str, name: str) -> Dict:
        return self.make_request('PUT', f'/tags/{tag_id}', data={'name': name})

    def reorder_tags(self, tag_id: str, to: int) -> Dict:
        return self.make_request('POST', '/reorder-tags', data={'tagId': tag_id, 'to': to})

    def delete_a_tag(self, tag_id: str) -> Dict:
        return self.make_request('DELETE', f'/tags/{tag_id}')